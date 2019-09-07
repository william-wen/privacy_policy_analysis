#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 14:39:31 2019

@author: willwen
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import tree
from sklearn.linear_model import LinearRegression

# Create Dataset
np.random.seed(0)
x = 2 - 3 * np.random.normal(0, 1, 20)
y = x - 2 * (x ** 2) + 0.5 * (x ** 3) + np.random.normal(-3, 3, 20)
# plt.scatter(x,y, s=10)
# plt.show()

# transforming data to include another axis
x = x[:, np.newaxis]
y = y[:, np.newaxis]

model = LinearRegression()
model.fit(x,y)
# Makes the Line
# Same X's, different Y's
y_pred = model.predict(x)

# Plot Scatter
plt.scatter(x, y, s=10)
# Plot Line 
plt.plot(x, y_pred, color='r')
plt.show()

