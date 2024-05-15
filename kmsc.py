import os
import subprocess
import platform
import sys

# Pass script.py as argument
script_name = sys.argv[0]

# Check if windows
def is_platform_windows():
    return platform.system() == "Windows"

# Check if *nix
def is_platform_linux_or_unix():
    system = platform.system()
    return system == "Linux" or system == "Darwin" 

# Check if *nix and if yes install pip
if is_platform_linux_or_unix():
    try:
        subprocess.check_output("dpkg --version", shell=True)
        subprocess.run("sudo dpkg -l | grep -qw python3-pip || sudo apt install python3-pip -y", shell=True)
    except subprocess.CalledProcessError:
        subprocess.run("python3 -m ensurepip --upgrade", shell=True)

# Check if windows and if yes install pip
if is_platform_windows():
    subprocess.run("py -m ensurepip --upgrade", shell=True)

# Check if *nix and if yes install the requirements and run the python script
if is_platform_linux_or_unix():
    if os.path.exists("./env"):
        print("Venv found! Using it")
    else:
        print("Creating a virtual environment & Installing Python packages...")
        subprocess.run("python3 -m venv env", shell=True)
        if os.path.exists("requirements.txt"):
            subprocess.run("./env/bin/pip3 install -r requirements.txt", shell=True)
        else:
            print("Error: no requirements.txt found. Exiting.")
            exit()

    subprocess.run(["./env/bin/python3"] + sys.argv[1:])  

# If windows, install the requirements and run the python script
else:
    if is_platform_windows():
        if os.path.exists(".\\env"):
            print("Venv found! Using it")
        else:
            print("Creating a virtual environment & Installing Python packages...")
            subprocess.run("py -m venv env", shell=True)
            if os.path.exists("requirements.txt"):
                subprocess.run(".\\env\\Scripts\\pip3.exe install -r requirements.txt", shell=True)
            else:
                print("Error: no requirements.txt found. Exiting.")
                exit()

        subprocess.run([".\\env\\Scripts\\python.exe"] + sys.argv[1:])  