from rich.console import Console
from rich.panel import Panel

from src.network.network import (
    get_default_gateway,
    get_local_ip,
    get_network,
)

from src.system.system import (
    get_hostname,
    get_os,
    get_python_version,
)


def main():
    console = Console()

    console.print(
        Panel.fit(
            "[bold cyan]IP-To Network Scanner[/bold cyan]\n"
            "[green]Version 3.0.0 Alpha[/green]",
            border_style="cyan",
        )
    )

    console.print(f"[bold]Local IP :[/bold] {get_local_ip()}")
    console.print(f"[bold]Gateway  :[/bold] {get_default_gateway()}")
    console.print(f"[bold]Network  :[/bold] {get_network()}")
    console.print(f"[bold]OS       :[/bold] {get_os()}")
    console.print(f"[bold]Python   :[/bold] {get_python_version()}")
    console.print(f"[bold]Hostname :[/bold] {get_hostname()}")


if __name__ == "__main__":
    main()