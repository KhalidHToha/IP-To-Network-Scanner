from rich.console import Console
from rich.panel import Panel

console = Console()


def show_banner():
    banner = Panel(
        "[bold cyan]IP-To Network Scanner[/bold cyan]\n"
        "[green]Version 3.0.0 Alpha[/green]",
        title="Welcome",
        border_style="blue",
    )

    console.print(banner)
