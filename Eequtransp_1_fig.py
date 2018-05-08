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

#schéma décentré à droite
def transportDrte(tmax,nt,nx,v):
    tau = tmax*nx / nt
    #lx liste des x indexée de 0 à nx
    lx = [l/nx for l in range(nx + 1)]
    
    #u est une liste de listes
    #u[k] est la fonction de l'espace au temps k*Dt
    u = []
    #u[0] cad u pour t = 0    
    u.append([v(x) for x in lx])

    k = 0
    
    while k < nt:
        if k >1 :
            print("coucou",lili)
        #lili désigne la liste des u(k,l) pour le k courant
        lili = [ u[k][l] + tau*(u[k][l] - u[k][l+1]) for l in range(nx)]
        #attention à l=nx
        #lili.append(u[k][nx] + tau*(u[k][nx] - u[k][1]))
        lili.append(lili[0])
        u.append(lili)
        lili[1]=0
        k += 1
        
    return u

#                   éléments communs à toutes les figures
nx = 5
#lx liste des x indexée de 0 à nx
lx = [l/nx for l in range(nx + 1)]
#lv liste des valeurs pour la condition aux limites
lv = [v(x) for x in lx]
# % largeur comme écartement entre les sous-figures
ecart = 0.3

#                figure pour le schéma décentré à droite
nt = 4
#plt.figure(1)
#plt.subplots_adjust(wspace=ecart)
#condition aux limites
#plt.subplot(1,2,1)
#plt.plot(lx,lv,'.',label='t = 0')

u = transportDrte(0.2,nt,nx,v)
plt.plot(lx,u[nt],'--',label='t = 0.1')
"""u = transportDrte(0.2,nt,nx,v)
plt.plot(lx,u[nt],label='t = 0.2')
plt.legend()
plt.title('nt = 100')

nt = 200
plt.subplot(1,2,2)
#lx = [l/nx for l in range(nx + 1)]
u = transportDrte(0.2,nt,nx,v)
plt.plot(lx,u[nt],'g',label='t = 0.2')
plt.legend()
plt.title('nt = 200')
plt.savefig('Eequtransp_1.pdf',format='pdf')
"""
for truc in u:
    print(truc)