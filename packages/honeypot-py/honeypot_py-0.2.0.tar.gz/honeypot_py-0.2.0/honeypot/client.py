"""
Honeypot Python Client

A simple client for tracking events and user behavior.

Basic Usage:
    from honeypot import Honeypot

    # Initialize with your endpoint
    hp = Honeypot("https://webhook.site/your-endpoint")

    # Track a simple event
    hp.track("Page View")

    # Track with properties
    hp.track("Purchase", {
        "product_id": "123",
        "amount": 99.99,
        "currency": "USD"
    })

With Request Object (Django/Flask):
    # Automatically extracts user agent, IP, and other request data
    hp.with_request(request).track("API Call")

    # With user identification
    hp.with_request(request).identify("user@example.com").track("Login")

    # Check if request is from browser
    if hp.is_browser():
        hp.track("Browser Event")

Path-based Event Tracking:
    # Set up path -> event mapping
    hp = Honeypot("https://webhook.site/your-endpoint")
    hp.event_paths({
        "config": "/api/user/user_config/",
        "feed": "/api/feed/*",  # Wildcard matching
        "profile": "/api/user/profile/"
    })

    # Events will be tracked automatically based on request path
    hp.with_request(request).track()  # Event name determined from path

    # Manual event names still work
    hp.track("custom_event")  # Explicitly named event
"""

import asyncio
import aiohttp
import ipaddress
import logging
from typing import Optional, Dict, Any, Union
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

def is_valid_ip(ip: str) -> bool:
    """Validate if string is a valid IP address."""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def is_private_ip(ip: str) -> bool:
    """Check if IP address is private."""
    try:
        return ipaddress.ip_address(ip).is_private
    except ValueError:
        return False

class Honeypot:
    """
    Honeypot client for tracking events and user behavior.
    
    Attributes:
        endpoint (str): The webhook endpoint to send events to
        user_id (Optional[str]): Current user identifier
        request (Any): Request object (Django/Flask) for extracting metadata
        ip (Optional[str]): IP address override
        event_path_mapping (Optional[Dict[str, str]]): Path to event name mapping
    """

    def __init__(self, endpoint: str):
        """
        Initialize Honeypot client.

        Args:
            endpoint: Webhook endpoint URL to send events to
        """
        self.endpoint = endpoint
        self.user_id = None
        self.request = None
        self.ip = None
        self.event_path_mapping = None

    def with_request(self, request: Any) -> 'Honeypot':
        """Attach request object to extract headers and metadata."""
        self.request = request
        return self

    def identify(self, user_id: str) -> 'Honeypot':
        """Set user identifier for tracking."""
        self.user_id = user_id
        return self

    def set_ip(self, ip: str) -> 'Honeypot':
        """Override IP address for tracking."""
        self.ip = ip
        return self

    def is_browser(self) -> bool:
        """Check if request is from a browser."""
        if not self.request:
            return False
        return bool(self.request.headers.get('Browser-Token'))

    def _get_client_ip(self) -> str:
        """Extract client IP from request object using specified header order"""
        if self.ip:
            return self.ip
            
        if not self.request:
            return ''

        # Headers to check in priority order
        ip_headers = [
            ('CF-Connecting-IP', lambda x: x),
            ('Forwarded', lambda x: next((
                part.split('=', 1)[1].strip().strip('[]').split(':')[0]
                for part in x.replace(' ', '').split(';')
                for sub_part in part.split(',')
                if sub_part.startswith('for=')
            ), None)),
            ('X-Forwarded-For', lambda x: x.split(',')[0].strip()),
            ('Remote-Addr', lambda x: x)
        ]

        first_ip_maybe_private = None

        # Check headers in order
        for header, extractor in ip_headers:
            value = self.request.headers.get(header)
            if not value:
                continue
                
            ip = extractor(value)
            if not ip or not is_valid_ip(ip):
                continue

            if not first_ip_maybe_private:
                first_ip_maybe_private = ip
                
            if not is_private_ip(ip):
                return ip

        return first_ip_maybe_private or ''

    def event_paths(self, path_mapping: Dict[str, str]) -> 'Honeypot':
        """
        Set path to event name mapping for automatic tracking.
        
        Args:
            path_mapping: Dictionary mapping event names to paths
                e.g. {"feed": "/api/feed/*"}
        """
        self.event_path_mapping = path_mapping
        return self

    def _get_event_name_from_path(self) -> Optional[str]:
        """Get event name from request path using configured mapping."""
        if not self.request or not self.event_path_mapping:
            return None
            
        path = getattr(self.request, 'path', '').split('?')[0].strip('/')
        
        for event_name, pattern in self.event_path_mapping.items():
            pattern = pattern.strip('/')
            
            if pattern.rstrip('*') == path:
                return event_name
                
            if pattern.endswith('*'):
                prefix = pattern.rstrip('*')
                if path.startswith(prefix):
                    return event_name
                    
        return None

    def _get_payload(self, event_name: str, properties: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Build event payload with request metadata."""
        payload = {
            'event_name': event_name,
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'user_id': self.user_id
        }

        if properties:
            payload['properties'] = properties

        if self.request:
            payload.update({
                'ip': self._get_client_ip(),
                'user_agent': self.request.headers.get('User-Agent', ''),
                'browser_token': self.request.headers.get('Browser-Token', ''),
                'device_id': self.request.headers.get('Device-Id', ''),
                'anonymous_id': self.request.headers.get('Anonymous-Id', ''),
                'path': getattr(self.request, 'path', None),
                'method': getattr(self.request, 'method', None)
            })

        return payload

    async def track_async(self, event_name: Optional[str] = None, properties: Optional[Dict[str, Any]] = None) -> None:
        """
        Track an event asynchronously.
        
        Args:
            event_name: Name of event to track (optional if path mapping is set)
            properties: Additional event properties
        """
        if not event_name:
            event_name = self._get_event_name_from_path()
            
        if not event_name:
            logger.debug(f"No event name provided and no mapping found for path: {getattr(self.request, 'path', None)}")
            return

        payload = self._get_payload(event_name, properties)
        logger.debug(f"Sending payload to {self.endpoint}: {payload}")

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    self.endpoint,
                    json=payload,
                    timeout=aiohttp.ClientTimeout(total=5)
                ) as response:
                    response_text = await response.text()
                    logger.debug(f"Response status: {response.status}, body: {response_text}")
                    if response.status != 200:
                        logger.error(f"Honeypot track failed with status {response.status}")
        except Exception as e:
            logger.exception(f"Error tracking event: {str(e)}")

    def track(self, event_name: Optional[str] = None, properties: Optional[Dict[str, Any]] = None) -> None:
        """
        Track an event synchronously.
        
        Args:
            event_name: Name of event to track (optional if path mapping is set)
            properties: Additional event properties
        """
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        
        loop.run_until_complete(self.track_async(event_name, properties)) 