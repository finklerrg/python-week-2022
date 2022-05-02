import typer


main = typer.Typer(help="Beer Management Application")


@main.command("add")
def add(name: str, style: str):
    """Adds a new beer to the database."""
    print(f"Adding {name} {style}")


@main.command("list")
def list_beers(style: str):
    """Lists all beers of a given style."""
    print(f"Listing {style}")
