from typing import Dict

import typer


def main(packages: str):
    packages_list = packages.split()
    for pkg in packages_list:
        package = find_package(pkg_name=pkg)
        if not package:
            typer.echo(f"Package {pkg} not found!")


def find_package(pkg_name: str) -> Dict:
    pkg = find_pkg_in_aor(pkg_name=pkg_name)
    if not pkg:
        pkg = find_pkg_in_aur(pkg_name=pkg_name)
    return pkg


def find_pkg_in_aor(pkg_name: str) -> Dict:
    return {}


def find_pkg_in_aur(pkg_name: str) -> Dict:
    return {}


if __name__ == "__main__":
    typer.run(main)
