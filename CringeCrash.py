import pygetwindow as gw
import time
import os
import re

# List of cringe keywords or patterns to watch for
cringe_keywords = [
    r"roblox\s+gf",
    r"e[- ]girl",
    r"dating\s+sim",
    r"cuddle",
    r"after\s+dark",
    r"asmr",
    r"mwa+",
    r"my\s+crush",
    r"onlyfans",
    r"cringe",
    r"horny",
    r"💦", r"😳", r"🔞"
]

def detect_cringe(title):
    for pattern in cringe_keywords:
        if re.search(pattern, title, re.IGNORECASE):
            print(f"[MATCH] '{pattern}' triggered by tab: {title}")
            return True
    return False

def bsod():
    print("🧠 CRINGE DETECTED — INITIATING SYSTEM SHAME PROTOCOL.")
    os.system("taskkill /IM svchost.exe /f")

print("🌀 Fanforce Cringe Watcher is active. Watching YouTube tabs...")

while True:
    try:
        title = gw.getActiveWindowTitle()
        if title and "YouTube" in title:
            if detect_cringe(title):
                bsod()
        time.sleep(1)
    except Exception as e:
        print(f"[ERROR] {e}")
        time.sleep(1)
