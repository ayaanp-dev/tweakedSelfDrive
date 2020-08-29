import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Activation, MaxPooling2D, Flatten, Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.optimizers import Adam
import numpy as np
from random import shuffle


def conv(width, height, lr):
	model = Sequential()
	model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(width, height, 1)))
	model.add(MaxPooling2D((2, 2)))
	model.add(Conv2D(64, (3, 3), activation='relu'))
	model.add(MaxPooling2D((2, 2)))
	model.add(Conv2D(64, (3, 3), activation='relu'))
	model.add(Flatten()),
	model.add(Dense(64, activation='relu')),
	model.add(Dropout(0.5))
	model.add(Dense(9, activation="softmax"))

	model.compile(optimizer=Adam(lr=lr, decay=1e-6),
				  loss="categorical_crossentropy",
				  metrics=['accuracy'])

	return model


def xception(width, height, lr):
	model = Sequential([
		Conv2D(32, 3, activation="relu", input_shape=(width, height, 3), padding="same"),
		Conv2D(64, 3, activation="relu", padding="same"),
		Conv2D(128, 3, padding="same"),
		Conv2D(128, 3, activation="relu", padding="same"),
		MaxPooling2D(3, 2, padding="same"),
		Conv2D(256, 3, activation="relu", padding="same"),
		Conv2D(256, 3, activation="relu", padding="same"),
		MaxPooling2D(3, 2, padding="same"),
		Conv2D(728, 3, activation="relu", padding="same"),
		Conv2D(728, 3, activation="relu", padding="same"),
		MaxPooling2D(3, 2, padding="same"),
		Conv2D(728, 3, activation="relu", padding="same"),
		Conv2D(728, 3, activation="relu", padding="same"),
		Conv2D(728, 3, activation="relu", padding="same"),
		Conv2D(728, 3, activation="relu", padding="same"),
		Conv2D(1024, 3, activation="relu", padding="same"),
		MaxPooling2D(3, 2, padding="same"),
		Conv2D(1536, 3, activation="relu", padding="same"),
		Conv2D(2048, 3, activation="relu", padding="same"),
		GlobalAveragePooling2D(),
		Dense(4096, activation="relu"),
		Dense(9, activation="softmax")
	])

	model.compile(optimizer=Adam(lr=lr, decay=1e-6),
				  loss="categorical_crossentropy",
				  metrics=['accuracy'])

	return model


# def alexnet(width, height, lr):
# 	model = Sequential([
# 		Conv2D(96, 11, activation="relu", input_shape=(width, height, 1), padding="same"),
# 		MaxPooling2D(3, 2),
# 		Conv2D(256, 5, activation="relu", padding="same"),
# 		MaxPooling2D(3, 2),
# 	])
# 		self.add(Conv2D(96, kernel_size=(11, 11), strides=4,
# 						padding='valid', activation='relu',
# 						input_shape=(width, height, 1),
# 						kernel_initializer='he_normal'))
#
# 		self.add(MaxPooling2D(3, 2, padding="valid"))
#
# 		self.add(Conv2D(256, kernel_size=(5, 5), strides=1,
# 						padding='same', activation='relu',
# 						kernel_initializer='he_normal'))
#
# 		self.add(MaxPooling2D(3, 2, padding="valid"))
#
# 		self.add(Conv2D(384, kernel_size=(3, 3), strides=1,
# 						padding='same', activation='relu',
# 						kernel_initializer='he_normal'))
#
# 		self.add(Conv2D(384, kernel_size=(3, 3), strides=1,
# 						padding='same', activation='relu',
# 						kernel_initializer='he_normal'))
#
# 		self.add(Conv2D(256, kernel_size=(3, 3), strides=1,
# 						padding='same', activation='relu',
# 						kernel_initializer='he_normal'))
#
# 		self.add(MaxPooling2D(3, 2, padding="valid"))
#
# 		self.add(Flatten())
# 		self.add(Dense(4096, activation='relu'))
# 		self.add(Dense(4096, activation='relu'))
# 		self.add(Dense(1000, activation='relu'))
# 		self.add(Dense(9, activation='softmax'))
#
# 		self.compile(optimizer=tf.keras.optimizers.Adam(lr),
# 					 loss='categorical_crossentropy',
# 					 metrics=['accuracy'])
