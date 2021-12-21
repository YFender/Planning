from configparser import ConfigParser
import darkdetect
from locale import getlocale

config = ConfigParser()
try:
    file = open("settings.ini", "r")
except Exception:
    print("ASDASD")
    config.add_section("Settings")
    config.set("Settings", "Language", f"{getlocale()[0]}")
    config.set("Settings", "IsSystemDark", f"{darkdetect.isDark()}")
    with open("settings.ini", "w") as file:
        config.write(file)
