from colored import fg, bg, attr
import time

hostname = "qamu-system-azure"

user = "root"
password = "root"

print("AzureOS on x86_64-qamu-system\nLoading kernel.img...")
time.sleep(3)

def uname():
    print(hostname)

def bash():
    