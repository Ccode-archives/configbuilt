import os
import platform


if platform.system() == "Windows":
    raise OSError("Don't run on Windows!")


run_folder = os.getcwd()
# get extra imports
try:
    os.chdir("~/.configbuilt")
except:
    raise OSError("Config directory does not exist")

import angledat
os.chdir(run_folder)
if os.path.exists("build.andat"):
    data = angledat.read_dict("build.andat")
else:
    raise OSError("Build data does not exist")
