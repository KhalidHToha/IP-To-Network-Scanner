import platform
import subprocess


def ping_host(ip: str) -> bool:
    """
    Returns True if the host responds to ping.
    """

    system = platform.system().lower()

    if system == "windows":
        command = ["ping", "-n", "1", "-w", "1000", ip]
    else:
        command = ["ping", "-c", "1", "-W", "1", ip]

    result = subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    return result.returncode == 0
