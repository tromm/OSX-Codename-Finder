#MIT License
#Copyright (c) 2023 tromm
#https://github.com/tromm
#see: LICENCSE FILE
#version 1.0

import sys

# Check Python version
if sys.version_info[0] < 3:
    print("Error: This script requires Python 3.")
    print("You can install Python 3 with 'brew install python3'.")
    sys.exit(1)

# Check for required libraries
required_libs = ["requests", "bs4"]  # Use 'bs4' instead of 'beautifulsoup4'
missing_libs = []

for lib in required_libs:
    try:
        __import__(lib)
    except ImportError:
        missing_libs.append(lib)

if missing_libs:
    print("Error: Missing libraries - " + ", ".join(missing_libs))
    print("Install the missing libraries with 'pip3 install " + " ".join(missing_libs) + "'")
    sys.exit(1)

import requests
from bs4 import BeautifulSoup
import subprocess
import argparse
import sys

def get_macos_codename(version, list_versions=False, debug=False):
    # URL of the Apple support page
    url = "https://support.apple.com/en-us/HT201260"

    # Fetch webpage content only if needed
    try:
        if debug:
            print(f"Attempting to access URL: {url}")
        response = requests.get(url)
        if response.status_code != 200:
            return "Error accessing Apple support page."
        if debug:
            print("Successfully accessed Apple support page.")
    except requests.exceptions.ConnectionError:
        return "Error: Unable to connect to the internet."

    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.find_all('tr')

    found_versions = []
    codename_match = None

    # Iterate through table rows
    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 2:
            macos_name, listed_version = cells[0].text.strip(), cells[1].text.strip()
            found_versions.append(f"{macos_name} - {listed_version}")
            if debug:
                print(f"Found: {macos_name} - {listed_version}")

            # Compare versions
            main_version, _, sub_version = version.partition('.')
            main_listed_version, _, sub_listed_version = listed_version.partition('.')
            if main_version == main_listed_version and (not sub_version or sub_version <= sub_listed_version):
                codename_match = macos_name

    if list_versions:
        print("All found macOS versions from the Apple support page:")
        for v in found_versions:
            print(v)
        sys.exit(0)

    return codename_match

def main():
    parser = argparse.ArgumentParser(description="Get macOS codename. Note: Some options require an online connection.")
    parser.add_argument('--codename', action='store_true', help='Return only the codename (requires online connection).')
    parser.add_argument('--version', action='store_true', help='Return only the macOS version.')
    parser.add_argument('--list-versions', action='store_true', help='List all macOS versions found on the Apple support page (requires online connection).')
    parser.add_argument('--debug', action='store_true', help='Show debug information (requires online connection).')
    args = parser.parse_args()

    if args.version:
        # Retrieve current macOS version
        version_process = subprocess.run(["sw_vers", "-productVersion"], capture_output=True, text=True)
        if version_process.returncode != 0:
            print("Error retrieving macOS version.")
            sys.exit(1)
        print(version_process.stdout.strip())
        sys.exit(0)

    # Read the current macOS version
    version_process = subprocess.run(["sw_vers", "-productVersion"], capture_output=True, text=True)
    if version_process.returncode != 0:
        print("Error retrieving macOS version.")
        sys.exit(1)

    system_version = version_process.stdout.strip()
    if args.debug:
        print(f"System version: {system_version}")

    # Retrieve codename
    codename = get_macos_codename(system_version, list_versions=args.list_versions, debug=args.debug)
    if codename:
        if args.codename:
            print(codename)
        else:
            print(f"The codename for macOS version {system_version} is: {codename}")
    else:
        print("Codename not found.")

if __name__ == '__main__':
    main()

