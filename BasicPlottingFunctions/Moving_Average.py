#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 16:18:57 2017

@author: eddieball
"""

def MovingAverage(n,X):
    # n = number of days to average over
    # X = Data to take moving average of
    
    num_stocks = len(X) #number of stocks minus 1
    MA = [[] for x in range(num_stocks)]  # moving average list
    # Pad MA with n zeros
    for i in range(1,num_stocks):
        for j in range(0,n):
            X[i].insert(0,0)
          
    for i in range(0,num_stocks):
        for j in range(n,len(X[i])):
            n_sum = 0
            for k in range(0,n):
                n_sum = n_sum + X[i][j-k]
            MA[i].append(n_sum/n) 
    return MA