import numpy as np
from mymodels import xception, conv
from tensorflow.keras.callbacks import TensorBoard

tensorboard = TensorBoard(log_dir="logs/", profile_batch=0)

WIDTH = 160
HEIGHT = 120
LR = 1e-4
EPOCHS = 1000
MODEL_NAME = "xception2_net"

model = xception(WIDTH, HEIGHT, LR)

for i in range(EPOCHS):
    train_data = np.load('trainingdata/balanced_training_data.npy', allow_pickle=True)

    train = train_data[:-100]
    test = train_data[-100:]

    X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
    Y = np.array([i[1] for i in train])

    test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
    test_y = np.array([i[1] for i in test])

    model.fit(X, Y, batch_size=10, validation_data=(test_x, test_y), callbacks=[tensorboard])
    model.save(MODEL_NAME)
