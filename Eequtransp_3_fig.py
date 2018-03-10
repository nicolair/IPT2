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

#schéma décentré à gauche
def transportGche(tmax,nt,nx,v):
    tau = tmax*nx / nt
    Dx = 1/nx
    lx = [l*Dx for l in range(nx + 1)]
    u = []
    u.append([v(x) for x in lx])
    k = 0
    while k < nt:
        lili = []
        lili.append( u[k][0] + tau*(u[k][nx-1] - u[k][0]))
        for l in range(1,nx+1):
            lili.append( u[k][l] + tau*(u[k][l-1] - u[k][l]))
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

#             figures pour le schéma décentré à gauche
nt = 100
plt.figure(3)
plt.subplots_adjust(wspace=ecart)
plt.subplot(1,2,1)
#condition aux limites
plt.plot(lx,lv,'.',label='t = 0')

u = transportGche(0.5,nt,nx,v)
plt.plot(lx,u[nt],'--',label='t = 0.5')
u = transportGche(1.2,nt,nx,v)
plt.plot(lx,u[nt],label='t = 1.2')
plt.legend()
plt.title('nt = 100')

plt.subplot(1,2,2)
nt = 200
u = transportGche(1.2,nt,nx,v)
plt.plot(lx,u[nt],'g.',label='t = 1.2')
u = transportGche(2.,nt,nx,v)
plt.plot(lx,u[nt],'--',label='t = 2')
plt.legend()
plt.title('nt = 200')
plt.savefig('Eequtransp_3.pdf',format='pdf')
