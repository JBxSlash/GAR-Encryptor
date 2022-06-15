### Using JBxSlash's Github File Bootstrapper! ###
### Modified Version 1.0.2 ###

import os
from pathlib import Path
import requests
import random
import time


for pop in range(11):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[" + "-" * pop + " " * (10-pop) + "] Getting Files From Github...")
    time.sleep(random.randint(1,10)/10)
#Gets the link of main.py and loads it#
GIT_REPO_MAIN_PY = "https://raw.githubusercontent.com/JBxSlash/GAR-Encryptor/main/GAR/main.py"

resp = requests.get(GIT_REPO_MAIN_PY)
time.sleep(1)
print("[+] Making File.py")

REPO_DATA = random.randint(100000,999999)
folder = ""
path = ""
if Path("Documents\TEST_TEXT_GAR"):
    folder = open("Documents\TEST_TEXT_GAR\\" + str(REPO_DATA) + ".py", "a")
    path = "Documents\TEST_TEXT_GAR\\" + str(REPO_DATA) + ".py"
else:
    folder = open("Documents\\" + str(REPO_DATA) + ".py", "a")
    path = "Documents\\" + str(REPO_DATA) + ".py"

for pop in range(11):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[----------] Getting Files From Github...")
    print("[+] Making File.py")
    print("[" + "-" * pop + " " * (10-pop) + "] Writing Data...")
    time.sleep(random.randint(1,10)/10)
with open(path, "w") as file:
    file.write(resp.text)
os.system('cls' if os.name == 'nt' else 'clear')
print("Finished: Loading file; Thanks for using JBxSlash's Github > File booststrapper!")
os.system(path)


