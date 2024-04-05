import subprocess
import time
import ctypes
import sys

SECONDS_WITH_WIFI_DISABLED = 3 * 60 * 60  # 3 hours in seconds
SECONDS_WITH_WIFI_ENABLED = 60

# Constants for the command prompt
CMD_BASE = 'cmd /c "{}"'  # first is remain/terminate, then is enable/disable
WIFI_CMD_BASE = 'wmic path win32_networkadapter where NetConnectionID="Wi-fi" call {}'
WIFI_CMD_ENABLE = WIFI_CMD_BASE.format('enable')
WIFI_CMD_DISABLE = WIFI_CMD_BASE.format('disable')

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

def main():
    if is_admin():
        turn_off_wifi()
        time.sleep(SECONDS_WITH_WIFI_DISABLED)
        turn_on_wifi()
        time.sleep(SECONDS_WITH_WIFI_ENABLED)
    else:
        run_as_admin()

def execute_cmd(cmd):
    subprocess.call(cmd, shell=True)

def turn_on_wifi():
    execute_cmd(CMD_BASE.format(WIFI_CMD_ENABLE))

def turn_off_wifi():
    execute_cmd(CMD_BASE.format(WIFI_CMD_DISABLE))

if __name__ == "__main__":
    main()

#This program disables your network wifi adaptor.
#To re-enable go to: settings, network adaptors, Wifi adaptor, edit, activate.