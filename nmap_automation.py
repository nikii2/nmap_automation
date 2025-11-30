#!/usr/bin/env python3
import argparse
import subprocess
import datetime
from pathlib import Path
import sys

def run_nmap(target, options):
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    safe_target = target.replace("/", "_")
    out_file = Path(f"nmap-{safe_target}-{timestamp}.txt")
    cmd = ["nmap"] + options.split() + ["-oN", str(out_file), target]
    print(f"[+] Running: {' '.join(cmd)}")
    try:
        subprocess.run(cmd, check=True)
    except FileNotFoundError:
        print("[-] nmap не е инсталиран или не е в PATH.")
        sys.exit(1)
    except subprocess.CalledProcessError:
        print("[-] nmap приключи с грешка.")
    else:
        print(f"[+] Резултатите са записани в {out_file}")

def main():
    parser = argparse.ArgumentParser(description="Прост автоматизатор за nmap сканирания.")
    parser.add_argument("target", help="Цел за сканиране (IP, домейн, мрежа).")
    parser.add_argument(
        "-o", "--options",
        default="-sV -sC",
        help="Опции за nmap (по подразбиране: '-sV -sC')."
    )
    args = parser.parse_args()
    run_nmap(args.target, args.options)

if __name__ == '__main__':
    main()
