from typing import Optional

import typer
from rich.console import Console

from find import find
from init.utils import create_default_config

app = typer.Typer()
console = Console()


@app.command("init")
def init(sub_command: Optional[str] = typer.Argument(None)) -> None:
    clean = True if sub_command else False
    if create_default_config(clean=clean):
        console.print("Config", "successfully ", "created!", style="bold green")


app.add_typer(find.app, name="find")


if __name__ == "__main__":
    app()
