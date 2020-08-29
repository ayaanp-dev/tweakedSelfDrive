import numpy as np
import cv2
from getkeys import key_check
from getscreen import get_screen
import presskeys
import os
import time
import tensorflow as tf
from tensorflow.keras.models import load_model

MODEL_NAME = "" #Put trained model file in here

def main():

    model = load_model(f"{MODEL_NAME}.h5")

    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    if not paused:
        while(True):
            screen = get_screen(region=(0,40,800,600))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (80,60))

            moves = model.predict([screen.reshape(-1, 80, 60, 1)])[0]

            if moves[0] > 0.7:
                presskeys.w()
            else:
                moves = np.delete(moves, 0)

                if np.argmax(moves) == 0:
                    presskeys.wa()
                elif np.argmax(moves) == 1:
                    presskeys.s()
                elif np.argmax(moves) == 2:
                    presskeys.wd()
                elif np.argmax(moves) == 3:
                    presskeys.wa()
                elif np.argmax(moves) == 4:
                    presskeys.wd()
                elif np.argmax(moves) == 5:
                    presskeys.sa()
                elif np.argmax(moves) == 6:
                    presskeys.sd()
                elif np.argmax(moves) == 7:
                    # presskeys.w()
                    pass
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
