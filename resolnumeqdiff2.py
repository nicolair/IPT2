# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:07:50 2014

@author: remy
"""
import matplotlib.pyplot as plt
import numpy as np

def euler3(F,a,b,y0,z_0,h):
    y = [y0,z_0]
    t = a
    l_t = [a]
    l_y = [y]
    while t+h <= b:
        y = [y[0]+h*F(y)[0],y[1]+h*F(y)[1]]
        l_y.append(y)
        t += h
        l_t.append(t)
    return l_y

def F(l):
    return [l[1],- np.sin(l[0])]
    

plt.grid(True)
plt.xlabel('theta')
plt.ylabel('theta prime')
for P in euler3(F, 0.,8.,0.15,-1.,0.05):
  plt.plot(P[0],P[1],'bo')
for P in euler3(F, 0.,8.,0.15,-2.,0.05):
  plt.plot(P[0],P[1],'ro')