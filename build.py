import PyInstaller
import subprocess
import os

# example use of pyinstaller inside a Python script

pwd = os.getcwd()
subprocess.call(r"python3 -m PyInstaller --noconsole --name pysubnetter ."+pwd+"/src/main.py")

# subprocess.call(r"python -m PyInstaller --noconsole --name WorkLogger F:\KivyApps\WorkLogger\main.py", cwd=r"F:\KivyApps\WorkLogger_Dist")
