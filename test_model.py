import numpy as np
import cv2
from getkeys import key_check
from getscreen import get_screen
import presskeys
import os
import time
import tensorflow as tf
from tensorflow.keras.models import load_model

PATH_TO_MODEL = "" #Put in your path to your model

def main():

    model = load_model(f"{PATH_TO_MODEL}.h5")
    
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    if not paused:
        while(True):
            screen = get_screen(region=(0,40,800,600))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (80,60))
            moves = list(np.around(model.predict([screen.reshape(-1,80,60,1)])[0]))

            for i in range(len(moves)):
                moves[i] = i/1e+1

            print(moves)

            if np.argmax(moves) == 0:
                presskeys.w()
            elif np.argmax(moves) == 1:
                presskeys.a()
            elif np.argmax(moves) == 2:
                presskeys.s()
            elif np.argmax(moves) == 3:
                presskeys.d()
            elif np.argmax(moves) == 4:
                presskeys.wa()
            elif np.argmax(moves) == 5:
                presskeys.wd()
            elif np.argmax(moves) == 6:
                presskeys.sa()
            elif np.argmax(moves) == 7:
                presskeys.sd()
            elif np.argmax(moves) == 8:
                presskeys.w()
            else:
                print("No matches")

        keys = key_check()

        if "T" in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                time.sleep(1)

main()
