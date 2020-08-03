import typer

from find.utils import find_package

from paur.paur import console

findcmd = typer.Typer()


@findcmd.command("find")
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
            console.print("Package ", pkg, "not", "found!", style="bold red")
