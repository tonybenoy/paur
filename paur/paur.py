from typing import Optional
import typer
from init.utils import create_default_config
from find import find
app = typer.Typer()


@app.command("init")
def init(sub_command: Optional[str] = typer.Argument(None)) -> None:
    clean = True if sub_command else False
    if create_default_config(clean=clean):
        typer.echo(f"Config successfully created!")

app.add_typer(find.app, name="find")


if __name__ == "__main__":
    app()
