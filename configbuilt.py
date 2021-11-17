import os
import platform
import distutils.spawn
import requests


def is_tool(name):
    return distutils.spawn.find_executable(name) is not None


if platform.system() == "Windows":
    raise OSError("Don't run on Windows!")


run_folder = os.getcwd()
home = os.path.expanduser('~')
# get extra imports

if not os.path.exists(home + "/.configbuilt"):
    raise OSError("Config directory does not exist!")



import angledat
os.system("rm angledat.py")
os.chdir(run_folder)
if os.path.exists("build.andat"):
    data = angledat.read_dict("build.andat")
else:
    raise OSError("Build data does not exist")

if not is_tool("wget"):
    raise OSError("wget not installed")
try:
    script = data["script to run"]
except:
    raise OSError("No script to run given")

if not os.path.exists("downloads"):
    os.system("mkdir downloads")
os.chdir("downloads")
for name in data:
    if name == "script to run":
        continue
    else:
        if not os.path.exists(name):
            os.system("mkdir " + name)
        else:
            raise OSError("Package '" + name + "' has already been downloaded")
        try:
            response = requests.get(data[name])
            os.system("wget " + data[name])
            os.system("mv " + data[name].split("/")[-1] + " '" + name + "/" + data[name].split("/")[-1] + "'")
        except requests.ConnectionError as exception:
            print("Warning: Package '" + "' does not exist!")
            os.remdir(name)
    os.system(script)
