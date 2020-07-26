from typing import Dict, Optional

import typer
from aorlib.aorlib import find_in_aor
from aurlib.aurlib import find_in_aur

from init.utils import create_default_config

app = typer.Typer()


@app.command()
def main(packages: str)->None:
    packages_list = packages.split()
    for pkg in packages_list:
        package = find_package(pkg_name=pkg)
        if not package:
            typer.echo(f"Package {pkg} not found!")


@app.command("init")
def init(sub_command: Optional[str] = typer.Argument(None))->None:
    clean = True if sub_command else False
    if create_default_config(clean=clean):
        typer.echo(f"Config successfully created!")


def find_package(pkg_name: str) -> Dict:
    pkg = find_in_aor(name=pkg_name)
    if not pkg:
        pkg = find_in_aur(pkg=pkg_name)
    return pkg


if __name__ == "__main__":
    app()
