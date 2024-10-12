# Pre-Installed Libraries
import os
import sys
import shutil
from time import sleep
from Tools.internetconnection import check_internet
from Tools.depedeciesChecker.requestsdep import check_dependencies_requests as check_requests
from Tools.depedeciesChecker.pyperclipdep import check_dependencies_pyperclip as check_pyperclip
os.system('cls' if os.name == 'nt' else 'clear')
# ANSI Escape Sequences

JAUNE = "\033[33m"
ROUGE = "\033[31m"
VERT = "\033[32m"
VIOLET = "\033[35m"  
RESET = "\033[0m"   

# Check Internet Connection + Dependencies

if not check_internet():
    print(f"{ROUGE}No internet connection detected.{RESET}")
    sleep(1)
    exit(1)
else:
    sleep(1)
    check_pyperclip()
    print(f"{VERT}Pyperclip Found !{RESET}")
    sleep(0.5)
    check_requests()
    print(f"{VERT}Requests Found !{RESET}")
    sleep(0.5)

# imported libraries after checking dependencies

import requests
import pyperclip
sleep(1)
# ASCII Art Pannel

ascii_art = r""" 
  ___    ___ ___  ___  ________  _______   ___  _________  ________  ________  ___       ________      
 |\  \  /  /|\  \|\  \|\   __  \|\  ___ \ |\  \|\___   ___\\   __  \|\   __  \|\  \     |\   ____\     
 \ \  \/  / | \  \\\  \ \  \|\  \ \   __/|\ \  \|___ \  \_\ \  \|\  \ \  \|\  \ \  \    \ \  \___|_    
  \ \    / / \ \  \\\  \ \   _  _\ \  \_|/_\ \  \   \ \  \ \ \  \\\  \ \  \\\  \ \  \    \ \_____  \   
   \/  /  /   \ \  \\\  \ \  \\  \\ \  \_|\ \ \  \   \ \  \ \ \  \\\  \ \  \\\  \ \  \____\|____|\  \  
 __/  / /      \ \_______\ \__\\ _\\ \_______\ \__\   \ \__\ \ \_______\ \_______\ \_______\____\_\  \ 
|\___/ /        \|_______|\|__|\|__|\|_______|\|__|    \|__|  \|_______|\|_______|\|_______|\_________\
\|___|/                                                                                    \|_________| 
by YureiNox --> https://github.com/yureinox"""

def DownloadFile(url, filename):
    try:
        response = requests.get(url, stream=True)
        with open(filename, 'wb') as file:
            shutil.copyfileobj(response.raw, file)
        return True

    except Exception as e:
        return False

# Main Function
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(VIOLET + ascii_art + RESET)
    if not check_internet():
        print(f'{RESET}Internet connection status: {ROUGE}Not Connected!{RESET}')
    else:
        print(f'{RESET}Internet connection status: {VERT}Connected !{RESET}')
    
    print(f"""
    {ROUGE}[ATTENTION] Sometimes windows defender can block the installation of the tools...{RESET}
    [1] Wireshark Windows x64 V4.4.1
    [2] Nmap
    [3] Metasploit
    [4] Exit   
    """)
    choice = input("Enter your choice: ")

    if choice == "1":
        url = 'https://2.na.dl.wireshark.org/win64/Wireshark-4.4.1-x64.exe'
        filename = 'Wireshark-4.4.1-x64.exe'
        DownloadFile(url, filename)
        if not DownloadFile:
            print(f"{ROUGE}Error: Download Failed !{RESET}")
            sleep(1)
            main()
        else:
            print(f"{JAUNE}Wireshark Downloaded !{RESET}")
            sleep(1)
            os.system(filename)
            input("Press Enter when installation is done...")
            os.system(f"del {filename}")
            main()

    elif choice == "2":
        url = 'https://nmap.org/dist/nmap-7.95-setup.exe'
        filename = 'nmap-7.95-setup.exe'
        DownloadFile(url, filename)
        if not DownloadFile:
            print(f"{ROUGE}Error: Download Failed !{RESET}")
            sleep(1)
            main()
        else:
            print(f"{JAUNE}Nmap Downloaded !{RESET}")
            sleep(1)
            os.system(filename)
            input("Press Enter when installation is done...")
            os.system(f"del {filename}")
            main()

    elif choice == "3":
        url = 'https://windows.metasploit.com/metasploit-latest-windows-installer.exe'
        filename = 'metasploit-latest-windows-installer.exe'
        DownloadFile(url, filename)
        if not DownloadFile:
            print(f"{ROUGE}Error: Download Failed !{RESET}")
            sleep(1)
            main()
        else:
            print(f"{JAUNE}Metasploit Downloaded !{RESET}")
            sleep(1)
            os.system(filename)
            input("Press Enter when installation is done...")
            os.system(f"del {filename}")
            main()


if __name__ == "__main__":
    main()