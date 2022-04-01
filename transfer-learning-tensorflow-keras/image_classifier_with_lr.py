# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 17:10:32 2022

@author: ARMAN
"""

#%%1.kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#%%2.veri onisleme
#2.1.veri yukleme

train_dir = 'veriseti/train'
validation_dir = 'veriseti/val'
test_dir = 'veriseti/test'
x_train = train_dir
y_train = train_dir
x_test = test_dir
y_test = test_dir

from sklearn.preprocessing import StandardScaler

scalers = {}
for i in range(x_train.shape[1]):
    scalers[i] = StandardScaler()
    x_train[:, i, :] = scalers[i].fit_transform(x_train[:, i, :]) 

for i in range(x_test.shape[1]):
    x_test[:, i, :] = scalers[i].transform(x_test[:, i, :]) 

from sklearn.linear_model import LogisticRegression
logr = LogisticRegression(random_state=0)
logr.fit(X_train,y_train)

y_pred = logr.predict(X_test)
print(y_pred)
print(y_test)





