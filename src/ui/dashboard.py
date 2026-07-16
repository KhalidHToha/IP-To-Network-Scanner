from rich.console import Console
from rich.table import Table

console = Console()


def show_dashboard(info: dict):
    table = Table(title="IP-To Network Scanner v3", show_header=False)

    table.add_column("Key", style="cyan", width=15)
    table.add_column("Value", style="green")

    for key, value in info.items():
        table.add_row(key, str(value))

    console.print(table)
