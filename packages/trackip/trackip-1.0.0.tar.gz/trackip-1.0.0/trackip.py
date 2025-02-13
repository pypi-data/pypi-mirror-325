import requests
import json
import sys
import os
from colorama import Fore, Style, init

# Init Colorama for Windows/Linux
init(autoreset=True)

# 🔥 App Info 🔥
APP_NAME = "TrackIP - The Ultimate IP Tracker CLI"
AUTHOR = "Nayan Das"
AUTHOR_WEBSITE = "https://socialportal.nayanchandradas.com"
AUTHOR_EMAIL = "nayanchandradas@hotmail.com"
CURRENT_VERSION = "1.0.0"
REPO_URL = "https://github.com/nayandas69/trackip"
LATEST_RELEASE_API = "https://api.github.com/repos/nayandas69/trackip/releases/latest"


# 🖼️ Banner (Aesthetic Vibes, Cuz Why Not?)
def show_banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        f"""
{Fore.MAGENTA}

▄▄▄█████▓ ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀    ██▓ ██▓███  
▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒    ▓██▒▓██░  ██▒
▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░    ▒██▒▓██░ ██▓▒
░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄    ░██░▒██▄█▓▒ ▒
  ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄   ░██░▒██▒ ░  ░
  ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒   ░▓  ▒▓▒░ ░  ░
    ░      ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░    ▒ ░░▒ ░     
  ░        ░░   ░   ░   ▒   ░        ░ ░░ ░     ▒ ░░░       
            ░           ░  ░░ ░      ░  ░       ░           
                            ░                               

{Fore.YELLOW}🔹 {APP_NAME} v{CURRENT_VERSION}
🔹 Author: {AUTHOR}
🔹 Website: {AUTHOR_WEBSITE}
🔹 Contact: {AUTHOR_EMAIL}
"""
    )


# 🔍 Function to Get IP Info
def track_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    print(f"\n{Fore.CYAN}🔍 Fetching details for IP: {ip}...\n")

    try:
        response = requests.get(url)
        data = response.json()

        if data["status"] == "fail":
            print(f"{Fore.RED}❌ Couldn't fetch IP details. Error: {data['message']}")
            return

        print(f"{Fore.GREEN}🌍 IP Address: {data['query']}")
        print(f"{Fore.YELLOW}📍 Country: {data['country']} ({data['countryCode']})")
        print(f"{Fore.CYAN}🏙️  City: {data['city']}")
        print(f"{Fore.MAGENTA}📡 ISP: {data['isp']}")
        print(f"{Fore.BLUE}🗺️  Latitude: {data['lat']} | Longitude: {data['lon']}")
        print(f"{Fore.LIGHTRED_EX}🕵️  Org: {data['org']}")
        print(f"{Fore.LIGHTCYAN_EX}📊 ZIP Code: {data['zip']}")
        print(f"{Fore.LIGHTGREEN_EX}⏳ Timezone: {data['timezone']}")

    except requests.RequestException:
        print(f"{Fore.RED}❌ Bruh, couldn't connect to the API. Check your internet!")


# 📡 Get Public IP
def get_my_ip():
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        return response.json().get("ip", "Unknown")
    except requests.RequestException:
        return "Unknown"


# 🔄 Check for Updates
def check_for_update():
    print(f"{Fore.GREEN}📌 Current Version: {CURRENT_VERSION}")
    print(f"{Fore.CYAN}🔄 Checking for updates...\n")

    try:
        response = requests.get(LATEST_RELEASE_API)
        response.raise_for_status()
        latest_version = response.json().get("tag_name", CURRENT_VERSION)

        if latest_version != CURRENT_VERSION:
            print(
                f"{Fore.YELLOW}⚡ New version available: {latest_version}! Check it here: {REPO_URL}"
            )
        else:
            print(f"{Fore.GREEN}✅ You're up-to-date! 🎉")
    except requests.RequestException:
        print(
            f"{Fore.RED}❌ Couldn't check for updates. Maybe GitHub is acting sus? 🤨"
        )


# 🎯 Main Menu
def main_menu():
    while True:
        show_banner()
        print(
            f"""
{Fore.BLUE}📌 Main Menu:
{Fore.GREEN}1️⃣  Start Tracking
2️⃣  Check for Update
3️⃣  Help
4️⃣  Exit
"""
        )
        choice = input(f"{Fore.LIGHTMAGENTA_EX}👉 Select an option: ")

        if choice == "1":
            ip = input(
                f"\n{Fore.CYAN}🌍 Enter an IP (or type 'my' to check your own): "
            )
            if ip.lower() == "my":
                ip = get_my_ip()
            track_ip(ip)
            input(f"\n{Fore.YELLOW}⏭️ Press Enter to return to the main menu...")

        elif choice == "2":
            check_for_update()
            input(f"\n{Fore.YELLOW}⏭️ Press Enter to return to the main menu...")

        elif choice == "3":
            print(
                f"""
{Fore.YELLOW}🔹 {APP_NAME} - Help Menu 🔹
{Fore.LIGHTBLUE_EX}This CLI tool lets you track any IP address to get details like:
- 🌎 Country, City, ISP
- 🗺️  Geolocation (Latitude & Longitude)
- 🕵️  Organization & Zip Code
- ⏳ Timezone

{Fore.GREEN}How to Use:
1️⃣  Select 'Start Tracking' from the menu.
2️⃣  Enter an IP address or type 'my' to check your own.
3️⃣  View results with full details.

{Fore.LIGHTRED_EX}P.S. This tool respects privacy and does NOT store any IP data.
"""
            )
            input(f"\n{Fore.YELLOW}⏭️ Press Enter to return to the main menu...")

        elif choice == "4":
            print(f"\n{Fore.GREEN}🚀 See ya, nerd! Stay safe online. ✌️")
            sys.exit()

        else:
            print(f"{Fore.RED}❌ Bro, that's not a valid option. Try again.")


# 🚀 Run the CLI
if __name__ == "__main__":
    main_menu()
