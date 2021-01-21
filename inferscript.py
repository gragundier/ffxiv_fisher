import tensorflow as tf
import cv2
import time
import numpy as np
import keyboard
import matplotlib.pyplot as plt
import random
#import mss

from mss.windows import MSS as mss
import mss.windows as mssw


monitor = {"top": 428, "left": 848, "width": 224, "height": 224}
output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

model = tf.keras.models.load_model("C:/Users/gragundier/Models/model1")
model2 = tf.keras.models.load_model("C:/Users/gragundier/Models/conv1")

HOOKED_DIR = "C:/Users/gragundier/Data/hooked/"
DISAGREE_DIR = "C:/Users/gragundier/Data/disagree/"

print("Model loaded...")

counter = 0
with mss() as sct:
    try:
        print("Beginning inference loop...")
        sct_old = None

        old_time = 0
        new_time = 0
        while True:
            sct_img = np.array(sct.grab(monitor).pixels, dtype=np.uint8).reshape(1, 224,224,3)
            #sct_test = sct_img.reshape(224,224,3)
            #plt.imshow(sct_test)
            #plt.show()
            if sct_old is not None:
                img = sct_img-sct_old
                #print(sct_img.shape)
                #print(model.predict(img), " ", model2.predict(img))
                #print(model2.predict(img))
                #mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
                classification = model.predict(img)[0]
                classification2 = model2.predict(img)[0]

                new_time = time.time()

                if abs(classification2[1] - classification[1]) > 0.1:
                    plt.imsave(DISAGREE_DIR+"img"+str(new_time)+".png", sct_img.reshape(224,224,3))
                    plt.imsave(DISAGREE_DIR+"img"+str(new_time)+"s"+str(classification2[0])+".png", img.reshape(224,224,3))

                #if classification[0] == 1:
                    #keyboard.send("2")
                if classification[1] >= 0.9:
                    if classification[1] >= 0.9:
                        print("Hook Detected!")

                        print("Time Passed: ",new_time-old_time)
                        if (new_time-old_time > 22.0):
                            print("Reeling")
                            keyboard.send("e")
                            time.sleep(0.2)
                            keyboard.send("e")
                            time.sleep(0.2)
                            keyboard.send("q")
                            time.sleep(0.2)
                            keyboard.send("q")
                            time.sleep(9)
                        else:
                            print("Passing")
                            keyboard.send("r")
                            time.sleep(0.2)
                            keyboard.send("r")
                            time.sleep(4)

                        plt.imsave(HOOKED_DIR+"img"+str(new_time)+".png", sct_img.reshape(224,224,3))
                        plt.imsave(HOOKED_DIR+"img"+str(new_time)+"s.png", img.reshape(224,224,3))

                    keyboard.send("f")
                    time.sleep(0.2)
                    keyboard.send("f")
                    old_time = new_time

                if random.randint(0,100) > 95:
                    #ftime.sleep(random.randint(0,2))
                    keyboard.send("f")
                    time.sleep(0.2)
                    keyboard.send("f")
                    


                    
            sct_old = sct_img

    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        #closing stuff...ffff