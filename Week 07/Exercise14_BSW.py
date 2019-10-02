# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 10:02:52 2019

@author: BSWOOD9321
"""
import numpy as np
import numpy.linalg as la

A=np.array([[4,-2,1],[3,6,-4],[2,1,8]])

Ainv=la.inv(A)

print("A: ",A)
print("Ainv: ",Ainv)



print("A*Ainv: ",A*Ainv)

print("Ainv*A: ",Ainv*A)

Ainvtest=np.array([[52,17,2],[-32,30,19],[-9,-8,30]])
print("Analytical result: ",(1/263)*Ainvtest)

Ae=np.array([[-2,2,-3],[2,1,-6],[-1,-2,0]])
Aee=la.eig(Ae)
print(Aee)