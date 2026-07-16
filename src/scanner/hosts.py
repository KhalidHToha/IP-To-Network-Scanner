import ipaddress


def generate_hosts(network: str) -> list[str]:
    """
    Generate all usable host IPs from a network.
    Example:
        192.168.1.0/24
            ↓
        192.168.1.1
        ...
        192.168.1.254
    """

    net = ipaddress.ip_network(network, strict=False)

    return [str(host) for host in net.hosts()]
