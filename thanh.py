import requests
import subprocess
import re

# Download the file from GitHub
url = "https://raw.githubusercontent.com/caonhatthanh/tweaksperformance/main/build.prop"
response = requests.get(url)

# Parse the settings from the file
settings = {}
for line in response.text.splitlines():
    match = re.match(r"(\w+)=.*", line)
    if match:
        setting_name = match.group(1)
        setting_value = line.split("=")[1].strip()
        settings[setting_name] = setting_value

# Apply the settings to the Android device
adb_path = "/path/to/adb"
subprocess.run([f"{adb_path} shell", f"settings put {settings['ro.build.version.release']}"])
for setting, value in settings.items():
    if setting != "ro.build.version.release":
        subprocess.run([f"{adb_path} shell", f"settings put {setting} {value}"])

print("Settings applied!")
