# -*- coding: utf-8 -*-
"""Electrical_Energy_Output.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15tNhmFhGvFtAepXymIHOy7lrP_E37ni-
"""

import numpy as np
import pandas as pd
import tensorflow as tf

dataset = pd.read_excel('Folds5x2_pp.xlsx')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2)

ann = tf.keras.models.Sequential()

ann.add(tf.keras.layers.Dense(units = 6,activation='relu'))

ann.add(tf.keras.layers.Dense(units=6,activation='relu'))

ann.add(tf.keras.layers.Dense(units=1))

ann.compile(optimizer = 'adam', loss = 'mean_squared_error')

ann.fit(X_train,Y_train,batch_size = 32,epochs = 100)

y_pred = ann.predict(X_test)
np.set_printoptions(precision = 0)
print(np.concatenate((y_pred.reshape(len(y_pred),1), Y_test.reshape(len(Y_test),1)),1))