import typer

app = typer.Typer()
from search.utils import find_package


@app.command("find")
def find(
    packages: str,
    in_aur: bool = typer.Option(False, help="Search only in AUR."),
    in_repo: bool = typer.Option(False, help="Search only in official repo."),

) -> None:
    if not (in_repo and in_aur):
        in_aur, in_repo = True, True
    packages_list = packages.split()
    for pkg in packages_list:
        package = find_package(pkg_name=pkg, aor=in_repo, aur=in_aur)
        if not package:
            typer.echo(f"Package {pkg} not found!")
