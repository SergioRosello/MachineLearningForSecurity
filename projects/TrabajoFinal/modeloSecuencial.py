# -*- coding: utf-8 -*-
"""
Original file is located at
    https://colab.research.google.com/drive/1VA1VbhrrcnQq5X26GbXmaTWM8NtZ5EgX

Vamos a cambiar los datos, para que ip.src tenga valor, para que no se quede el campo vacio.
"""

from pandas import read_csv

data = read_csv('./isot_app_and_botnet_dataset/sorted_merged_traffic.csv', header=0,
                dtype={'frame.time_epoch': float,
                       'ip.src': str,
                       'ip.dst': str,
                       '_ws.col.Protocol': str,
                       'frame.len': str,
                       '_ws.col.Info': str,
                       'Botnet': str})
print("Data head:")
print(data.head())

"""
Vamos a obtener un sample del dataset, para no cargar con el archivo enorme
"""

import pandas as pd
data = data.sample(frac=.0001)

# retrieve numpy array
dataset = data.values
# split into input (X) and output (y) variables
X = dataset[:, 1:-1]
y = dataset[:,-1]
# format all fields as string 
X = X.astype(str)
# reshape target to be a 2d array
y = y.reshape((len(y), 1)) 


def prepare_input(X):
    ct = ColumnTransformer(
      [('oh_enc', OneHotEncoder(sparse=False), [0, 1, 2, 4]),],  # the column numbers I want to apply this to
      remainder='passthrough'  # This leaves the rest of my columns in place
    )
    X_transformed = ct.fit_transform(X)
    normalized_X = preprocessing.normalize(X_transformed[:, [-1]], axis=0)
    X_enc = np.append(X_transformed[:, 0:-1], normalized_X, axis=1)
    return X_enc
  
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

X = prepare_input(X)

"""Entrenamos los datos, de esta forma, tenemos las variables que necesitamos para mas adelante."""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

# prepare target
def prepare_targets(y_train, y_test):
	le = LabelEncoder()
	le.fit(y_train)
	y_train_enc = le.transform(y_train)
	y_test_enc = le.transform(y_test)
	return y_train_enc, y_test_enc

from sklearn.preprocessing import LabelEncoder
y_train_enc, y_test_enc = prepare_targets(y_train.ravel(), y_test.ravel())

"""Model creation phase"""

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
# Input layer
# 32 neurons
# input_shape 16
    # To specify the data structure the neural network data will be sent to the model
# Relu activation
# 
model.add(Dense(32, input_dim=X_train.shape[1], activation='relu', kernel_initializer='he_normal'))
model.add(Dense(1, activation='sigmoid'))

model.summary()

"""Model Training and Evaluation phase"""

# compile the keras model
print("Compiling the Keras model")
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
print("Fitting the Keras model")
model.fit(X_train, y_train, epochs=10, batch_size=16, verbose=2)

from keras.utils import print_summary
print_summary(model)

# evaluate the keras model
print("evaluating the Keras model")
_, accuracy = model.evaluate(X_test, y_test, verbose=0)
print('Accuracy: %.2f' % (accuracy*100))

# Save the model to disk
model.save('modeloSecuencial.h5')
print("Model saved to disk")
