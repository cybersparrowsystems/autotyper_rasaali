import pyautogui
from pynput import keyboard
import threading
import pyperclip
import time
import random

typing_active = False

def type_clipboard():
    global typing_active
    typing_active = True
    text = pyperclip.paste()
    for char in text:
        pyautogui.typewrite(char)
        delay = random.uniform(0.001, 0.005)  
        time.sleep(delay)
        if not typing_active:
            break
    typing_active = False


def start_typing():
    global typing_active
    if not typing_active:
        t = threading.Thread(target=type_clipboard)
        t.start()


def stop_typing():
    global typing_active
    typing_active = False

def on_press(key):
    if key == keyboard.Key.f8:
        start_typing()
    elif key == keyboard.Key.f9:
        stop_typing()


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()



#ParakumRasaali 
