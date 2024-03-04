import pyautogui
from pynput import keyboard
import threading
import pyperclip
import time
import random

typing_active = False
paused = False

def type_clipboard():
    global typing_active, paused
    typing_active = True
    text = pyperclip.paste()
    for char in text:
        if not paused:
            pyautogui.typewrite(char)
            delay = random.uniform(0.001, 0.005)  
            time.sleep(delay)
        else:
            while paused:
                time.sleep(0.1)  # Sleeps for a short time to reduce CPU load
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


def pause_typing():
    global paused
    paused = True


def resume_typing():
    global paused
    paused = False


def on_press(key):
    if key == keyboard.Key.f8:
        start_typing()
    elif key == keyboard.Key.f9:
        stop_typing()
    elif key == keyboard.Key.f4:
        if not typing_active:
            start_typing()
        elif paused:
            resume_typing()
        else:
            pause_typing()


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
