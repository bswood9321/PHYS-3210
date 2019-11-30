# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 22:17:26 2019

@author: Brandon
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 



e0=8.8541878128e-12
echarge=1.60217662e-19
hbar=1.0545718e-34
me=9.10938356e-31
a0=5.29177210903e-11
c=299792458
h=6.6260693e-34

def r(n):
    rn=(4*np.pi*e0*(hbar**2)*n**2)/(me*(echarge**2))
    return rn/a0

def v(n):
    vn=hbar/(me*a0*n)
    return vn

def p(n):
    pn=hbar/(a0*n)
    return pn/1e-24

def E(n):
    En=-((me*(echarge**4))/(32*(np.pi**2)*(e0**2)*(hbar**2)))*(1/(n**2))
    En=En*6.242e18
    return En

def delE(m,n):
    delE=np.absolute(E(m)-E(n))
    return delE

def photonwavel(delE):
    l=h*c/(delE*1.60218e-19)
    return l

def photonfreq(l):
    f=c/l
    return f

def Zr(z,n):
    Zr=(4*np.pi*e0*(hbar**2)*n**2)/(me*z*(echarge**2))
    return Zr

def Ze(z,n):
    Zn=-((me*(z**2)*(echarge**4))/(32*(np.pi**2)*(e0**2)*(hbar**2)))*(1/(n**2))
    Zn=Zn*6.242e18
    return Zn

def delZe(z,m,n):
    delZe=np.absolute(Ze(z,m)-Ze(z,n))
    return delZe



def prob_1s(x,y,z):
    r=np.sqrt(np.square(x)+np.square(y)+np.square(z))
    return np.square((2/(np.sqrt(np.pi)))*np.e**(-r))

x=np.linspace(-5,5,30)
y=np.linspace(-5,5,30)
z=np.linspace(-5,5,30)
elements = []
probability = []
for ix in x:
    for iy in y:
        for iz in z:
            elements.append(str((ix,iy,iz)))
            probability.append(prob_1s(ix,iy,iz))
            

probability = probability/sum(probability)

coord = np.random.choice(elements, size=100000, replace=True, p=probability)
elem_mat = [i.split(',') for i in coord]
elem_mat = np.matrix(elem_mat)
x_coords = [float(i.item()[1:]) for i in elem_mat[:,0]] 
y_coords = [float(i.item()) for i in elem_mat[:,1]] 
z_coords = [float(i.item()[0:-1]) for i in elem_mat[:,2]]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_coords, y_coords, z_coords, alpha=0.05)
ax.set_title("Hydrogen 1s density")
plt.show()


def prob_2s(x,y,z):
    r=np.sqrt(np.square(x)+np.square(y)+np.square(z))
    return np.square((1/(4*np.sqrt(2*np.pi))*(2-(r))*np.e**(-r/2)))

x=np.linspace(-10,10,30)
y=np.linspace(-10,10,30)
z=np.linspace(-10,10,30)
elements = []
probability = []
for ix in x:
    for iy in y:
        for iz in z:
            elements.append(str((ix,iy,iz)))
            probability.append(prob_2s(ix,iy,iz))
            

probability = probability/sum(probability)

coord = np.random.choice(elements, size=100000, replace=True, p=probability)
elem_mat = [i.split(',') for i in coord]
elem_mat = np.matrix(elem_mat)
x_coords = [float(i.item()[1:]) for i in elem_mat[:,0]] 
y_coords = [float(i.item()) for i in elem_mat[:,1]] 
z_coords = [float(i.item()[0:-1]) for i in elem_mat[:,2]]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_coords, y_coords, z_coords, alpha=0.05)
ax.set_title("Hydrogen 2s density")
plt.show()


def prob_2p(x,y,z):
    r=np.sqrt(np.square(x)+np.square(y)+np.square(z))
    phi=np.arctan(y/x)
    theta=np.arccos(z/r)
    return np.square((1/4)*(1/np.sqrt(2*np.pi))*r*(np.e**(-r))*np.cos(theta))

x=np.linspace(-10,10,30)
y=np.linspace(-10,10,30)
z=np.linspace(-10,10,30)
elements = []
probability = []
for ix in x:
    for iy in y:
        for iz in z:
            elements.append(str((ix,iy,iz)))
            probability.append(prob_2p(ix,iy,iz))
            

probability = probability/sum(probability)

coord = np.random.choice(elements, size=100000, replace=True, p=probability)
elem_mat = [i.split(',') for i in coord]
elem_mat = np.matrix(elem_mat)
x_coords = [float(i.item()[1:]) for i in elem_mat[:,0]] 
y_coords = [float(i.item()) for i in elem_mat[:,1]] 
z_coords = [float(i.item()[0:-1]) for i in elem_mat[:,2]]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_coords, y_coords, z_coords, alpha=0.05)
ax.set_title("Hydrogen 2p density")
plt.show()


