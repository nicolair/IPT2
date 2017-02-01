# -*- coding: utf-8 -*-
"""
Created  1 02 17
script pour créer les images pdf à inclure dans le LaTex
@author: remy
"""
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

def euler3(F,a,b,y0,z0,h):
    y = [y0,z0]
    t = a
    l_t = [a]
    l_0 = [y0]
    l_1 = [z0]
    while t+h <= b:
        y = [y[0]+h*F(y)[0],y[1]+h*F(y)[1]]
        l_0.append(y[0])
        l_1.append(y[1])
        t += h
        l_t.append(t)
    return l_0,l_1

def F(l):
    return [l[1],- np.sin(l[0])]
    

#plt.show()
with PdfPages('./resolnumeqdiff_1.pdf') as pdf:
    plt.grid(True)
    plt.xlabel(r'$\theta$')
    plt.ylabel(r'$\theta\prime$')
    
    truc = euler3(F, 0.,8.,0.15,-1.,0.05)
    plt.plot(truc[0],truc[1],'bo')
    plt.text(-0.8, -1.5,r'init $\theta\prime = -1.0$',fontsize=14,color='blue')
    
    truc = euler3(F, 0.,8.,0.15,-2.,0.05)
    plt.plot(truc[0],truc[1],'ro')
    plt.text(-0.8, -2.3,r'init $\theta\prime = -2.0$',fontsize=14,color='red')

    pdf.savefig()
    plt.close()

 
