import tensorflow as tf  
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam
import numpy as np 
from random import shuffle

def conv(width, height, lr):
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(None, width, height, 1)))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    model.add(Dense(4))

    model.compile(optimizer=Adam(lr=lr, decay=1e-6, epsilon=0.1),
                  loss="categorical_crossentropy",
                  metrics=['accuracy'])

    return model

def xception(width, height, lr):
    model = Sequential([
        Conv2D(32, 3, activation="relu", input_shape=(width, height, 1), padding="same"),
        Conv2D(64, 3, activation="relu", padding="same"),
        Conv2D(128, 3, padding="same"),
        Conv2D(128, 3, activation="relu", padding="same"),
        MaxPooling2D(3, 2),
        Conv2D(256, 3, activation="relu", padding="same"),
        Conv2D(256, 3, activation="relu", padding="same"),
        MaxPooling2D(3, 2),
        Conv2D(728, 3, activation="relu", padding="same"),
        Conv2D(728, 3, activation="relu", padding="same"),
        MaxPooling2D(3, 2),
        Conv2D(728, 3, activation="relu", padding="same"),
        Conv2D(728, 3, activation="relu", padding="same"),
        Conv2D(728, 3, activation="relu", padding="same"),
        Conv2D(728, 3, activation="relu", padding="same"),
        Conv2D(1024, 3, activation="relu", padding="same"),
        MaxPooling2D(3, 2),
        Conv2D(1536, 3, activation="relu", padding="same"),
        Conv2D(4, 3, activation="relu", padding="same"),
        GlobalAveragePooling2D(),
        ])

    model.compile(optimizer=Adam(lr=lr, decay=1e-6),
              loss="categorical_crossentropy",
              metrics=['accuracy'])
    return model

