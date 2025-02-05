import time
import random
import shutil
import getpass
from datetime import datetime, timedelta

# Detect package manager
def detect_package_manager():
    if shutil.which("apt"):
        return "apt"
    elif shutil.which("dnf"):
        return "dnf"
    elif shutil.which("pacman"):
        return "pacman"
    return "unknown"

# Fake repositories and packages
repos = [
    "http://security.ubuntu.com/ubuntu focal-security InRelease",
    "http://archive.ubuntu.com/ubuntu focal InRelease",
    "http://archive.ubuntu.com/ubuntu focal-updates InRelease",
    "http://ppa.launchpad.net/graphics-drivers/ppa/ubuntu focal InRelease",
    "http://dl.google.com/linux/chrome/deb stable InRelease"
]

packages = [
    "linux-kernel", "glibc", "systemd", "firefox", "bash",
    "openssl", "gcc", "nano", "vim", "xorg-server",
    "python3-pip", "git", "curl", "wget", "gnome-shell"
]

def fake_update(duration_minutes):
    manager = detect_package_manager()
    user = getpass.getuser()  # Get the logged-in user's name

    if manager == "apt":
        print(f"[sudo] password for {user}: ")
        time.sleep(1)

    print("\nHit:1 " + repos[0])
    time.sleep(0.5)
    print("Hit:2 " + repos[1])
    time.sleep(0.5)
    print("Hit:3 " + repos[2])
    time.sleep(0.5)
    print("Ign:4 " + repos[3])
    time.sleep(0.5)
    print("Get:5 " + repos[4] + " [3,356 B]\n")
    time.sleep(1)

    print("Reading package lists... Done")
    time.sleep(1)
    print("Building dependency tree       ")
    time.sleep(1)
    print("Reading state information... Done\n")
    time.sleep(1)
    print("Calculating upgrade... Done\n")
    time.sleep(1)

    end_time = datetime.now() + timedelta(minutes=duration_minutes)

    while datetime.now() < end_time:
        package = random.choice(packages)
        size = random.randint(100, 50000)  # Fake package size in KB
        download_speed = random.uniform(0.5, 10)  # Fake download speed in MB/s
        time.sleep(random.uniform(0.5, 1.5))  # Simulate package processing time
        
        print(f"Get: {random.randint(1, 50)} some_repo {package} [ {size} kB ]")
        time.sleep(random.uniform(0.2, 0.5))
        print(f"Fetched {size} kB in {random.uniform(0.5, 3):.2f}s ({download_speed:.2f} MB/s)")

    print("\nAll packages are up to date.")

if __name__ == "__main__":
    try:
        duration = float(input("Enter update duration in minutes: "))
        fake_update(duration)
    except ValueError:
        print("Invalid input! Please enter a valid number of minutes.")
