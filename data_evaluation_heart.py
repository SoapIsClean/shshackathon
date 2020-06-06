#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np # linear algebra
import pandas as pd # data processing
import h5py
import math
from lightgbm import LGBMRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


# In[6]:


with h5py.File("D:/shs_6.6_hackathon/training_data.h5py", "r") as f:
    x =  f['values'][:]
    y = f['labels'][:]
train_x = x[:3000]
val_x = x[3000:]
train_y = y[:3000]
val_y = y[3000:]


# In[9]:


def evaluate(x_train, x_eval, y_train, y_eval, model):
    model.fit(x_train, y_train)
    y_predict = model.predict(x_eval)
    return math.sqrt(mean_squared_error(y_predict, y_eval))
root_path = "C:/users/ryan/Downloads/"
# Read data
x_load = pd.read_csv(root_path + 'Training_values.csv')
y_load = pd.read_csv(root_path + 'Training_labels.csv')
df_X_test  = pd.read_csv(root_path + 'Test_values.csv')

df_X_train = x_load[:3000]
df_Y_train = y_load[:3000]

x_test_final = x_load[3000:]
y_test_final = y_load[3000:]

df_X_train.describe()

# Split training data , Evaluate model , Tune hyper-parameters
X_train, X_test, y_train, y_test = train_test_split(train_x, train_y, test_size=0.2, random_state=1)

from scipy.stats import randint as sp_randint
from scipy.stats import uniform as sp_uniform
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV

model = LGBMRegressor(n_estimators=2000, learning_rate=0.05, num_leaves=30, n_jobs=-5)
rmse = evaluate(X_train, X_test, y_train, y_test, model)
print ('LGBMRegressor RMSE :', rmse)


# In[8]:


def predict_result(data):
    return model.predict_result(np.expand_dims(data, axis = 1))

