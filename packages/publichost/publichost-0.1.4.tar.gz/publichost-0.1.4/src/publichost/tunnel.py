# src/publichost/tunnel.py
import asyncio
import json
import logging
import re
import socket
import os
import aiohttp
import websockets
import threading
from typing import Optional, Dict, Any
from websockets.exceptions import WebSocketException
from .exceptions import ConnectionError, ProxyError, TunnelError
from .utils import generate_subdomain, RESERVED_WORDS

logger = logging.getLogger(__name__)

class Tunnel:
    """A tunnel that makes a local port accessible via a public URL.
    
    This class creates a secure tunnel to expose a local port to the internet
    using WebSocket-based proxying. It handles connection management, request
    forwarding, and automatic reconnection.

    Attributes:
        port (int): The local port to tunnel
        subdomain (str): The subdomain for the public URL
        public_url (str): The complete public URL for accessing the tunnel
        
    Example:
        ```python
        tunnel = Tunnel(port=5000)
        print(f"🌍 Access your app at: {tunnel.public_url}")
        ```
    """

    SUBDOMAIN_PATTERN = re.compile(r'^[a-z0-9][a-z0-9-]{1,61}[a-z0-9]$')
    DEFAULT_WS_URL = "wss://tunnel.publichost.dev/ws"
    DEFAULT_PUBLIC_DOMAIN = "publichost.dev"
    MAX_RETRIES = 3
    RETRY_DELAY = 2  # seconds
    PING_INTERVAL = 30  # seconds
    REQUEST_TIMEOUT = 30  # seconds
    
    def __init__(
        self, 
        port: int, 
        subdomain: Optional[str] = None,
        dev_mode: bool = False,
        proxy: Optional[Dict[str, str]] = None
    ) -> None:
        """Initialize a new tunnel.

        Args:
            port: Local port to tunnel (1-65535)
            subdomain: Optional custom subdomain to use
            dev_mode: Enable development mode (uses localhost)
            proxy: Optional proxy configuration (e.g., {"http": "http://proxy:8080"})

        Raises:
            TunnelError: If the subdomain is invalid or reserved
            ConnectionError: If the tunnel service is unreachable
        """
        self._validate_port(port)
        self.port = port
        self.proxy = proxy
        self.subdomain = self._validate_subdomain(subdomain) if subdomain else generate_subdomain()
        
        # Configure URLs
        self.ws_url = self._get_ws_url(dev_mode)
        self.public_url = self._get_public_url(dev_mode)
        
        # Start tunnel in background
        self._start_background_tunnel()

    def _validate_port(self, port: int) -> None:
        """Validate the port number."""
        if not isinstance(port, int) or port < 1 or port > 65535:
            raise TunnelError("Port must be between 1 and 65535")

    def _get_ws_url(self, dev_mode: bool) -> str:
        """Get WebSocket URL based on environment."""
        if dev_mode:
            return f"ws://localhost:{self.port}/ws"
        ws_url = os.getenv("PUBLICHOST_WS_URL", self.DEFAULT_WS_URL)
        if not ws_url:
            raise TunnelError("PUBLICHOST_WS_URL environment variable is not set")
        return ws_url

    def _get_public_url(self, dev_mode: bool) -> str:
        """Get public URL based on environment."""
        domain = f"localhost:{self.port}" if dev_mode else os.getenv("PUBLICHOST_DOMAIN", self.DEFAULT_PUBLIC_DOMAIN)
        protocol = "http" if dev_mode else "https"
        return f"{protocol}://{self.subdomain}.{domain}"

    def _validate_subdomain(self, subdomain: str) -> str:
        """Validate and normalize a custom subdomain."""
        subdomain = subdomain.lower()
        if subdomain in RESERVED_WORDS:
            raise TunnelError(f"Subdomain '{subdomain}' is reserved")
        if not self.SUBDOMAIN_PATTERN.match(subdomain):
            raise TunnelError(
                "Subdomain must contain only letters, numbers, and hyphens, "
                "and must not start or end with a hyphen"
            )
        return subdomain

    def _start_background_tunnel(self) -> None:
        """Start the tunnel in a background thread."""
        self.tunnel_thread = threading.Thread(target=self._start_tunnel)
        self.tunnel_thread.daemon = True
        self.tunnel_thread.start()

    def _start_tunnel(self) -> None:
        """Start and maintain the tunnel connection."""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            for attempt in range(self.MAX_RETRIES):
                try:
                    loop.run_until_complete(self._connect())
                    break
                except Exception as e:
                    if attempt == self.MAX_RETRIES - 1:
                        raise ConnectionError("Unable to establish tunnel after retries") from e
                    logger.warning(f"Connection attempt {attempt + 1} failed, retrying...")
                    asyncio.sleep(self.RETRY_DELAY * (attempt + 1))
            
            logger.info(f"Tunnel established at {self.public_url}")
            loop.run_forever()
        except Exception as e:
            raise TunnelError(str(e))
        finally:
            loop.close()

    async def _connect(self) -> None:
        """Establish and maintain WebSocket connection."""
        try:
            async with websockets.connect(self.ws_url) as ws:
                await self._register_tunnel(ws)
                await asyncio.gather(
                    self._handle_messages(ws),
                    self._keep_alive(ws)
            )
        except Exception as e:
            logger.error(f"Connection error: {str(e)}")
            raise

    async def _register_tunnel(self, ws: websockets.WebSocketClientProtocol) -> None:
        """Register the tunnel with the server."""
        await ws.send(json.dumps({
            "type": "register",
            "tunnel_id": self.subdomain,
            "local_port": self.port
        }))

    async def _keep_alive(self, ws: websockets.WebSocketClientProtocol) -> None:
        """Maintain connection with periodic ping messages."""
        while True:
            try:
                await asyncio.sleep(self.PING_INTERVAL)
                await ws.send(json.dumps({"type": "ping"}))
            except Exception as e:
                logger.error(f"Keep-alive failed: {str(e)}")
                break

    async def _handle_messages(self, ws: websockets.WebSocketClientProtocol) -> None:
        """Handle incoming WebSocket messages."""
        async for message in ws:
            try:
                data = json.loads(message)
                if data["type"] == "request":
                    response = await self._handle_proxy_request(data)
                    await ws.send(json.dumps(response))
            except json.JSONDecodeError:
                logger.error("Invalid message format received")
            except Exception as e:
                logger.error(f"Error handling message: {str(e)}")

    async def _handle_proxy_request(self, data: dict) -> dict:
        """Handle and proxy an incoming request."""
        path = data['path'] if data['path'].startswith('/') else f"/{data['path']}"
        url = f"http://localhost:{self.port}{path}"

        async with aiohttp.ClientSession() as session:
            try:
                async with session.request(
                    method=data["method"],
                    url=url,
                    headers=data["headers"],
                    data=data.get("body", ""),
                    timeout=aiohttp.ClientTimeout(total=self.REQUEST_TIMEOUT),
                    proxy=self.proxy.get('http') if self.proxy else None
                ) as response:
                    return {
                        "type": "response",
                        "request_id": data["request_id"],
                        "status": response.status,
                        "headers": dict(response.headers),
                        "content": await response.text()
                    }
            except aiohttp.ClientError as e:
                logger.error(f"Proxy request failed: {str(e)}")
                return self._create_error_response(data["request_id"])

    def _create_error_response(self, request_id: str) -> dict:
        """Create an error response for failed requests."""
        return {
            "type": "response",
            "request_id": request_id,
            "status": 502,
            "headers": {},
            "content": f"Failed to reach local server on port {self.port}"
        }

    def __str__(self) -> str:
        """Return the public URL of the tunnel."""
        return self.public_url