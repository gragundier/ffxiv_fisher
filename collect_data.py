import keyboard
import time
import cv2

import numpy as np

from mss.windows import MSS as mss

RESOLUTION = 128
COLLECTED_RAW_DIR = "C:/Users/gragundier/Data/collected_raw/"
COLLECTED_DIR = "C:/Users/gragundier/Data/collected/"

monitor = {"top": 476, "left": 896, "width": RESOLUTION, "height": RESOLUTION}
output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

def hook(hook_type, sct_img, img):
    new_time = time.time()
    x = hook_type
    sct_img = cv2.cvtColor(sct_img.reshape(RESOLUTION,RESOLUTION,3), cv2.COLOR_RGB2BGR)
    img = cv2.cvtColor(img.reshape(RESOLUTION,RESOLUTION,3), cv2.COLOR_RGB2BGR)
    cv2.imwrite(COLLECTED_RAW_DIR+str(x)+"/"+"img"+str(new_time)+".png", sct_img)
    cv2.imwrite(COLLECTED_DIR+str(x)+"/"+"img"+str(new_time)+".png", img)

sct_img = None
sct_old = None
img = None

#keyboard.add_hotkey('q', hook, args=[1, sct_img, img])

with mss() as sct:
    try:
        while True:
            sct_img = np.array(sct.grab(monitor).pixels, dtype=np.uint8).reshape(1, RESOLUTION,RESOLUTION,3)
            if sct_old is not None:
                img = sct_img-sct_old
                keyboard.add_hotkey('q', hook, args=[1, sct_img, img], trigger_on_release=True)
                keyboard.add_hotkey('e', hook, args=[1, sct_img, img], trigger_on_release=True)
                keyboard.add_hotkey('f', hook, args=[0, sct_img, img], trigger_on_release=True)
                keyboard.add_hotkey('1', hook, args=[2, sct_img, img], trigger_on_release=True)
                keyboard.add_hotkey('2', hook, args=[0, sct_img, img], trigger_on_release=True)
                keyboard.add_hotkey('3', hook, args=[1, sct_img, img], trigger_on_release=True)
                keyboard.add_hotkey('m', hook, args=['m', sct_img, img], trigger_on_release=True)
                keyboard.add_hotkey('z', hook, args=["m2", sct_img, img], trigger_on_release=True)
                keyboard.add_hotkey('x', hook, args=[2, sct_img, img], trigger_on_release=True)
                keyboard.add_hotkey('c', hook, args=[2, sct_img, img], trigger_on_release=True)
            sct_old = sct_img
    
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    #closing stuff...