def prob_3s(x,y,z):
    r=np.sqrt(np.square(x)+np.square(y)+np.square(z))
    phi=np.arctan(y/x)
    theta=np.arccos(z/r)
    return np.square((1/81)*(1/(np.sqrt(3*np.pi)))*(np.e**(-r/3))*(27-(18*r)+(2*r**2)))

x=np.linspace(-15,15,30)
y=np.linspace(-15,15,30)
z=np.linspace(-15,15,30)
elements = []
probability = []
for ix in x:
    for iy in y:
        for iz in z:
            elements.append(str((ix,iy,iz)))
            probability.append(prob_3s(ix,iy,iz))
            

probability = probability/sum(probability)

coord = np.random.choice(elements, size=100000, replace=True, p=probability)
elem_mat = [i.split(',') for i in coord]
elem_mat = np.matrix(elem_mat)
x_coords = [float(i.item()[1:]) for i in elem_mat[:,0]] 
y_coords = [float(i.item()) for i in elem_mat[:,1]] 
z_coords = [float(i.item()[0:-1]) for i in elem_mat[:,2]]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_coords, y_coords, z_coords, alpha=0.05)
ax.set_title("Hydrogen 3s density")
plt.show()


def prob_3p(x,y,z):
    r=np.sqrt(np.square(x)+np.square(y)+np.square(z))
    phi=np.arctan(y/x)
    theta=np.arccos(z/r)
    return np.square((np.sqrt(2)/81)*(1/(np.sqrt(np.pi)))*(np.e**(-r/3))*(6-r))

x=np.linspace(-25,25,30)
y=np.linspace(-25,25,30)
z=np.linspace(-25,25,30)
elements = []
probability = []
for ix in x:
    for iy in y:
        for iz in z:
            elements.append(str((ix,iy,iz)))
            probability.append(prob_3p(ix,iy,iz))
            

probability = probability/sum(probability)

coord = np.random.choice(elements, size=100000, replace=True, p=probability)
elem_mat = [i.split(',') for i in coord]
elem_mat = np.matrix(elem_mat)
x_coords = [float(i.item()[1:]) for i in elem_mat[:,0]] 
y_coords = [float(i.item()) for i in elem_mat[:,1]] 
z_coords = [float(i.item()[0:-1]) for i in elem_mat[:,2]]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_coords, y_coords, z_coords, alpha=0.05)
ax.set_title("Hydrogen 3p density")
plt.show()

def prob_3d(x,y,z):
    r=np.sqrt(np.square(x)+np.square(y)+np.square(z))
    phi=np.arctan(y/x)
    theta=np.arccos(z/r)
    return np.square(((r**2)/81)*(1/np.sqrt(6*np.pi))*(np.e**(-r/3))*((3*np.cos(theta)**2)-1))

x=np.linspace(-25,25,30)
y=np.linspace(-25,25,30)
z=np.linspace(-25,25,30)
elements = []
probability = []
for ix in x:
    for iy in y:
        for iz in z:
            elements.append(str((ix,iy,iz)))
            probability.append(prob_3d(ix,iy,iz))
            

probability = probability/sum(probability)

coord = np.random.choice(elements, size=100000, replace=True, p=probability)
elem_mat = [i.split(',') for i in coord]
elem_mat = np.matrix(elem_mat)
x_coords = [float(i.item()[1:]) for i in elem_mat[:,0]] 
y_coords = [float(i.item()) for i in elem_mat[:,1]] 
z_coords = [float(i.item()[0:-1]) for i in elem_mat[:,2]]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_coords, y_coords, z_coords, alpha=0.05)
ax.set_title("Hydrogen 3d density")
plt.show()


n=1
Es=[]
radii=[]
Vs=[]
Ps=[]
while n<=10:
    e=E(n)
    rs=r(n)
    vs=v(n)
    ps=p(n)
    radii.append([rs,rs])
    Es.append([e,e])
    Vs.append([vs,vs])
    Ps.append([ps,ps])
    n=n+1



x=[1,2]
plt.figure(figsize=(1.5,6))
plt.plot(x,Es[0],'k')
plt.plot(x,Es[1],'k')
plt.plot(x,Es[2],'k')
plt.plot(x,Es[3],'k')
plt.plot(x,Es[4],'k')
plt.plot(x,Es[5],'k')
plt.plot(x,Es[6],'k')
plt.plot(x,Es[7],'k')
plt.plot(x,Es[8],'k')
plt.plot(x,Es[9],'k')
plt.xlim(1.1,1.9)
plt.yticks([-13.6, -3.4, -1.5, -.85, -.2],('n=1, -13.6eV','n=2, -3.4eV','n=3, -1.5eV','n=4,0.85eV','n=5+'))
plt.xticks([])
plt.title('Energy Levels of a Hydrogen Atom electron')
plt.show()


