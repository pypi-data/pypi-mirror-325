from urllib.parse import urlparse
import os

def should_skip_proxy(url: str) -> bool:
    """Check if proxy should be skipped based on NO_PROXY environment variable."""
    no_proxy = os.getenv("NO_PROXY") or os.getenv("no_proxy")
    if not no_proxy:
        return False

    no_proxy_list = [np.strip().lower() for np in no_proxy.split(",") if np.strip()]
    hostname = urlparse(url).hostname.lower()

    return any(
        entry == "*" or hostname.endswith(entry)
        for entry in no_proxy_list
    )

def is_running_in_docker() -> bool:
    """Check if the application is running inside a Docker container."""
    try:
        return os.path.exists("/.dockerenv")
    except:
        return False