import os
import platform


def is_tool(name):
    return distutils.spawn.find_executable(name) is not None


if platform.system() == "Windows":
    raise OSError("Don't run on Windows!")


run_folder = os.getcwd()
home = os.path.expanduser('~')
# get extra imports
try:
    os.chdir(home + "/.configbuilt")
except:
    raise OSError("Config directory does not exist")

import angledat
os.chdir(run_folder)
if os.path.exists("build.andat"):
    data = angledat.read_dict("build.andat")
else:
    raise OSError("Build data does not exist")

if not istool("wget"):
    raise OSError("wget not installed")
try:
    script = data["script to run"]
except:
    raise OSError("No script to run given")

if not os.path.exists("downloads"):
    os.system("touch downloads")
os.chdir("downloads")
for name, value in data:
    if name == "script to run":
        continue
    else:
        if not os.path.exists(name):
            os.system("mkdir" + name)
        else:
            raise OSError("Package '" + name + "' has already been downloaded")
        try:
            response = requests.get(value)
            os.system("wget " + value)
            os.system("mv " + value.split("/")[-1] + " '" + name + "/" + value + "'")
        except requests.ConnectionError as exception:
            print("Warning: Package '" + "' does not exist!")
            os.remdir(name)
    os.system(script)
