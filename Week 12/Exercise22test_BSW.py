# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 09:59:51 2019

@author: BSWOOD9321
"""

import numpy as np
import matplotlib.pyplot as plt

def potential(x,a):
    if np.abs(x) <=a:
        V0=-83.0
    else:
        V0=0.0
    return V0

def wavefout(x,K):
    psi=np.exp(-K*np.abs(x))
    dpsi=-np.sign(x)*K*np.exp(-K*np.abs(x))
    return psi,dpsi

def solvepsi(dx,x_l,x_r,a,E):
    q=0.0483
    K2=-q*E
    Ka=np.sqrt(K2)
    xs=[x_l]
    psi=[np.exp(-Ka*np.abs(xs[-1]))]
    dpsi=[-np.sign(xs[-1])*ka*np.exp(-ka*np.abs(xs[-1]))]
    for n in range(int((x_r-x_l)/dx)):
        x=xs[-1]
        if np.abs(x)>a:
            dpsi_n=dpsi[-1]+K2*psi[-1]*dx
            psi_n=psi[-1]+dpsi[-1]*dx
        else:
            dpsi_n=dpsi[-1]+(q*potential())