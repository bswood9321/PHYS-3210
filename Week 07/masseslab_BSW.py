# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 21:03:25 2019

@author: Brandon
"""

import numpy as np
import numpy.linalg as la

def Jac(Ls,X):
    J=np.zeros((9,9))
    J[0,1]=J[1,0]=Ls[0]
    J[0,3]=J[1,2]=Ls[1]
    J[0,5]=Ls[2]
    J[1,4]=-Ls[2]
    
    J[2,0]=2*X[0]
    J[2,1]=2*X[1]
    J[3,2]=2*X[2]
    J[3,3]=2*X[3]
    J[4,4]=2*X[4]
    J[4,5]=2*X[5]
    
    J[5,0]=J[6,1]=X[6]
    J[5,2]=J[6,3]=-X[7]
    J[5,6]=X[0]
    J[5,7]=-X[2]
    J[6,6]=X[1]
    J[6,7]=-X[3]
    
    J[7,2]=J[8,3]=X[7]
    J[7,4]=X[8]
    J[7,5]=-X[8]
    
    J[7,7]=X[2]
    J[7,8]=X[4]
    J[8,7]=X[3]
    J[8,8]=-X[5]
    
    return J

def Function(L,Ls,W,X):
    f = np.empty((9, 1))
    
    f[0] = Ls[0]*X[1] + Ls[1]*X[3] + Ls[2]*X[5] - L
    f[1] = Ls[0]*X[0] + Ls[1]*X[2] - Ls[2]*X[4]
    f[2] = X[0]**2 + X[1]**2 - 1.0
    f[3] = X[2]**2 + X[3]**2 - 1.0
    f[4] = X[4]**2 + X[5]**2 - 1.0
    f[5] = X[6]*X[0] - X[7]*X[2] - W[0]
    f[6] = X[6]*X[1] - X[7]*X[3]
    f[7] = X[7]*X[2] + X[8]*X[4] - W[1]
    f[8] = X[7]*X[3] - X[8]*X[5]
    
    return f

def Angles(X):
    angles = np.zeros((3, 1))
    
    angles[0] = np.arcsin(X[0])*180./np.pi
    angles[1] = np.arcsin(X[2])*180./np.pi
    angles[2] = np.arcsin(X[4])*180./np.pi
    
    return angles

def chkchange(dX):
    tol = 1.0e-8
    if abs(dX[0]) < tol and abs(dX[1]) < tol and abs(dX[2]) < tol and \
       abs(dX[3]) < tol and abs(dX[4]) < tol and abs(dX[5]) < tol and \
       abs(dX[6]) < tol and abs(dX[7]) < tol and abs(dX[8]) < tol:
        small_change = True
    else:
        small_change = False
    
    return small_change

def Initial():
    return np.zeros((9,1))+1.0

X=Initial()
W=[10.0,20.0]
Ls=[3.0,4.0,4.0]
L=8.0

for n in range(100):
    f=Function(L,Ls,W,X)
    
    J = Jac(Ls,X)
    
    dX = np.dot(-1.0*la.inv(J), f)
    
    X+= dX
    
    solved = chkchange(dX)
    if solved:
        break
    else:
        continue
    
print("Changes after {:03.0f} iterations:".format(n))
print(dX)
print("Final Parameters:")
print(X)
print("Angles:")
print(calcAngles(X))
    