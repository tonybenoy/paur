import requests

def aor_search(name = None, desc = None, pkg = None, repo = None, arch = None, maintainer = None, packager = None, flagged=None):
    url = "https://www.archlinux.org/packages/search/json/"
    if name != None:
        querystring = {"name":name}
    elif desc != None:
        print(desc)
        querystring = {"desc":desc}
    elif pkg != None:
        if repo!=None:
            if repo not in ['Core', 'Extra', 'Testing', 'Multilib', 'Multilib-Testing', 'Community', 'Community-Testing']:
                raise Exception("Repository not available in Arch Linux!")
        if arch!=None:
            if arch not in ['any', 'i686', 'x86_64']:
                raise Exception("Architecture not available in Arch Linux!")
        if flagged!=None:
            if flagged not in ["Flagged", "Not+Flagged"]:
                raise Exception("Flagged parameter incorrect!")
        querystring = {"q":pkg,"repo":repo,"maintainer":maintainer,"arch":arch,"packager":packager}
    else:
            raise Exception("Not enough parameters to perform query!")
    response = requests.request("GET", url, params=querystring)
    return response.text

def package(repo ,arch,name):
    if repo not in ['Core', 'Extra', 'Testing', 'Multilib', 'Multilib-Testing', 'Community', 'Community-Testing']:
        raise Exception("Repository not available in Arch Linux! See available Repositories at https://wiki.archlinux.org/index.php/Official_repositories_web_interface#Repository")
    if arch not in ['any', 'i686', 'x86_64']:
        raise Exception("Architecture not available in Arch Linux!See available Architecture at https://wiki.archlinux.org/index.php/Official_repositories_web_interface#Architecture")
    url = "https://www.archlinux.org/packages"+"/"+repo+"/"+arch+"/"+name+"/json"
    response = requests.request("GET", url)
    return response.text

def packagefiles(repo ,arch,name):
    if repo not in ['Core', 'Extra', 'Testing', 'Multilib', 'Multilib-Testing', 'Community', 'Community-Testing']:
        raise Exception("Repository not available in Arch Linux!")
    if arch not in ['any', 'i686', 'x86_64']:
        raise Exception("Architecture not available in Arch Linux!")
    url = "https://www.archlinux.org/packages"+"/"+repo+"/"+arch+"/"+name+"/files/json"
    response = requests.request("GET", url)
    return response.text
