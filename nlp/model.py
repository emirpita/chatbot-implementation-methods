from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import Adam
import numpy as np
from training_data_creation import data_creator


def model_builder():
    data_creator()
    x = np.load('test-train-data/x_train.npy')
    y = np.load('test-train-data/y_train.npy')
    model = Sequential()
    model.add(Dense(32, input_shape=(len(x[0]),), activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.3))
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.3))
    model.add(Dense(len(y[0]), activation='softmax'))

    adam = Adam(lr=0.001)
    model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])
    return model, x, y
