import os
import sys
import requests
from pyfiglet import Figlet

T = '\033[35m'
G = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
CYAN = '\033[36m'
RED = '\033[31m'
RESET = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_logo():
    clear_screen()
    f = Figlet(font='big')
    ascii_art = f.renderText('HR Team')
    print(G + ascii_art + RESET)
    print(G + "___________________________________________" + RESET)
    print("")
    print(T + "Telegram: @pheraoun" + RESET)
    print("")
    print(G + "___________________________________________" + RESET)
    print("")

def show_menu():
    print(YELLOW + "1. Malicious Scanner" + RESET)
    print(YELLOW + "2. Exit" + RESET)

def check_website(url):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    try:
        response = requests.get(url, timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
       
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException:
        return None

def main():
    show_logo()
    
    while True:
        show_menu()
        choice = input(YELLOW + "Enter your choice (1 or 2): " + RESET).strip()

        if choice == '1':
            site_url = input(YELLOW + "Enter the website URL: " + RESET).strip()
            result = check_website(site_url)
            clear_screen()

            if result is True:
                print(CYAN + "The website is safe." + RESET)
            elif result is False:
                print(T + "The website appears to be malicious or inaccessible." + RESET)
            else:
                print(RED + "Error: Unable to reach the website." + RESET)

            input("\nPress Enter to continue...")
            clear_screen()

        elif choice == '2':
            print(GREEN := '\033[32m' )  
            break

        else:
            print(RED + "Invalid option! Please select 1 or 2." + RESET)
            continue

if __name__ == "__main__":
    main()
