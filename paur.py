# -*- coding: utf-8 -*-
import json
import urllib.parse
import urllib.request
import subprocess
import os
import re
import argparse

class backend:
    passwrd = ""

#AUR search function
    def aur_search(self, args):
        target_url = "http://aur.archlinux.org/rpc.php"
        params = urllib.parse.urlencode({'type': 'search', 'arg': args})
        response = urllib.request.urlopen("%s?%s" % (target_url, params)).read()
        data = json.loads(response)
        aurpkglist = []
        if not isinstance(data['results'], list):
            data['results'] = [data['results'], ]
        for pkg in data['results']:
            l = []
            for name in pkg:
                l.append(pkg[name])
            aurpkglist.append(l)
        return aurpkglist

#Downdloads AUR package , Builds it and installs it 
    def makepkg(self, name):
        cmd = "git clone https://aur.archlinux.org/" + name + ".git"
        subprocess.call(str.split(str(cmd)))
        os.chdir(name)
        os.popen("sudo -k")
        cmd = "makepkg -src --noconfirm"
        subprocess.call(str.split(str(cmd)))
        files = os.listdir('.')
        files_txt = [i for i in files if i.endswith('.pkg.tar.xz')]
        subprocess.call(str.split(str(cmd)))
        cmd = " pacman -U " + files_txt[0] + " --noconfirm"
        os.popen("sudo -S %s" % (cmd), 'w').write(self.passwrd + '\n')
        os.popen("sudo -k")
        os.chdir("path")

#Installs the package from official repository
    def pacinstall(self, name):
        cmd = " pacman -S " + name + " --noconfirm"
        os.popen("sudo -S %s" % (cmd), 'w').write(self.passwrd + '\n')
        os.popen("sudo -k")

#Uninstalls the package from the system
    def uninstall(self, name):
        cmd = " pacman -R " + name + " --noconfirm"
        os.popen("sudo -S %s" % (cmd), 'w').write(self.passwrd + '\n')
        os.popen("sudo -k")

#Searches for the package in Official Repository
    def pacsearch(self, name):
        paclist = []
        cmd = "pacman -Ss " + name
        try:
           data = subprocess.check_output(str.split(str(cmd)))
        except:
            data = ""
        pkglist = data.splitlines()
        n = 0
        fin = []
        size = len(pkglist)
        while n != size:
            if n % 2 != 0:
                fin.append(pkglist[n])
            else:
                t = re.split('/', pkglist[n].decode('utf-8'))
                fin.append(t[0])
                s = t[1].split()
                fin.append(s[0])
                fin.append(s[1])
            n = n + 1
        size = len(fin)
        i = int(size / 4)
        nn = 0
        for k in range(0, i):
            l = [fin[nn], fin[nn + 1], fin[nn + 2], fin[nn + 3]]
            paclist.append(l)
            nn += 4
        return paclist

#Updates the system by running Pacman
    def pac_update(self):
        os.popen("sudo -S %s" % ("pacman -Syyu --noconfirm "),
                 'w').write(self.passwrd + '\n')

#Creates a database of all installed applications 
    def installed_db(self):
        cmd = "pacman -Q"
        data = subprocess.check_output(str.split(str(cmd)))
        pkglist = data.splitlines()
        cmd = "pacman -Qqm"
        data = subprocess.check_output(str.split(str(cmd)))
        aurlist = data.splitlines()
        n = 0
        installedlist = []
        size = len(pkglist)
        while n != size:
            l = pkglist[n].split()
            if l[0] in aurlist:
                l.append("Yes")
            else:
                l.append("NO")
            installedlist.append(l)
            n = n + 1
        return installedlist

#Performs and AUR Update
    def aur_update(self):
        conn = sqlite3.connect('installed_db.db')
        c = conn.cursor()
        c.execute(
            'CREATE TABLE IF NOT EXISTS installed(name TEXT, version TEXT, aur TEXT)')
        c.execute('''SELECT name ,version from installed where aur="Yes"''')
        data1 = c.fetchall()
        target_url = "http://aur.archlinux.org/rpc.php"
        size = len(data1)
        conn1 = sqlite3.connect('aurup.db')
        c1 = conn1.cursor()
        c1.execute(''' drop table if exists searchdata''')
        c1.execute('''CREATE TABLE searchdata(FirstSubmitted text, Maintainer text, Description text,License text, URL text,LastModified text,PackageBaseID text,CategoryID text,Version text,URLPath text,OutOfDate text,NumVotes text,PackageBase text,ID text,Name text )''')
        for i in range(0, size):
            params = urllib.urlencode({'type': 'search', 'arg': data1[i][0]})
            response = urllib.urlopen("%s?%s" % (target_url, params)).read()
            data = json.loads(response)
            if not isinstance(data['results'], list):
                data['results'] = [data['results'], ]
            for pkg in data['results']:
                l = []
                for name in pkg:
                   l.append(pkg[name])
                c1.execute('''INSERT INTO searchdata(FirstSubmitted , Maintainer , Description ,License , URL ,LastModified ,PackageBaseID ,CategoryID ,Version ,URLPath ,OutOfDate ,NumVotes ,PackageBase ,ID,Name ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', l)

        c1.execute('''SELECT name,version from searchdata''')
        data2 = c1.fetchall()
        s = len(data2)
        for i in range(0, size):
            for j in range(0, s):
                if data1[i][0] == data2[j][0]:
                    if data1[i][1] != data2[j][1]:
                        self.makepkg(data1[i][0])
        conn.commit()
        conn.close()
        conn1.commit()
        conn1.close()


if __name__ == '__main__':
    tpc = backend()
    parser = argparse.ArgumentParser(description='AUR Helper for Arch Linux.')
    parser.add_argument('-Ss', help='Search Official Repository')
    parser.add_argument('-As', help='Search AUR')
    parser.add_argument('-s', help='Search both AUR and Official Repository')
    parser.add_argument('-R', help='Uninstall Package')
    parser.add_argument('-S', help='Install Package')
    parser.add_argument('-Syu', help='Update System')
    parser.add_argument('-Sa', help='Update AUR')
    parser.add_argument('-Sya', help='Update AUR and System')

    args = parser.parse_args()
    if args.S:
        tpc.pacinstall(args.S)
    if args.R:
        tpc. uninstall(args.R)
    if args.Ss:
        k = tpc.pacsearch(args.Ss)
        if len(k) == 0:
            print("Package " + args.Ss + " not found in official repositories")
        else:
            count = 0
            for item in k:
                count += 1
                print(str(count) + ")" + item[0] +"/ "+
                    item[1] + " " + item[2] + "\n" + item[3].decode('utf-8'))
    if args.As:
        k = tpc.aur_search(args.s)
        if len(k) == 0:
            print("Package " + args.As + " not found in AUR")
        else:
            count = 0
            for item in k:
                count += 1
                print(str(count) + ")" + "AUR " + "/ " +
                    item[1] + " " + item[4] + "\n" + "    " + item[5])
    if args.s:
        k = tpc.pacsearch(args.s)
        count = 0
        if len(k) == 0:
            print("Package " + args.ss + " not found in official repositories")
        else:
            for item in k:
                count += 1
                print(str(count) + ")" + item[0] + "/ " +
                      item[1] + " " + item[2] + "\n" + item[3].decode('utf-8'))
        k1 = tpc.aur_search(args.s)
        if len(k1) == 0:
            print("Package " + args.s + " not found in AUR")
        else:
            for item in k1:
                count += 1
                print(str(count) + ")" + "AUR " + "/ " +
                      item[1] + " " + item[4] + "\n" + "    " + item[5])
