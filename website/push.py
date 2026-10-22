#!/bin/python3

from sys import argv
from os import system

try:
    msg = argv[1]
except:
    msg = "Autumatic commit message"


system('git add --all')

system(f'git commit -m "{msg}"')

system('git push')

