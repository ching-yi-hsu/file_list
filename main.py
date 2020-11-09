from os import listdir
import os


mypath = os.getcwd()

files = listdir(mypath)

for f in files:
    print(f)

