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


    
    
    
from mpl_toolkits.mplot3d import Axes3D 



n=1
L=1
k=n*np.pi/L
x=0
psi=np.sqrt(2/L)*np.sin(k*x)
dpsi=np.sqrt(2)*k*np.cos(k*x)/np.sqrt(L)
X=[x]
PSI=[0]
P=[psi**2]
dx=1e-5
while x<=L:
    d2psi=-k**2*(np.sqrt(2/L))*np.sin(k*x)
    dpsi=dpsi+d2psi*dx
    psi=psi+dpsi*dx
    x=x+dx
    X.append(x)
    PSI.append(psi)
    P.append((np.sqrt(2/L)*np.sin(k*x))**2)


n=2
L=1
k=n*np.pi/L
x=0
psi=np.sqrt(2/L)*np.sin(k*x)
dpsi=np.sqrt(2)*k*np.cos(k*x)/np.sqrt(L)
PSI2=[0]
P2=[psi**2]
dx=1e-5
while x<=L:
    d2psi=-k**2*(np.sqrt(2/L))*np.sin(k*x)
    dpsi=dpsi+d2psi*dx
    psi=psi+dpsi*dx
    x=x+dx
    PSI2.append(psi+5)
    P2.append(((np.sqrt(2/L)*np.sin(k*x))**2)+5)
    
n=3
L=1
k=n*np.pi/L
x=0
psi=np.sqrt(2/L)*np.sin(k*x)
dpsi=np.sqrt(2)*k*np.cos(k*x)/np.sqrt(L)
PSI3=[0]
P3=[psi**2]
dx=1e-5
while x<=L:
    d2psi=-k**2*(np.sqrt(2/L))*np.sin(k*x)
    dpsi=dpsi+d2psi*dx
    psi=psi+dpsi*dx
    x=x+dx
    PSI3.append(psi+10)
    P3.append(((np.sqrt(2/L)*np.sin(k*x))**2)+10)

n=4
L=1
k=n*np.pi/L
x=0
psi=np.sqrt(2/L)*np.sin(k*x)
dpsi=np.sqrt(2)*k*np.cos(k*x)/np.sqrt(L)
PSI4=[0]
P4=[psi**2]
dx=1e-5
while x<=L:
    d2psi=-k**2*(np.sqrt(2/L))*np.sin(k*x)
    dpsi=dpsi+d2psi*dx
    psi=psi+dpsi*dx
    x=x+dx
    PSI4.append(psi+15)
    P4.append(((np.sqrt(2/L)*np.sin(k*x))**2)+15)    
    
xgrid=[0,1]
ygrid=[[0,0],[5,5],[10,10],[15,15]]

plt.figure(figsize=(3,6))
plt.title('Wave function for Psi(x,n)')
plt.plot(X,PSI,color='blue')
plt.plot(xgrid,ygrid[0],color='black')
plt.plot(xgrid,ygrid[1],color='black')
plt.plot(xgrid,ygrid[2],color='black')
plt.plot(xgrid,ygrid[3],color='black')
plt.plot(X,PSI2,color='blue')
plt.plot(X,PSI3,color='blue')
plt.plot(X,PSI4,color='blue')
plt.xlim(0,1)
plt.yticks([0,5,10,15],('n=1','n=2','n=3','n=4'))
plt.xticks([0,1],('0','L'))
plt.show()    
    
plt.figure(figsize=(3,6))
plt.title('Probability curve for Psi(x,n)')
plt.plot(X,P,color='blue')
plt.plot(X,P2,color='blue')
plt.plot(X,P3,color='blue')
plt.plot(X,P4,color='blue')
plt.plot(xgrid,ygrid[0],color='black')
plt.plot(xgrid,ygrid[1],color='black')
plt.plot(xgrid,ygrid[2],color='black')
plt.plot(xgrid,ygrid[3],color='black')
plt.xlim(0.1,1)
plt.yticks([0,5,10,15],('n=1','n=2','n=3','n=4'))
plt.xticks([0,1],('0','L'))
plt.show()

