# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:01:29 2019

@author: BSWOOD9321
"""

import numpy as np
import matplotlib.pyplot as plt

h=.01
m=int(input('Enter a mass: '))
y1=[]
v0=int(input('Enter a starting velocity: '))
k=int(input('Enter a spring constant: '))
p=int(input('Enter an even p-value between 2-12: '))
y1.append(v0)
i=0
t=[0]
