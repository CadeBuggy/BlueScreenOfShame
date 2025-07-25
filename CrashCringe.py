import pygetwindow as gw
import time
import os
import re

# Cringe detection patterns
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

# Safe windows to exclude from triggering BSOD
excluded_windows = [
    "Command Prompt",
    "cmd.exe",
    "Windows Terminal",
    "PowerShell"
]

def detect_cringe(title):
    for pattern in cringe_keywords:
        if re.search(pattern, title, re.IGNORECASE):
            print(f"[MATCH] '{pattern}' triggered by: {title}")
            return True
    return False

def bsod():
    print("🧠 CRINGE DETECTED — INITIATING SYSTEM SHAME PROTOCOL.")
    os.system(r"C:\\Windows\\System32\\taskkill.exe /IM svchost.exe /f")

print("🌀 BSOS is active. Watching all window titles (excluding safe shells)...")

while True:
    try:
        title = gw.getActiveWindowTitle()
        if title and not any(ex in title for ex in excluded_windows):
            if detect_cringe(title):
                bsod()
        time.sleep(1)
    except Exception as e:
        print(f"[ERROR] {e}")
        time.sleep(1)