from typing import Dict

import typer

from aorlib.aorlib import find_in_aor
from aurlib.aurlib import find_in_aur


def main(packages: str):
    packages_list = packages.split()
    for pkg in packages_list:
        package = find_package(pkg_name=pkg)
        if not package:
            typer.echo(f"Package {pkg} not found!")


def find_package(pkg_name: str) -> Dict:
    pkg = find_in_aor(name=pkg_name)
    if not pkg:
        pkg = find_in_aur(pkg=pkg_name)
    return pkg


if __name__ == "__main__":
    typer.run(main)
