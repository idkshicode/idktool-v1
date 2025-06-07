import requests
import os
import json 
from colorama import init, Fore, Style


init(autoreset=True)


#ascii banner
logo_lines = [
    "██╗██████╗ ██╗  ██╗████████╗ ██████╗  ██████╗ ██╗     ",
    "██║██╔══██╗██║ ██╔╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     ",
    "██║██║  ██║█████╔╝    ██║   ██║   ██║██║   ██║██║     ",
    "██║██║  ██║██╔═██╗    ██║   ██║   ██║██║   ██║██║     ",
    "██║██████╔╝██║  ██╗   ██║   ╚██████╔╝╚██████╔╝███████╗",
    "╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝",
    "                                          made by @idkshi224"
]

#colors for ascii
green_shades = [
    Fore.LIGHTGREEN_EX,
    Fore.GREEN,
    Fore.LIGHTGREEN_EX,
    Fore.GREEN,
    Fore.LIGHTGREEN_EX,
    Fore.GREEN,
    Fore.LIGHTGREEN_EX
]

logo = ""
for shade, line in zip(green_shades, logo_lines):
    logo += shade + line + "\n"
#title for the cmd
while True:
    os.system("title IDKTOOL")
    os.system("cls")
    print(logo)

    # menu
    menu_lines = [
        "[1] IP lookup",
        "[2] Webhook sender",
        "More Features on the way",
        ""
    ]

    # colors for menu
    red_shades = [Fore.LIGHTRED_EX, Fore.RED, Fore.LIGHTRED_EX]
    for i, line in enumerate(menu_lines):
        print(red_shades[i % len(red_shades)] + line)
#the input basically
    x = input(Fore.YELLOW + "Choose: " + Style.RESET_ALL)
#option 1 
    if x == "1":
        os.system("cls")
        print(Fore.CYAN + "IP Lookup\n")
        ip = input(Fore.YELLOW + "Type IP: " + Style.RESET_ALL)
#requests the ip data
        try:
            r = requests.get(f"http://ip-api.com/json/{ip}")
            data = r.json()
#results
            print(Fore.CYAN + "\nResults:\n")
            print(Fore.WHITE + f"Country: {Fore.GREEN}{data.get('country', 'N/A')}")
            print(Fore.WHITE + f"City: {Fore.GREEN}{data.get('city', 'N/A')}")
            print(Fore.WHITE + f"Region: {Fore.GREEN}{data.get('regionName', 'N/A')}")
            print(Fore.WHITE + f"TimeZone: {Fore.GREEN}{data.get('timezone', 'N/A')}")
        except Exception as e:
            print(Fore.RED + f"\nFailed to lookup IP: {e}")

        input(Fore.YELLOW + "\nPress Enter to return..." + Style.RESET_ALL)
#option 2
    elif x == "2":
        os.system("cls")
        print(Fore.CYAN + "Webhook Sender\n")
#inputs for the data
        webhook = input(Fore.YELLOW + "Webhook URL: " + Style.RESET_ALL)
        message = input(Fore.YELLOW + "Message: " + Style.RESET_ALL)
        data = {"content": message}
#requests from the webhook to send a msg
        try:
            response = requests.post(webhook, json=data)
            if response.status_code == 204:
                print(Fore.GREEN + "Message sent successfully.")
            else:
                print(Fore.RED + f"Failed to send message. Status code: {response.status_code}")
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

        input(Fore.YELLOW + "\nPress Enter to return..." + Style.RESET_ALL)
#if theres an error
    else:
        print(Fore.RED + "Invalid option!")
        input(Fore.YELLOW + "Press Enter to try again..." + Style.RESET_ALL)