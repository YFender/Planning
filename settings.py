from configparser import ConfigParser
import darkdetect
from PyQt5.Qt import QLocale

config = ConfigParser()
try:
    file = open("settings.ini", "r")
except Exception:
    print("ASDASD")
    config.add_section("Settings")
    config.set("Settings", "Language", f"{QLocale.system().name()}")
    config.set("Settings", "IsSystemDark", f"{darkdetect.isDark()}")
    with open("settings.ini", "w") as file:
        config.write(file)
