# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 23:49:01 2019

@author: Brandon
"""

import numpy as np
import matplotlib.pyplot as plt
i=1
theta1=np.pi/8
while i<=4:
    theta=theta1
    w=0
    l=2
    g=9.82
    t=0
    m=5
    dt=.01
    THETA=[theta]
    W=[w]
    T=[t]
    X=[l*np.sin(theta)]
    Y=[l-l*np.cos(theta)]
    findT=[]
    while t<=10:
        x=l*np.sin(theta)
        y=l-l*np.cos(theta)
        f=-m*g*np.sin(theta)
        w=w+(f/m)*dt
        theta = theta+w*dt
        t=t+dt
        T.append(t)
        X.append(x)
        Y.append(y)
        THETA.append(theta)
        W.append(w)

    print('Starting angle: ',theta1)
    theta1=theta1+np.pi/8
    i=i+1
    
    plt.plot(T,X,label='x')
    plt.plot(T,W,label='w')
    plt.plot(T,THETA,label='angle')
    plt.plot(T,Y,label='y')
    plt.legend(loc=(1.04,0))
    plt.show()
    
    plt.plot(X,Y)
    plt.title('Pendulum position in X,Y plane')
    plt.show()
    
    plt.plot(THETA,W)
    plt.title('Pendulum angle vs. angular speed')
    plt.xlabel('Angle')
    plt.ylabel('W')
    plt.show()

    print('The theoretical Tau is: ',2*np.pi*np.sqrt((l/g)))
    print('------------------------------------------------')
    
    
    
print('The X,Y plot makes sense because it is basically plotting a visualization of the pendulum swinging '
      'back and forth in front of a viewer.')

print('The angle vs. angular velocity graph also makes sense, as we see the angular velocity is at its max '
      'when the pendulum is at the lowest point (an angle of zero), while moving towards the positive theta '
      'and is at its min when the pendulum is at its lowest, and moving towards the negative theta values.')    