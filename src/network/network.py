import socket
import netifaces


def get_local_ip() -> str:
    """
    Returns the local IPv4 address.
    """

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.connect(("8.8.8.8", 80))
            return sock.getsockname()[0]

    except OSError:
        return "127.0.0.1"

def get_default_gateway() -> str:
    """
    Returns the default gateway IPv4 address.
    """

    gateways = netifaces.gateways()

    default = gateways.get("default")

    if default and netifaces.AF_INET in default:
        return default[netifaces.AF_INET][0]

    return "Unknown"