plt.figure(figsize=(1.5,6))
plt.plot(x,radii[0],'k')
plt.plot(x,radii[1],'k')
plt.plot(x,radii[2],'k')
plt.plot(x,radii[3],'k')
plt.plot(x,radii[4],'k')
plt.plot(x,radii[5],'k')
plt.plot(x,radii[6],'k')
plt.plot(x,radii[7],'k')
plt.plot(x,radii[8],'k')
plt.plot(x,radii[9],'k')
plt.xlim(1.1,1.9)
plt.yticks([1,4,8,16,25,36,49,64,81,100])
plt.xticks([])
plt.title('Quantized Radii of electron [Bohr radii]')
plt.show()

plt.figure(figsize=(1.5,6))
plt.plot(x,Vs[0],'k')
plt.plot(x,Vs[1],'k')
plt.plot(x,Vs[2],'k')
plt.plot(x,Vs[3],'k')
plt.plot(x,Vs[4],'k')
plt.plot(x,Vs[5],'k')
plt.plot(x,Vs[6],'k')
plt.plot(x,Vs[7],'k')
plt.plot(x,Vs[8],'k')
plt.plot(x,Vs[9],'k')
plt.xlim(1.1,1.9)
plt.yticks([2.2e6,1.1e6,7.3e5,5.5e5,4.4e5,3.6e5],('2.2e6','1.1e6','7.3e5','5.5e5','4.4e5','n=6+'))
plt.xticks([])
plt.title('Quantized Velocity of electron [m/s]')
plt.show()

plt.figure(figsize=(1.5,6))
plt.plot(x,Ps[0],'k')
plt.plot(x,Ps[1],'k')
plt.plot(x,Ps[2],'k')
plt.plot(x,Ps[3],'k')
plt.plot(x,Ps[4],'k')
plt.plot(x,Ps[5],'k')
plt.plot(x,Ps[6],'k')
plt.plot(x,Ps[7],'k')
plt.plot(x,Ps[8],'k')
plt.plot(x,Ps[9],'k')
plt.xlim(1.1,1.9)
plt.yticks([2,1,.66,.5,.4,.33],('2','1','.66','.5','.4','n=6+'))
plt.xticks([])
plt.title('Quantized momenta of electron [e-24 kg.m/s]')
plt.show()

zs=2

ZEs=[]
while zs<=5:
    zes=Ze(zs,1)
    ZEs.append([zes,zes])
    zs=zs+1
    
plt.figure(figsize=(1.5,6))
plt.plot(x,ZEs[0])
plt.plot(x,ZEs[1])
plt.plot(x,ZEs[2])
plt.plot(x,ZEs[3])
plt.xlim(1.1,1.9)
plt.yticks([-54.43,-122.46,-217.71,-340.17],('He(-54.43Ev)','Li(-122.46eV)','Be(-217.71eV)','B(-340.17eV)'))
plt.xticks([])
plt.title('Ionizing Energy of ground state electron for Z=2-5')
plt.show() 


m,n=10,2

BalmerphotonE=[]
Balmerphotonwavelength=[]

while m>n:
    BPE=delE(m,n)
    BPW=photonwavel(BPE)
    BPWref=BPW/1e-9
    BalmerphotonE.append(BPE)
    Balmerphotonwavelength.append([BPWref,BPWref])
    m=m-1
    
plt.figure(figsize=(15,1.5))
ax=plt.axes()
ax.set_facecolor('black')
plt.plot(Balmerphotonwavelength[0],x, color='indigo')
plt.plot(Balmerphotonwavelength[1],x, color='indigo')
plt.plot(Balmerphotonwavelength[2],x, color='indigo')
plt.plot(Balmerphotonwavelength[3],x, color='indigo')
plt.plot(Balmerphotonwavelength[4],x, color='purple')
plt.plot(Balmerphotonwavelength[5],x, color='blue')
plt.plot(Balmerphotonwavelength[6],x, color='green')
plt.plot(Balmerphotonwavelength[7],x, color='red')
plt.ylim(1.1,1.9)
plt.xticks([396,410,434,485,656],('<---UV','410nm','434nm','486nm','656nm'))
plt.title('Balmer series Hydrogen Emission Spectrum')
plt.yticks([])
plt.show()


    
    
    
    
    
    
    
    