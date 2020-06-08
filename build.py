import PyInstaller
import subprocess
import json
import os

# open the json build file build.json
buildJson = open("build.json", "r")
specs = json.load(buildJson)

# set build properties
name = specs["name"]
version = specs["version"]
buildtype = specs["type"]
python_ver = specs["python_version"]
main = specs["main"]

if(buildtype!="release"):
    version = version+"-"+buildtype

# recreate main path string platform-independently
main = os.path.join(os.getcwd(),main)

# run build sequence
os.system(
    python_ver\
    +" -m PyInstaller --onefile "\
    +main+" --name "\
    +name\
    +"-"\
    +version\
    +" --clean")


