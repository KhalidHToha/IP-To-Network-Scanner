from src.network.network import (
    get_local_ip,
    get_default_gateway,
    get_network,
)

from src.system.system import (
    get_hostname,
    get_os,
    get_python_version,
)

from src.ui.dashboard import show_dashboard


class ScannerApp:
    def run(self):
        info = {
            "Local IP": get_local_ip(),
            "Gateway": get_default_gateway(),
            "Network": get_network(),
            "OS": get_os(),
            "Python": get_python_version(),
            "Hostname": get_hostname(),
        }

        show_dashboard(info)
