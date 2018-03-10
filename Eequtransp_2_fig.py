#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 16:03:50 2018

@author: remy
"""
import math
import matplotlib.pyplot as plt

def v(x):
    return math.sin(2*math.pi*x)

#schéma centré
def transportCtre(tmax,nt,nx,v):
    tau = tmax*nx / nt
    lx = [l/nx for l in range(nx + 1)]
    u = []
    u.append([v(x) for x in lx])

    k = 0
    while k < nt:
        lili = []
        lili.append(u[k][0] + 0.5*tau*(u[k][nx-1] - u[k][1]))
        for l in range(1,nx):
            lili.append( u[k][l] + 0.5*tau*(u[k][l-1] - u[k][l+1]))
        lili.append(u[k][nx] + 0.5*tau*(u[k][nx-1] - u[k][1]))
        u.append(lili)
        k += 1
    return u


#                   éléments communs à toutes les figures
nx = 100
#lx liste des x indexée de 0 à nx
lx = [l/nx for l in range(nx + 1)]
#lv liste des valeurs pour la condition aux limites
lv = [v(x) for x in lx]
# % largeur comme écartement entre les sous-figures
ecart = 0.3


#                  figures pour le schéma centré
nt = 100
plt.figure(2)
plt.subplots_adjust(wspace=ecart)
#condition aux limites
plt.subplot(1,2,1)
plt.plot(lx,lv,'.',label='t = 0')

u = transportCtre(0.5,nt,nx,v)
plt.plot(lx,u[nt],'--',label='t = 0.5')
u = transportCtre(1.0,nt,nx,v)
plt.plot(lx,u[nt],label='t = 1.0')
plt.legend()
plt.title('nt = 100')

nt = 200
plt.subplot(1,2,2)
u = transportCtre(1.0,nt,nx,v)
plt.plot(lx,u[nt],'g--',label='t = 1.0')
u = transportCtre(1.35,nt,nx,v)
plt.plot(lx,u[nt],label='t = 1.35')
plt.legend()
plt.title('nt = 200')
plt.savefig('Eequtransp_2.pdf',format='pdf')

