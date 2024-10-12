import os
import sys
import shutil
from time import sleep


JAUNE = "\033[33m"
ROUGE = "\033[31m"
VERT = "\033[32m"
VIOLET = "\033[35m"  
RESET = "\033[0m"   

dependencies = ["requests"]

def check_dependencies_requests():
    missing_dependencies = []
    for dependency in dependencies:
        try:
            __import__(dependency)
            sleep(1)
        except ImportError:
            missing_dependencies.append(dependency)
    
    if missing_dependencies:
        for dependency in missing_dependencies:
            sleep(1)
        return False
    return True

sleep(1.5)


if not check_dependencies_requests():
    for dependency in dependencies:
        print(f"Installing {dependency}...")
        sleep(1)
        os.system(f"pip install {dependency}")
        sleep(2)