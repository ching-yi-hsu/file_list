from os import listdir
from os.path import isfile, isdir, join
import os


mypath = os.getcwd()

files = listdir(mypath)

for f in files:
    print(f)

