# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:32:01 2014

@author: remy
"""
import math
import matplotlib.pyplot as plt

############# DICHOTOMIE 
def dicho(f,a,b,epsilon):
    va , vb = f(a) , f(b)
    while b - a > epsilon:
        m = (a + b)/2.
        vm = f(m)
        if va * vm <= 0:
            b , vb = m , vm
        else:
            a , va = m , vm
    return a
    
def r(x):
    return x**2 -2.
    
print(math.sqrt(2) , dicho(r,1,2,10**(-8)))

v =dicho(lambda t: t**2-2. , 1 , 2 , 10**(-10))
print(v)

def dicho1(f,a,b,n):
    va , vb = f(a) , f(b)
    k = 0
    while k < n:
        m = (a + b)/2.
        vm = f(m)
        if va * vm <= 0:
            b , vb = m , vm
        else:
            a , va = m , vm
        k += 1
    # renvoyer le milieu du segment
    return (a+b)/2.

def dicho2(f,a,b,n):
    va , vb = f(a) , f(b)
    k = 0
    while k < n:
        m = (a + b)/2.
        vm = f(m)
        if va * vm <= 0:
            b , vb = m , vm
        else:
            a , va = m , vm
        k += 1
    # renoyer la meilleure extrémité
    if abs(va) < abs(vb):
        return a
    else:
        return b

def dicho3(f,a,b,n):
    va , vb = f(a) , f(b)
    k = 0
    while k < n:
        m = (a + b)/2.
        vm = f(m)
        if va * vm <= 0:
            b , vb = m , vm
        else:
            a , va = m , vm
        k += 1
    # renvoyer une moyenne pondérée
    return (abs(vb)*a + abs(va)*b)/(abs(va) + abs(vb))


r2 = math.sqrt(2)

courbe1 = [math.log(abs(dicho1(r,1,2,i)-r2)) for i in range(1,30)]
courbe2 = [math.log(abs(dicho2(r,1,2,i)-r2)) for i in range(1,30)]
courbe3 = [math.log(abs(dicho3(r,1,2,i)-r2)) for i in range(1,20)]
plt.figure(1)
plt.plot(courbe1,'blue') # milieu du segment
plt.plot(courbe2, 'red') # meilleur bord
plt.plot(courbe3, 'green') # moyenne pond.
plt.show(1)
################# NEWTON

def newt(f,g,b,eps):
    bb = b - f(b)/g(b)
    k = 0
    while abs(bb-b)> eps:
        b =bb
        bb = b - f(b)/g(b)
        k += 1
    return bb

eps = 0.0001
def r(x):
    return x**2 -2.
    
def dr(x) :
    return 2*x
    
r2 = math.sqrt(2)
print(abs(newt(r,dr,2,eps) - r2))

    
j = complex(math.cos(2*math.pi/3),math.sin(2*math.pi/3))
j2 = complex(math.cos(2*math.pi/3),-math.sin(2*math.pi/3))
   
#renvoie le codage d'une couleur suivant la position de z 
def col(z):
    if(abs(z-1)<eps):
        return '.r'
    elif(abs(z-j)<eps):
        return '.b'
    elif(abs(z-j2)<eps):
        return '.g'
    else:
        return 0

def f(x): return x**3-1
def df(x): return 3*x**2

xmin = 0.1
xmax = 10.
ymin = 0.1
ymax = 10
nx = 20
ny = 20
pasx = (xmax-xmin)/nx
pasy = (ymax-ymin)/ny
Lx = [xmin + i*pasx for i in range(0,nx)]
Ly = [ymin + i*pasy for i in range(0,ny)]
plt.figure(2)
for x in Lx:
    for y in Ly:
        zi = complex(x,y)
        z = newt(f,df,zi,eps)
        if col(z) != 0:
            plt.plot([zi.real],[zi.imag],col(z))
plt.show(2)

