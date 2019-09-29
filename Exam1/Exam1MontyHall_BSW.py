# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 21:17:32 2019

@author: Brandon
"""
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rand


Winsonfirstpick=[]
Winsonsecondpick=[]
i = 1
while i<=1000000:
    Door1, Door2, Door3 = False, False, False
    D= rand.randint(1,4)
    if D==1:
        Door1=True
    elif D==2:
        Door2=True
    else:
        Door3=True
    Doors=[Door1,Door2,Door3]
    A=rand.randint(0,3)
    Playerschoice=Doors[A]
    if Playerschoice:
        Winsonfirstpick.append(1)    
    i=i+1
    
Totalwins=np.sum(Winsonfirstpick)

print("The odds of winning when the player stands pat are: ",Totalwins/1000000)

j=1
while j<=1000000:
    Door1, Door2, Door3=False, False, False
    D= rand.randint(1,4)
    if D==1:
        Door1=True
    elif D==2:
        Door2=True
    else:
        Door3=True
    Doors=[Door1,Door2,Door3]
    A=rand.randint(0,3)
    B=A-1
    C=B-1
    Playerschoice=Doors[A]
    Otherdoor1=Doors[B]
    Otherdoor2=Doors[C]
    if Playerschoice:
        Playerschoice=False #Because the player is ALWAYS choosing the other option, if they chose the winner first, they have to choose a losing door        
    if Otherdoor1:#Because if the player chose a loser 1st, and they are always changing after being shown the other loser, they will have to choose the winner
        Playerschoice=Otherdoor1
    if Otherdoor2:
        Playerschoice=Otherdoor2
    if Playerschoice:
        Winsonsecondpick.append(1)
    j=j+1

Totalwins2=np.sum(Winsonsecondpick)

print("The odds of winning when the player always chooses the second option are: ", Totalwins2/1000000)    
    