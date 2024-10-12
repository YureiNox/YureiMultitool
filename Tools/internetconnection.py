import os, sys, shutil
from time import sleep

JAUNE = "\033[33m"
ROUGE = "\033[31m"
VERT = "\033[32m"
VIOLET = "\033[35m"  
RESET = "\033[0m" 

def check_internet():
    try:
        with open(os.devnull, 'w') as devnull:
            result = os.system("ping -n 1 google.com > NUL 2>&1")
        return result == 0
    except:
        return False
    
if not check_internet():
    print(f"{ROUGE}No internet connection detected.{RESET}")
    sys.exit(1)
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    sleep(0.5)
    print(f"{VERT}Internet connection Found !{RESET}")
    sleep(0.5)
    print("Please wait...")

if __name__ == "__main__":
    check_internet()