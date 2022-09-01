#! /usr/bin/python3
from os import system as s, getcwd as _cwd
from sys import argv as a, executable as E
try:
  cwd=_cwd()
  s("clear")
  print("\nWelcome to the Overlord Installer!\n")
  n=input("Project Name: ")
  print(f"\ncreating project: {n}...")
except: pass
s(f"sudo rm {__file__}")
#s(f"git clone git@github.com:EasterCompany/Overlord.git {n}")
#s(f"cd {n}")
#s(f"{E} core.py install {cwd}/{n}")
# clear && echo "" && echo "Downloading installer..." && wget -q https://raw.githubusercontent.com/EasterCompany/RDFS/Prd/Overlord/version/1.2.0/create_new_overlord_project.py && sudo chmod +x ./create_new_overlord_project.py && sudo ./create_new_overlord_project.py
