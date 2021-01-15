import tensorflow as tf
import time
import numpy as np
import keyboard
#import mss

from mss.windows import MSS as mss


monitor = {"top": 316, "left": 848, "width": 224, "height": 224}
output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

model = tf.keras.models.load_model("C:/Users/gragundier/Models/model1")

with mss() as sct:
    try:
        sct_old = None
        while True:
            sct_img = np.array(sct.grab(monitor).pixels).reshape(1, 224,224,3)
            if sct_old is not None:
                img = sct_old-sct_img
                #print(sct_img.shape)
                #print(model.predict(sct_img))
                #mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
                classification = model.predict(img)[0]
                #if classification[0] == 1:
                    #keyboard.send("2")
                if classification[1] == 1:
                    keyboard.send("q")
                    time.sleep(5)
                    keyboard.send("f")
            sct_old = sct_img

    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        #closing stuff...