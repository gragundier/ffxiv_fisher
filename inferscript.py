import tensorflow as tf
import numpy as np
import keyboard
#import mss

from mss.windows import MSS as mss


monitor = {"top": 316, "left": 848, "width": 224, "height": 224}
output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

model = tf.keras.models.load_model("model")

with mss() as sct:
    try:
        while True:
            sct_img = np.array(sct.grab(monitor).pixels).reshape(1, 224,224,3)
            #print(sct_img.shape)
            #print(model.predict(sct_img))
            #mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
            classification = model.predict(sct_img)[0]
            if classification[0] == 1:
                keyboard.send("2")
            elif classification[1] == 1:
                keyboard.send("q")
            elif classification[2] == 1:
                keyboard.send("e")
            elif classification[3] == 1:
                keyboard.send("e")
            elif classification[3] == 1:
                keyboard.send("e")
            elif classification[4] == 1:
                keyboard.send("e")

    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        #closing stuff...