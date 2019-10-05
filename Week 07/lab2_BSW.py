
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
L1,L2,L3=3,4,4
W1, W2 = 10,20
th1, th2, th3=30,45,45
T1,T2,T3=1,1,1

J=np.array([[0,0,0,L1,L2,L3,0,0,0],[L1,L2,-L3,0,0,0,0,0,0],[T1,T2,0,0,0,0,np.sin(th1),-np.sin(th2),0]])