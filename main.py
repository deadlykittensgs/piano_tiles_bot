import pyautogui
import time
from pynput import keyboard
import mss


# Variables 
positions = [
{"x": 240, "y": 750},
{"x": 313, "y": 750},
{"x": 435, "y": 750},
{"x": 536, "y": 750}
]

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


# run a loop checking a single pixel to see if the color matches the target color
with mss.mss() as sct:
    while running:
        clicked = False
        for pos in positions:
            monitor = {"top": pos["y"], "left": pos["x"], "width": 1, "height": 1}
            img = sct.grab(monitor)
            pixel = img.pixel(0, 0)

            if pixel[:4] == target_color[:4]:  # Compare RGB only
                pyautogui.click(pos["x"], pos["y"])
                print(f"Clicked at ({pos['x']}, {pos['y']})!")
                clicked = True
        

        if not clicked:
            print("Waiting...")
            time.sleep(0.01)