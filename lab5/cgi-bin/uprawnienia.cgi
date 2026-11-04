#!/usr/bin/python3
import os

print("Content-Type: text/plain; charset=utf-8")
print()
print(f"EUID: {os.geteuid()}")
print(f"EGID: {os.getegid()}")
for sciezka in ("/lab-data/ogolny.txt", "/lab-data/poufny.txt"):
    try:
        with open(sciezka, encoding="utf-8") as f:
            print(f"{sciezka}: {f.read().strip()}")
    except OSError as e:
        print(f"{sciezka}: odmowa odczytu ({e.strerror})")
