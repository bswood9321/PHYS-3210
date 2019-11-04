# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:01:07 2019

@author: BSWOOD9321
"""

import numpy as np
import matplotlib.pyplot as plt

m=.511
hbar=6.582e-22

def psi(x,K):
    if x<0:
        psi=np.exp(K*x)
    elif x>0:
        psi=np.exp(-K*x)
    return psi    