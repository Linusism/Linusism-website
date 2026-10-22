#!/bin/python3

from sys import argv
from os import system

try:
    msg = argv[1]
    push = argv[2]
except:
    msg = "Autumatic commit message"
    push = "1"


system('git add --all')

system(f'git commit -m "{msg}"')

if push == "1":
    system('git push')
