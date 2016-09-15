# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:07:50 2014

@author: remy
"""
import matplotlib.pyplot as plt
import numpy as np
"""
def euler1(F,a,b,y0,h):
    y = y0
    t = a
    l_t = [a]
    l_y = [y0]
    while t+h <= b:
        y += h*F(t,y)
        l_y.append(y)
        t += h
        l_t.append(t)
    return l_t, l_y

tau = -3.5
x = np.linspace(0.,1.,50)
y = np.exp(tau*x)
plt.plot(x,y, 'b')
truc = euler1(lambda t,y: tau*y, 0.,1.,1.,0.3)
plt.plot(truc[0],truc[1],'g')
truc = euler1(lambda t,y: tau*y, 0.,1.,1.,0.1)
plt.plot(truc[0],truc[1],'r')
"""
import matplotlib.pyplot as plt
import numpy as np

def euler2(F,a,b,y0,h):
    y = y0
    t = a
    l_t = [a]
    l_y = [y0]
    yy = y + h*F(t,y)
    l_y.append(yy)
    t += h
    l_t.append(t)
    while t+h <= b:
        yyy = y + 2*h*F(t,yy)
        l_y.append(yyy)
        y = yy
        yy = yyy
        t += h
        l_t.append(t)
    return l_t, l_y

tau = 1
tau = -3.5
x = np.linspace(0.,1.,50)
y = np.exp(tau*x)
plt.plot(x,y, 'b')
truc = euler2(lambda t,y: tau*y, 0.,1.,1.,0.3)
plt.plot(truc[0],truc[1],'g')
truc = euler2(lambda t,y: tau*y, 0.,1.,1.,0.1)
plt.plot(truc[0],truc[1],'r')
