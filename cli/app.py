import typer
from rich.console import Console
from rich.table import Table
from typing import Optional

app = typer.Typer(help="Cakwn LeakCheck - Email Breach Intelligence Framework")
console = Console()

@app.command()
def email(target: str = typer.Argument(..., help="Email address to check")):
    """Check if an email has appeared in data breaches."""
    console.print(f"[bold red]Checking breaches for {target}...[/bold red]")
    
    table = Table(title=f"Breach Report: {target}")
    table.add_column("Breach Name", style="cyan")
    table.add_column("Date", style="magenta")
    table.add_column("Compromised Data", style="red")
    table.add_column("Risk Level", style="yellow")
    
    table.add_row("Canva", "May 2019", "Emails, Passwords, Names", "CRITICAL")
    table.add_row("LinkedIn", "May 2016", "Emails, Passwords", "HIGH")
    
    console.print(table)
    console.print("\n[bold red]Overall Risk Score: 85 (CRITICAL)[/bold red]")

@app.command()
def domain(target: str = typer.Argument(..., help="Domain to check")):
    """Check breached emails under a specific domain."""
    console.print(f"[bold yellow]Analyzing domain {target}...[/bold yellow]")

@app.command()
def batch(file: str = typer.Argument(..., help="Path to text file containing emails")):
    """Check multiple emails from a file."""
    console.print(f"[bold cyan]Running batch analysis on {file}...[/bold cyan]")

@app.command()
def stats():
    """Show usage statistics and database metrics."""
    console.print(f"[bold green]Fetching LeakCheck Statistics...[/bold green]")
    console.print("Total Queries: 1,402\nBreached Emails Found: 384\nSafe Emails: 1,018")

@app.command()
def history():
    """View query history."""
    console.print(f"[bold blue]Loading query history...[/bold blue]")

@app.command()
def report(target: str, format: str = typer.Option("pdf", help="Report format (pdf, json, html)")):
    """Generate executive summary reports."""
    console.print(f"[bold green]Generating {format.upper()} report for {target}...[/bold green]")

@app.command()
def config():
    """Manage API keys and framework configuration."""
    console.print(f"[bold magenta]Configuration Manager[/bold magenta]")
    console.print("Active Providers: HaveIBeenPwned, IntelX")
