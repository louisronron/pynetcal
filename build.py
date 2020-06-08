import PyInstaller.__main__
import json
import os

# open the json build file build.json
buildJson = open("build.json", "r")
specs = json.load(buildJson)

# set build properties
name = specs["name"]
version = specs["version"]
buildtype = specs["type"]
main = specs["main"]

if(buildtype!="release"):
    version = version+"-"+buildtype

# recreate main path string platform-independently
main = os.path.join(os.getcwd(),main)

# run build sequence
PyInstaller.__main__.run([
    '--name=%s' % name, 
    '--onefile',
    main
])

