from typing import Dict

import httpx


def find_in_aor(
    name: str = None,
    desc: str = None,
    pkg: str = None,
    repo: str = None,
    arch: str = None,
    maintainer: str = None,
    packager: str = None,
    flagged: str = None,
) -> Dict:
    url = "https://www.archlinux.org/packages/search/json/"
    if name != None:
        querystring = {"name": name}
    elif desc != None:
        querystring = {"desc": desc}
    elif pkg != None:
        if repo != None:
            if repo not in [
                "Core",
                "Extra",
                "Testing",
                "Multilib",
                "Multilib-Testing",
                "Community",
                "Community-Testing",
            ]:
                raise Exception("Repository not available in Arch Linux!")
        if arch != None:
            if arch not in ["any", "i686", "x86_64"]:
                raise Exception("Architecture not available in Arch Linux!")
        if flagged != None:
            if flagged not in ["Flagged", "Not+Flagged"]:
                raise Exception("Flagged parameter incorrect!")
        querystring = {
            "q": pkg,
            "repo": repo,
            "maintainer": maintainer,
            "arch": arch,
            "packager": packager,
        }
    else:
        raise Exception("Not enough parameters to perform query!")
    response = httpx.request(method="GET", url=url, params=querystring)
    return response.json()


def package(repo: str, arch: str, name: str) -> Dict:
    if repo not in [
        "Core",
        "Extra",
        "Testing",
        "Multilib",
        "Multilib-Testing",
        "Community",
        "Community-Testing",
    ]:
        raise Exception(
            "Repository not available in Arch Linux! See available Repositories at https://wiki.archlinux.org/index.php/Official_repositories_web_interface#Repository"
        )
    if arch not in ["any", "i686", "x86_64"]:
        raise Exception(
            "Architecture not available in Arch Linux!See available Architecture at https://wiki.archlinux.org/index.php/Official_repositories_web_interface#Architecture"
        )
    url = f"https://www.archlinux.org/packages/{repo}/{arch}/{name}/json"
    response = httpx.request(method="GET", url=url)
    return response.json()


def packagefiles(repo: str, arch: str, name: str) -> Dict:
    if repo not in [
        "Core",
        "Extra",
        "Testing",
        "Multilib",
        "Multilib-Testing",
        "Community",
        "Community-Testing",
    ]:
        raise Exception("Repository not available in Arch Linux!")
    if arch not in ["any", "i686", "x86_64"]:
        raise Exception("Architecture not available in Arch Linux!")
    url = f"https://www.archlinux.org/packages/{repo}/{arch}/{name}/files/json"
    response = httpx.request("GET", url)
    return response.json()
