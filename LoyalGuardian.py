# Loyal Guardian Source Code by Lucas Yichen Jiao
# (c) 2023 OuterSpiral studios. All rights reserved. 

import os
from pathlib import Path
import shutil

usr = Path.home()
print("Welcome to Loyal Guardian! Your trusty friend and greatest enemy to GoGuardian!")
print("I heard that the school reinplemented GoGuardian on Freshman and Sophormone MacBooks and disabled other browsers so you HAVE TO USE IT!. What a burden!")
print("Lucky for you though, I know how to help!")
print("Just press 'y' and hit enter. I will restart your browser and everything should be working!")

cmd = input("Begin operation by typing in y: ")
if cmd == "y":
    os.system("clear")
    os.chdir("/Applications")
    os.system("killall Google\ Chrome")
    for target in os.listdir(f"{usr}/Library/Application Support/Google/Chrome"):
        if "Profile" in target:
            if target[0:7] == "Profile": # avoids tampering with system profile
                for file in os.listdir(f"{usr}/Library/Application Support/Google/Chrome/{target}/Extensions"):
                    if file != ".DS_Store":
                        shutil.rmtree(f"{usr}/Library/Application Support/Google/Chrome/{target}/Extensions/{file}")
    
    print("Its done! Enjoy Chrome to its fullest!")
    os.system("open Google\ Chrome.app")

elif cmd == "n":
    print("Hmmm... This student has an interesting thought process...")

else:
    print("...")
