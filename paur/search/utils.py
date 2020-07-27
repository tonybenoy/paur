from typing import Dict
from aorlib.aorlib import find_in_aor
from aurlib.aurlib import find_in_aur


def find_package(pkg_name: str, aor: bool = True, aur: bool = True) -> Dict:
    pkg = {}
    if aor:
        pkg = find_in_aor(name=pkg_name)
    if not pkg and aur:
        pkg = find_in_aur(pkg=pkg_name)
    return pkg
