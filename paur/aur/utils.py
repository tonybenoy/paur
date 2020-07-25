from typing import Dict

import httpx

from constants import AUR_URL


def find_in_aur(pkg: str, qby: str = "name-desc") -> Dict:
    if qby not in [
        "name",
        "name-desc",
        "maintainer",
        "depends",
        "makedepends",
        "optdepends",
        "checkdepends",
    ]:
        raise Exception(
            "Unsupported keyword. See supported keywords at https://wiki.archlinux.org/index.php/Aurweb_RPC_interface#search "
        )
    querystring = {"v": "5", "type": "search", "by": qby, "arg": pkg}
    response = httpx.request(method="GET", url=AUR_URL, params=querystring)
    return response.json()


def aur_info(*args) -> Dict:
    querystring = {"v": "5", "type": "info", "arg[]": args}
    response = httpx.request(method="GET", url=AUR_URL, params=querystring)
    return response.json()
