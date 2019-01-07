import requests

def aur_search(pkg,qby="name-desc"):
    url = "https://aur.archlinux.org/rpc.php/rpc/"
    print(pkg,qby)
    if qby not in ["name","name-desc","maintainer","depends","makedepends","optdepends","checkdepends"]:
        raise Exception("Unsupported keyword. See supported keywords at https://wiki.archlinux.org/index.php/Aurweb_RPC_interface#search ")
    querystring = {"v":"5","type":"search","by":qby,"arg":pkg}
    response = requests.request("GET", url, params=querystring)
    return response.text

def aur_info(*args):
    url = "https://aur.archlinux.org/rpc.php/rpc/"
    querystring = {"v":"5","type":"info","arg[]":args}
    response = requests.request("GET", url, params=querystring)
    return response.text

#print(aur_search("cower"))
#print(aur_info("cower","teamviewer"))