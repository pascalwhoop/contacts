import platform

import typer
from rich.console import Console
from rich.table import Table

from contacts.config import settings

app = typer.Typer(
    help="Headless personal CRM for relationships, memory, and AI-assisted context.",
    no_args_is_help=True,
    rich_markup_mode="rich",
)
console = Console()


@app.command()
def doctor() -> None:
    """Show the current local runtime configuration."""
    table = Table(title="contacts")
    table.add_column("Key", style="cyan")
    table.add_column("Value", style="green")
    table.add_row("app_name", settings.app_name)
    table.add_row("environment", settings.environment)
    table.add_row("data_dir", str(settings.data_dir))
    table.add_row("default_model", settings.default_model)
    table.add_row("python", platform.python_version())
    console.print(table)


@app.command()
def init_data_dir() -> None:
    """Create the local data directory used by the CLI."""
    settings.data_dir.mkdir(parents=True, exist_ok=True)
    console.print(f"[bold green]Ready[/bold green] {settings.data_dir}")


def main() -> None:
    app()
