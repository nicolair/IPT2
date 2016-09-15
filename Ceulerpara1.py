# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 16:23:43 2015

@author: remy
"""
import matplotlib.pyplot as plt
import numpy as np

def vpara(v0,T,n):
    g = float(9.81)
    K = float(0.0357)
    h = T/float(n)
    t = [i*h for i in range(n)]
    v = [0. for i in range(n)]
    v[0] = v0
    for i in range(n-1):
        v[i+1] = v[i] +(g - K*v[i]**2)*h
    return [t,v]

vini = [0.,10.,20.,30.]
for v in vini:    
  truc = vpara(v,6.5,100)
  plt.plot(truc[0],truc[1])
  