n=1
k=n*np.pi/L
def f(x, y):
    return np.sqrt(2/L)*np.sin(k*x)*np.sqrt(2/L)*np.sin(k*y)

x = np.linspace(-L, L, 30)
y = np.linspace(-L, L, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='viridis')
ax.set_xlabel('x')
plt.xticks([])
plt.yticks([])
ax.set_zticks([])
ax.set_ylabel('y')
ax.set_zlabel('z')

import scipy.integrate as inte
import scipy.optimize as opt

def findzeros(rightvals):
    return np.where(np.diff(np.signbit(rightvals)))[0]

def shoot_ode(E,psi_init,x,L):
    sol=inte.odeint(schrderiv,psi_init,x,args=(L,E))
    return sol[len(sol)-1][0]

def schrderiv(y,r,L,E):
    du2=y[0]*((L*(L+1))/(r**2)-2/r-E)
    return [y[1],du2]

def normalize(output):
    normal = max(output)
    return output*(1/normal)

def shoothydr(psi_init,h_,L):
    x_arr_hy=np.arange(0.0001,35.0+h_,h_)
    E_arr = np.arange(-1,0,.001)
    rightb=[]
    for EE in E_arr:
        psi=inte.odeint(schrderiv,psi_init,x_arr_hy,args=(L,EE))[:,0]
        rightb.append(psi[len(psi)-1])
    rightb_arr=np.asarray(rightb)
    crossings=findzeros(rightb_arr)
    energy_1=[]
    for cross in crossings:
        energy_1.append(opt.newton(shoot_ode,E_arr[cross],args=(psi_init,x_arr_hy,L)))
    psi_out=[]
    for EN in energy_1:
        psi_out.append(inte.odeint(schrderiv,psi_init,x_arr_hy,args=(L,EN))[:,0])
    return x_arr_hy,np.asarray(psi_out)

def HYDRO(x,N,L):
    if (((N-L-1)==0) and (L==0)):
        return x*np.exp(-x)
    elif (((N-L-1)==1) and (L==0)):
        return (np.sqrt(2)*(-x+2)*np.exp(-x/2)/4)*x
    elif ((N-L-1)==2):
        return (2*np.sqrt(3)*(2*x**2/9-2*x+3)*np.exp(-x/3)/27)*x
    elif (((N-L-1)==0) and (L==1)):
        return (np.sqrt(6)*x*np.exp(-x/2)/12)*x
    else:
        print("No wavefunction found")
        
def plot_wave(fig,title_string,x_arr,num_arr,ana_arr,axis_list):
    plt.cla()
    plt.clf()
    plt.plot(x_arr,num_arr,'b.',linewidth=4,label=r"$\Psi(\hat{x})_{num}$")
    plt.plot(x_arr,normalize(ana_arr),'r-',label=r"$\Psi(\hat{x})_{ana}$")
    plt.ylabel(r"$\Psi(\hat{x})$",fontsize=16)
    plt.xlabel(r"$\hat{x}$",fontsize='small')
    plt.axis(axis_list)
    plt.title(title_string)
    plt.grid()
    
    
psi_0=0.0
phi_0=1.0
psi_init=np.asarray([psi_0,phi_0])
h_=1.0/200.0    
    
