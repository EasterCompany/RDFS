#! /usr/bin/python3
from os import system as s, getcwd as _cwd
from sys import argv as a, executable as E
cwd=_cwd()
print("\nWelcome to the Overlord Installer!\n")
n=input("Project Name: ")
s(f"rm {cwd}/ol_installer.py")
#s(f"git clone git@github.com:EasterCompany/Overlord.git {n}")
#s(f"cd {n}")
#s(f"{E} core.py install {cwd}/{n}")
# clear && echo "" && echo "Downloading installer..." && wget -q https://raw.githubusercontent.com/EasterCompany/RDFS/Prd/ol_installer.py && sudo chmod +x ./ol_installer.py && sudo ./ol_installer.py
