# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:25:03 2019

@author: BSWOOD9321
"""

import numpy as np
import matplotlib.pyplot as plt

Rf=np.linspace(1000,10000,1000)
Ri=1000

Vin=10

Vout=-Vin*(Rf/Ri)

plt.plot(Rf,Vout,'r-')
plt.title('Inverted Amp voltage for Rf values')
plt.show()

R2=np.linspace(1000,100000,1000)
R1=1000
Vin=10
Vout=Vin*(1+(R2/R1))

plt.plot(R2,Vout,'r-')
plt.title('Non-inverted Amp')
plt.show()