from core.runner import run_campaign
from core.validator import validate_phone, validate_config
from core.banner import show_banner
from core.logger import Logger
import json, os, sys

def check_terms():
    if not os.path.exists("terms.txt"):
        print("[!] terms.txt not found.")
        sys.exit(1)
    with open("terms.txt") as f:
        print(f.read())
    agree = input("Do you agree to the terms? (yes/no): ").strip().lower()
    if agree != 'yes':
        print("[-] User declined terms.")
        sys.exit(0)

def load_services():
    with open("config/services.json") as f:
        return json.load(f)

def main():
    show_banner()
    check_terms()

    phone = input("Target Phone (e.g., 912XXXXXXX): ").strip()
    if not validate_phone(phone):
        print("[-] Invalid phone format.")
        return

    rounds = int(input("Rounds [default=1]: ") or 1)
    threads = int(input("Threads [default=5]: ") or 5)
    delay = float(input("Sleep between rounds [default=1.0]: ") or 1.0)
    dry_run = input("Dry Run (Y/n)? ").strip().lower() == 'y'

    logger = Logger()
    services = load_services()

    run_campaign(phone, services, rounds, threads, delay, logger, dry_run)

if __name__ == "__main__":
    main()
