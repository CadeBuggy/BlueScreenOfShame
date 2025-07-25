# BlueScreenOfShame
Crashes computer if it sees cringe (Windows only)

Blue Screen of Shame is a Python script that monitors the active browser window for keywords associated with low-quality or cringe content. If any predefined keyword is detected in the window title (such as in a YouTube video tab), the script will force a Blue Screen of Death (BSOD) by terminating a critical system process.

This tool is designed as a humorous but effective way to discourage unwanted browsing behavior.

What It Does
Continuously monitors the active window title.

Searches for specific keywords that are considered "cringe" (e.g., "roblox gf", "e-girl", "asmr", etc.).

If a match is found, the script executes a taskkill command to terminate svchost.exe, which will immediately crash the system and trigger a BSOD.

Requirements
Windows 10 or 11

Python 3.x

Administrative privileges (to execute system-level commands)

pygetwindow module (pip install pygetwindow)

psutil module (pip install psutil)

Installation
Clone or download this repository.

Install required Python packages:

nginx
Copy
Edit
pip install pygetwindow psutil
Run the script in an elevated command prompt (right-click > Run as administrator):

nginx
Copy
Edit
python bsos.py
Notes
This script is intentionally destructive. It should only be run in test environments or with full understanding of its behavior.

This script will immediately crash the computer if a match is found. There is no confirmation or undo.

The script uses the Windows built-in taskkill utility to force termination of system-critical processes. Misuse may result in data loss.

Disclaimer
This project is for educational or comedic purposes only. Use at your own risk. The author is not responsible for any damage, data loss, or disruption caused by running this script.
