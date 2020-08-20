import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

def w():
    keyboard.press("w")
    time.sleep(1)
    keyboard.release("w")

def wd():
    keyboard.press("w")
    keyboard.press("d")
    time.sleep(1)
    keyboard.release("w")
    keyboard.release("d")

def wa():
    keyboard.press("w")
    keyboard.press("a")
    time.sleep(1)
    keyboard.release("w")
    keyboard.release("a")

def s():
    keyboard.press("s")
    time.sleep(1)
    keyboard.release("s")

def sd():
    keyboard.press("s")
    keyboard.press("d")
    time.sleep(1)
    keyboard.release("s")
    keyboard.release("d")

def sa():
    keyboard.press("s")
    keyboard.press("a")
    time.sleep(1)
    keyboard.release("s")
    keyboard.release("a")

def a():
    keyboard.press("a")
    time.sleep(1)
    keyboard.release("a")

def d():
    keyboard.press("d")
    time.sleep(1)
    keyboard.release("d")

def slow_down():
    keyboard.release("w")
    keyboard.release("s")
    keyboard.release("a")
    keyboard.release("d")
