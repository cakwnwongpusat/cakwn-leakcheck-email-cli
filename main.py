import typer
from rich.console import Console
from cli.app import app

console = Console()

if __name__ == "__main__":
    console.rule("[bold red]CAKWN-LEAKCHECK-EMAIL-CLI[/bold red]")
    console.print(
        "[bold yellow]Email Breach Intelligence and Exposure Detection Framework[/bold yellow]\n",
        justify="center"
    )
    app()
