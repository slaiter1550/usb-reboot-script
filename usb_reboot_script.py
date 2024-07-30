
import os
import time
import ctypes
from win32file import GetLogicalDrives, GetDriveType, DRIVE_REMOVABLE

# Define constants
USB_DRIVE_LABEL = "YourUSBLabel"  # Change this to the label of your USB drive

def get_usb_drives():
    drives = []
    drive_bits = GetLogicalDrives()
    for drive_letter in range(26):
        mask = 1 << drive_letter
        if drive_bits & mask:
            drive_name = f"{chr(65 + drive_letter)}:\\"
            if GetDriveType(drive_name) == DRIVE_REMOVABLE:
                drives.append(drive_name)
    return drives

def find_target_usb(drives):
    for drive in drives:
        if USB_DRIVE_LABEL in os.listdir(drive):
            return True
    return False

def main():
    while True:
        usb_drives = get_usb_drives()
        if find_target_usb(usb_drives):
            print("Target USB drive detected. Restarting system...")
            restart_system()
        time.sleep(5)

def restart_system():
    # This command will restart the computer
    if ctypes.windll.shell32.IsUserAnAdmin():
        os.system("shutdown /r /t 1")
    else:
        print("You need to run this script with administrative privileges.")

if __name__ == "__main__":
    main()
