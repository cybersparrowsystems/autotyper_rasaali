import subprocess
import sys
print("Rasaali")
def install_packages(packages):
    for package in packages:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    required_packages = ["pyautogui", "pynput", "pyperclip"]
    install_packages(required_packages)
    print("All required packages installed successfully!")


