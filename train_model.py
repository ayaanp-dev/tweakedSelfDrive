from models import conv, xception
import numpy as np
import time
import tensorflow as tf
from tensorflow.keras.callbacks import TensorBoard

tensorboard_cb = TensorBoard(log_dir="logs/", profile_batch=0)

WIDTH = 80
HEIGHT = 60
LEARNING_RATE = 0.001
EPOCHS = 100
BATCH_SIZE = 75
MODEL_NAME = f"SelfDrivingCar-{time.time()}.h5"

model = conv(WIDTH, HEIGHT, LEARNING_RATE)

train_data = np.load("balanced_data.npy", allow_pickle=True)

train = train_data[:-100]
test = train_data[-100:]

x_train = np.array([sample[0] for sample in train], dtype="int32").reshape(-1, WIDTH, HEIGHT, 1)
y_train = np.array([sample[1] for sample in train], dtype="int32")

x_test = np.array([sample[0] for sample in test], dtype="int32").reshape(-1, WIDTH, HEIGHT, 1)
y_test = np.array([sample[1] for sample in test], dtype="int32")

print(x_train)
print(y_train)

model.fit(x_train, y_train, batch_size=BATCH_SIZE, epochs=EPOCHS, steps_per_epoch=len(train) // BATCH_SIZE, validation_data=(x_test, y_test), callbacks=[tensorboard_cb])

model.save(MODEL_NAME)
