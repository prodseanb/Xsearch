# input URL link, validate, then Xsearch script will run it
import sys
import requests
import argparse
import urllib.request
import io
import csv
# use argparse

class bcolors:
    WARNING="\033[93m"
    ENDC = '\033[0m'

def check_target(args):
    response = requests.get(f'https://raw.githubusercontent.com/offensive-security/exploitdb/master/{args.examine}')
    if response.status_code == 200:
        return True
    return False


def scrape(args):
    page = urllib.request.urlopen(f'https://raw.githubusercontent.com/offensive-security/exploitdb/master/{args.examine}')
    reader = csv.reader(io.TextIOWrapper(page))

    for row in reader:
        print(bcolors.WARNING + ", ".join(row) + bcolors.ENDC)

def main():
    parser = argparse.ArgumentParser(description="Examine the exploit")
    parser.add_argument("examine", metavar="<target exploit/shellcode>", help="Target exploit/shellcode")
    args = parser.parse_args()

    if check_target(args):
        scrape(args)
    else:
        print("[!] Exploit/shellcode not available/does not exist in the database.")
        exit
if __name__ == "__main__":
    main()