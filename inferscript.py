import tensorflow as tf
import cv2
import time
import numpy as np
import keyboard
import matplotlib.pyplot as plt
import random
#import mss

from mss.windows import MSS as mss

gpu = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(gpu[0], True)

RESOLUTION = 224

monitor = {"top": 428, "left": 848, "width": RESOLUTION, "height": RESOLUTION}
output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

model = tf.keras.models.load_model("C:/Users/gragundier/Models/model1")
model2 = tf.keras.models.load_model("C:/Users/gragundier/Models/checkpoint")

print("Model loaded...")

HOOKED_DIR = "C:/Users/gragundier/Data/hooked/"
DISAGREE_DIR = "C:/Users/gragundier/Data/disagree/"


'''
input_dict = {
    "q": ""
}
'''

#def record(input, classification):
#

#def save_data():

#print("Hotkeys loaded...")

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
                    x = np.argmax(classification2)
                    sct_img_print = cv2.cvtColor(sct_img.reshape(RESOLUTION,RESOLUTION,3), cv2.COLOR_RGB2BGR)
                    img_print = cv2.cvtColor(img.reshape(RESOLUTION,RESOLUTION,3), cv2.COLOR_RGB2BGR)
                    cv2.imwrite(DISAGREE_DIR+str(x)+"/"+"img"+str(new_time)+".png", sct_img_print)
                    cv2.imwrite(DISAGREE_DIR+str(x)+"/"+"img"+str(new_time)+".png", img_print)
                    

                #if classification[0] == 1:
                    #keyboard.send("2")
                if classification[1] >= 0.9:
                    if classification[1] >= 0.9:
                        print("Hook Detected!")

                        print("Time Passed: ",new_time-old_time)
                        #if (new_time-old_time > 0.0):
                        if True:
                            print("Reeling")
                            #keyboard.send("e")
                            #time.sleep(0.2)
                            #keyboard.send("e")
                            time.sleep(0.2)
                            keyboard.send("q")
                            time.sleep(0.2)
                            keyboard.send("q")
                            time.sleep(6)
                        else:
                            print("Passing")
                            keyboard.send("r")
                            time.sleep(0.2)
                            keyboard.send("r")
                            time.sleep(4)

                    sct_img_print = cv2.cvtColor(sct_img.reshape(RESOLUTION,RESOLUTION,3), cv2.COLOR_RGB2BGR)
                    img_print = cv2.cvtColor(img.reshape(RESOLUTION,RESOLUTION,3), cv2.COLOR_RGB2BGR)
                    cv2.imwrite(HOOKED_DIR+str(x)+"/"+"img"+str(new_time)+".png", sct_img_print)
                    cv2.imwrite(HOOKED_DIR+str(x)+"/"+"img"+str(new_time)+".png", img_print)

                    keyboard.send("4")
                    time.sleep(0.2)
                    keyboard.send("4")
                    time.sleep(0.3)
                    keyboard.send("z")
                    time.sleep(0.2)
                    keyboard.send("z")
                    time.sleep(0.3)
                    keyboard.send("f")
                    time.sleep(0.2)
                    keyboard.send("f")
                    old_time = new_time
                '''
                else:
                    if classification[2] >= 0.9:
                        x = np.argmax(classification2)
                        plt.imsave(HOOKED_DIR+str(x)+"/"+"img"+str(new_time)+".png", sct_img.reshape(224,224,3))
                        plt.imsave(HOOKED_DIR+str(x)+"/"+"img"+str(new_time)+"s.png", img.reshape(224,224,3))
                    if classification[0] >= 0.9 and random.randint(0,100000) > 95000:
                        x = np.argmax(classification2)
                        plt.imsave(HOOKED_DIR+str(x)+"/"+"img"+str(new_time)+".png", sct_img.reshape(224,224,3))
                        plt.imsave(HOOKED_DIR+str(x)+"/"+"img"+str(new_time)+"s.png", img.reshape(224,224,3))
                '''

                if random.randint(0,100) > 95:
                    #ftime.sleep(random.randint(0,2))
                    keyboard.send("f")
                    time.sleep(0.2)
                    keyboard.send("f")
                    

            #else:
            #    img = sct_img
                    
            sct_old = sct_img

    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        #closing stuff...ffff