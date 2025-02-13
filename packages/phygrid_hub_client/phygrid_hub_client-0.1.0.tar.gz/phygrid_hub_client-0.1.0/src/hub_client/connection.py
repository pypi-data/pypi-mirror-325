from typing import Dict, List, Optional
import socketio
from .utils import should_skip_proxy, is_running_in_docker

class UrlConfig:
    def __init__(self, url: str, timeout: int = 5000, options: Optional[Dict] = None):
        self.url = url
        self.timeout = timeout
        self.options = options or {}

class PhyHubConnection:
    _instance = None
    
    def __init__(self, data_residency: Optional[str] = None):
        self.phygrid_socket_singleton = None
        
        # Determine local IP based on environment
        local_ip = "172.26.128.1" if is_running_in_docker() else "127.0.0.1"
        
        self.socket_urls = [
            UrlConfig(f"http://{local_ip}:55000", 5000)
        ]
        
        # Add additional URLs if not running in server-side context
        try:
            import sys
            if 'win' in sys.platform or 'darwin' in sys.platform:  # Client-side check
                self.socket_urls.append(UrlConfig("https://phyos:55500", 5000))
                if data_residency:
                    self.socket_urls.append(
                        UrlConfig(
                            f"https://phyhub.{data_residency.lower()}.omborigrid.net:443",
                            10000
                        )
                    )
        except ImportError:
            pass

    @classmethod
    def get_instance(cls, data_residency: Optional[str] = None) -> 'PhyHubConnection':
        if not cls._instance:
            cls._instance = PhyHubConnection(data_residency)
        return cls._instance

    def get_socket_io_with_proxy(self, url: str, options: Dict = None) -> socketio.Client:
        options = options or {}
        
        if should_skip_proxy(url):
            return socketio.Client(**options)
            
        proxy = (
            os.getenv("HTTPS_PROXY")
            or os.getenv("https_proxy")
            or os.getenv("HTTP_PROXY")
            or os.getenv("http_proxy")
        )
        
        if not proxy:
            return socketio.Client(**options)
            
        try:
            options["http_proxy"] = proxy
            options["https_proxy"] = proxy
            return socketio.Client(**options)
        except Exception as e:
            print(f"Invalid proxy URL: {proxy}. Creating Socket.IO instance without proxy.")
            return socketio.Client(**options)

    async def get_socket_io_instance(self) -> socketio.Client:
        for url_config in self.socket_urls:
            try:
                socket = self.get_socket_io_with_proxy(
                    url_config.url,
                    {
                        **url_config.options,
                        "reconnection_attempts": 0,
                        "timeout": url_config.timeout,
                    }
                )
                return socket
            except Exception as e:
                print(f"Failed to connect to {url_config.url}. Trying next option...")
                continue
        raise Exception("Failed to connect to any socket.io server")