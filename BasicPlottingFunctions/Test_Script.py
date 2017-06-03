#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 11:30:39 2017

@author: eddieball
"""
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import numpy as np # loadtxt
import pandas as pd
from Moving_Average import MovingAverage

n       = 10
data    = pd.read_csv("shareprices.csv",header='infer',skiprows=1)
X       = np.asarray(data.values).T.tolist()[0:-1] # Transpose dataframe and make list
# sort date from past to present
for i in range(0,len(X)):
    X[i].reverse()

MA = MovingAverage(n,X[1:])
for i in range(0,len(MA)):
    print(len(MA[i]))

fig1 = plt.figure(1)
for i in range(0,len(MA)):
    plt.plot_date(dates.datestr2num(X[0][n-1:]),MA[i][n-1:],'-',label=list(data)[i+1])

plt.xlabel('Date')
plt.ylabel('Price [$]')
plt.title('TSP Funds: ' + str(n) + ' Day Moving Average' )
fig1.autofmt_xdate()
plt.legend(loc=2)
plt.show()
