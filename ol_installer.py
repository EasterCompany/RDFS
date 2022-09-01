#! /usr/bin/python3
from os import system as s, getcwd as _cwd
from sys import argv as a, executable as E
cwd=_cwd()
print(cwd)
n=input("")
s(f"rm {cwd}/ol_installer.py")
#s(f"git clone git@github.com:EasterCompany/Overlord.git {n}")
#s(f"cd {n}")
#s(f"{E} core.py install {cwd}/{n}")
# clear && echo "" && echo "Downloading installer..." && wget -q https://www.pythonanywhere.com/user/OwenEaster/files/home/OwenEaster/ol_installer.py && sudo chmod +x ./ol_installer.py && sudo ./ol_installer.py
