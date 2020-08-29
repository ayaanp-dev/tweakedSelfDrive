import numpy as np
import cv2
#from getkeys import key_check
from getscreen import get_screen
import os
import time
import keyboard

def keys_to_output():

    w = [1,0,0,0,0,0,0,0,0]
    a = [0,1,0,0,0,0,0,0,0]
    s = [0,0,1,0,0,0,0,0,0]
    d = [0,0,0,1,0,0,0,0,0]
    wa = [0,0,0,0,1,0,0,0,0]
    wd = [0,0,0,0,0,1,0,0,0]
    sa = [0,0,0,0,0,0,1,0,0]
    sd = [0,0,0,0,0,0,0,1,0]
    nk = [0,0,0,0,0,0,0,0,1]
    
    output = [0,0,0,0,0,0,0,0,0]

    if keyboard.is_pressed("w"):
        output = w
    elif keyboard.is_pressed("a"):
        output = a
    elif keyboard.is_pressed("s"):
        output = s
    elif keyboard.is_pressed("d"):
        output = d
    elif keyboard.is_pressed("w") and keyboard.is_pressed("a"):
        output = wa
    elif keyboard.is_pressed("w") and keyboard.is_pressed("d"):
        output = wd
    elif keyboard.is_pressed("s") and keyboard.is_pressed("a"):
        output = sa
    elif keyboard.is_pressed("s") and keyboard.is_pressed("d"):
        output = sd
    else:
        output = nk

    return output

file_name = "training_data.npy"

if os.path.isfile(file_name):
    print("File exists, loading previous data!")
    training_data = list(np.load(file_name, allow_pickle=True))
else:
    print("No file found, starting fresh!")
    training_data = []

def main():
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
        
    while(True):
        screen = get_screen(region=(0,40,800,600))
        last_time = time.time()
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        screen = cv2.resize(screen, (80,60))
        output = keys_to_output()
        training_data.append([screen, output])
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        if len(training_data) % 500 == 0:
            print(len(training_data))
            np.save(file_name,training_data)

main()
