# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt



N = int(input("Pick a number: "))

n, a, sum1, m, b, sum2 = 1, 0, 0, N, 0, 0


while (n<=N):
    a = 1/n
    sum1+=a
    n = n+1
    
while (m>=1):
    b = 1/m
    sum2+=b
    m = m-1
    
ploteq = (sum1 - sum2)/(np.absolute(sum1)+np.absolute(sum2))
print(N, ploteq)

