import numpy as np
from PIL import ImageGrab
import cv2
import time

def get_screen(region): 
    screen = np.array(ImageGrab.grab(bbox=region))
    return screen
