import pyautogui
import time
from pynput import keyboard
import mss
from PIL import ImageGrab



target_color = (29, 47, 83)
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
    while running == True:
        pixel_One = sct.grab({"top": 550, "left": 240, "width": 1, "height": 1}).pixel(0, 0)
        # print("p1" , pixel_One)
        pixel_Two = sct.grab({"top": 550, "left": 313, "width": 1, "height": 1}).pixel(0, 0)
        # print("p2" , pixel_Two)
        pixel_Three = sct.grab({"top": 550, "left": 435, "width": 1, "height": 1}).pixel(0, 0)
        # print("p3" , pixel_Three)
        pixel_Four = sct.grab({"top": 550, "left": 536, "width": 1, "height": 1}).pixel(0, 0)
        # print("p4" , pixel_Four)
        if pixel_One == target_color:
            pyautogui.moveTo(x=240, y=550)
            pyautogui.click()
            print("p1" , pixel_One)
        if pixel_Two == target_color:
            pyautogui.moveTo(x=313, y=550)
            pyautogui.click()
            print("p2" , pixel_Two)
        if pixel_Three == target_color:
            pyautogui.moveTo(x=435, y=550)
            pyautogui.click()
            print("p3" , pixel_Three)
        if pixel_Four == target_color:
            pyautogui.moveTo(x=536, y=550)
            pyautogui.click()
            print("p4" , pixel_Four)

        time.sleep(0.01)