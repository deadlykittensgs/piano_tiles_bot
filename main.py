import pyautogui
import time
from pynput import keyboard
import mss
from PIL import ImageGrab



target_color = (22, 43, 86) 
running = True


# Function to kill process
def on_press(key):
    global running
    try:
        if key.char == 'q':
            print("Q pressed — stopping loop.")
            running = False
            return False
    except:
        pass




# start a listener to run function on press  
listener = keyboard.Listener(on_press=on_press)
listener.start() 

with mss.mss() as sct: 
    while running:
        pixel_One = sct.grab({"top": 550, "left": 240, "width": 1, "height": 1}).pixel(0, 0)
        pixel_Two = sct.grab({"top": 550, "left": 313, "width": 1, "height": 1}).pixel(0, 0)
        pixel_Three = sct.grab({"top": 550, "left": 435, "width": 1, "height": 1}).pixel(0, 0)
        pixel_Four = sct.grab({"top": 550, "left": 536, "width": 1, "height": 1}).pixel(0, 0)
        if pixel_One == target_color:
            pyautogui.click(240, 550)
        if pixel_Two == target_color:
            pyautogui.click(313, 550)
        if pixel_Three == target_color:
            pyautogui.click(435, 550)
        if pixel_Four == target_color:
            pyautogui.click(536, 550)

        time.sleep(0.01)