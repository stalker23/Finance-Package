#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 11:30:39 2017

@author: eddieball
"""
import matplotlib.pyplot as plt
import numpy as np # loadtxt
import pandas as pd
from Moving_Average import MovingAverage

n       = 10
data    = pd.read_csv("shareprices.csv",header='infer')
X       = np.asarray(data.values).T.tolist()[1:-1]

MA = MovingAverage(n,X)

plt.figure(1)
for i in range(0,10):
    plt.plot(MA[i][n-1:],label=list(data)[i+1])
plt.legend()
plt.show()