fig=plt.figure()
hydro_x,hydro_num=shoothydr(psi_init,h_,0)
hydro_x2p,hydro_num2p=shoothydr(psi_init,h_,1)
hydro_ana1s=HYDRO(hydro_x,1,0)
hydro_ana2s=HYDRO(hydro_x,2,0)
hydro_ana3s=HYDRO(hydro_x,3,0)
hydro_ana2p=HYDRO(hydro_x,2,1)
print("Hydrogen shooting")
plot_wave(fig,"Hydrogen Atom, 1s",hydro_x,normalize(hydro_num[0,:]),hydro_ana1s,[-0.1,30,-0.1,1.2])
fig1=plt.figure()
plot_wave(fig1,"Hydrogen Atom, 2s",hydro_x,normalize(hydro_num[1,:]),hydro_ana2s,[-0.1,30,-2.2,1.2])
fig2=plt.figure()
plot_wave(fig2,"Hydrogen Atom, 2p",hydro_x2p,normalize(hydro_num2p[0,:]),hydro_ana2p,[-0.1,30,-0.1,1.2])
fig3=plt.figure()
plot_wave(fig3,"Hydrogen Atom, 3s",hydro_x,normalize(hydro_num[2,:]),hydro_ana3s,[-0.1,30,-1.2,1.2])

from mayavi import mlab


x, y, z = np.ogrid[-25:25:200j, -25:25:200j, -25:25:200j]
r=np.sqrt(np.square(x)+np.square(y)+np.square(z))
phi=np.arctan(y/x)
theta=np.arccos(z/r)
s=np.square(((r**2)/81)*(1/np.sqrt(6*np.pi))*(np.e**(-r/3))*((3*np.cos(theta)**2)-1))

mlab.pipeline.volume(mlab.pipeline.scalar_field(s))
mlab.title("3d Hydrogen")
mlab.show()

x, y, z = np.ogrid[-25:25:200j, -25:25:200j, -25:25:200j]
r=np.sqrt(np.square(x)+np.square(y)+np.square(z))
phi=np.arctan(y/x)
theta=np.arccos(z/r)
s=np.square((np.sqrt(2)/81)*(1/(np.sqrt(np.pi)))*(np.e**(-r/3))*(6-r))

mlab.pipeline.volume(mlab.pipeline.scalar_field(s))
mlab.title("3p Hydrogen")
mlab.show()

x, y, z = np.ogrid[-15:15:200j, -15:15:200j, -15:15:200j]
r=np.sqrt(np.square(x)+np.square(y)+np.square(z))
phi=np.arctan(y/x)
theta=np.arccos(z/r)
s=np.square((1/81)*(1/(np.sqrt(3*np.pi)))*(np.e**(-r/3))*(27-(18*r)+(2*r**2)))

mlab.pipeline.volume(mlab.pipeline.scalar_field(s))
mlab.title("3s Hydrogen")
mlab.show()

x, y, z = np.ogrid[-10:10:200j, -10:10:200j, -10:10:200j]
r=np.sqrt(np.square(x)+np.square(y)+np.square(z))
phi=np.arctan(y/x)
theta=np.arccos(z/r)
s=np.square((1/4)*(1/np.sqrt(2*np.pi))*r*(np.e**(-r))*np.cos(theta))

mlab.pipeline.volume(mlab.pipeline.scalar_field(s))
mlab.title("2p Hydrogen")
mlab.show()

x, y, z = np.ogrid[-10:10:200j, -10:10:200j, -10:10:200j]
r=np.sqrt(np.square(x)+np.square(y)+np.square(z))
phi=np.arctan(y/x)
theta=np.arccos(z/r)
s=np.square((1/(4*np.sqrt(2*np.pi))*(2-(r))*np.e**(-r/2)))

mlab.pipeline.volume(mlab.pipeline.scalar_field(s))
mlab.title("2s Hydrogen")
mlab.show()

x, y, z = np.ogrid[-5:5:200j, -5:5:200j, -5:5:200j]
r=np.sqrt(np.square(x)+np.square(y)+np.square(z))
phi=np.arctan(y/x)
theta=np.arccos(z/r)
s=np.square((2/(np.sqrt(np.pi)))*np.e**(-r))

mlab.pipeline.volume(mlab.pipeline.scalar_field(s))
mlab.title("1s Hydrogen")
mlab.show()
    
    
    
    