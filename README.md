here is exactly what this script does: 

DETECTS USB: this script will detect when a specific USB drive is inserted. this script can be run in the background on the windows system (currently working on one for mac - this will be posted later)

RESTART SYSTEM: when the USB drive is detected, the script will restart the system. 

BIOS/UEFI SETTINGS (you MUST configure your BIOS/UEFI settings to boot from USB first. this part cannot be automated through a script and has to be set manually. 

notes: 

- ADMIN PRIVILEGES: make sure this script is being run with administrative privileges (to be able to restart the computer) 
- BIOS/UEFI CONFIG: make sure you manually set your BIOS/UEFI to prioritize USB booting (this setting makes sure that when the system restarts with the USB plugged in, it boots FROM THE USB. 

steps to follow:

1. ensure your BIOS/UEFI is set to boot from the USB
2. place the script on your windows running device/machine 
3. Customize the “USB_DRIVE_LABEL” in the script with the label of your USB drive
4. run the script with admin 
5. plug in the USB drive

personal note: im working on a script for mac os right now. :]]
