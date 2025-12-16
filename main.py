import argparse
import json
import sys
import time
import os


BANNER = r"""
███████╗██╗   ██╗███████╗███████╗
██╔════╝██║   ██║╚══███╔╝╚══███╔╝
█████╗  ██║   ██║  ███╔╝   ███╔╝ 
██╔══╝  ██║   ██║ ███╔╝   ███╔╝  
██║     ╚██████╔╝███████╗███████╗
╚═╝      ╚═════╝ ╚══════╝╚══════╝

☠️  FTP / SSH BRUTE FORCE TOOL
👁️  NO MERCY FOR WEAK PASSWORDS
🔥  USE RESPONSIBLY
"""

def scary_loading():
    print("[+] Loading dark modules", end="")
    for _ in range(6):
        time.sleep(0.3)
        print(".", end="")
        sys.stdout.flush()
    print("\n")

print(BANNER)
scary_loading()

parser = argparse.ArgumentParser(
    description="☠️ Bruteforce FTP or SSH using FUZZ keyword"
)

parser.add_argument(
    "service",
    choices=["FTP", "SSH"],
    help="Target service (FTP or SSH)"
)

parser.add_argument(
    "target",
    help="Target format: user:FUZZ@ip:port"
)

parser.add_argument(
    "-w", "--wordlist",
    required=True,
    help="Path to password wordlist"
)

args = parser.parse_args()


try:
    user_part, host_part = args.target.split("@")
    username, fuzz = user_part.split(":")
    ip, port = host_part.split(":")

    if fuzz != "FUZZ":
        raise ValueError

except ValueError:
    print("[!] Invalid target format!")
    print("    Correct format: user:FUZZ@ip:port")
    sys.exit(1)

print("[☠️] SERVICE  :", args.service)
print("[☠️] USER     :", username)
print("[☠️] TARGET   :", f"{ip}:{port}")
print("[☠️] WORDLIST :", args.wordlist)
print("[😈] Bruteforce initializing...\n")

data = {
    "service": args.service,
    "user": username,
    "ip": ip,
    "port": port,
    "wordlist": args.wordlist
}

def openFile(data : dict) :
    with open(".rq.json", "w") as file:
        json.dump(data, file)
openFile(data)
os.system("make")