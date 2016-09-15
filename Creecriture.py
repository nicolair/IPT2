# -*- coding: utf-8 -*-
"""
Created on Fri Jun 13 18:01:53 2014

@author: remy
"""
#from matplotlib import use
#use('pdf')

import matplotlib.pyplot as plt
from math import cos, sin, pi
"""
def a(E):
    plt.plot([E[2],E[2]+E[0]],[E[3],E[3]+E[1]],'g')
    return [E[0],E[1],E[2]+E[0],E[3]+E[1]]
    
def l(E):
    return [cos(alpha)*E[0] - sin(alpha)*E[1], sin(alpha)*E[0] + cos(alpha)*E[1], E[2], E[3]]

def r(E):
    return [cos(alpha)*E[0] + sin(alpha)*E[1], -sin(alpha)*E[0] + cos(alpha)*E[1], E[2], E[3]]
    
func_dic = {'a':a, 'l':l, 'r':r}

def affiche(L):
    plt.clf()
    plt.figure(1)
    plt.axis('equal')
    plt.axis('off')
    E = [1.,0.,0.,0.]
    for lettre in L:
        E = func_dic[lettre](E)

init = "allalla"
motif = "arallara"
alpha = pi/3

texte  = init
#print texte
for i in range(4):
    texte = texte.replace('a',motif)


affiche(texte)
"""
def a(lE):
    n = len(lE)-1
    E = lE[n] # état actuel
    plt.plot([E[2],E[2]+E[0]],[E[3],E[3]+E[1]],'g')
    lE[n] = [E[0],E[1],E[2]+E[0],E[3]+E[1]] 
    return lE
    
def l(lE):
    n = len(lE)-1
    E = lE[n] # état actuel
    lE[n] = [cos(alpha)*E[0] - sin(alpha)*E[1], sin(alpha)*E[0] + cos(alpha)*E[1], E[2], E[3]]
    return lE

def r(lE):
    n = len(lE)-1
    E = lE[n] # état actuel
    lE[n] = [cos(alpha)*E[0] + sin(alpha)*E[1], -sin(alpha)*E[0] + cos(alpha)*E[1], E[2], E[3]]
    return lE
    
def e(lE):
    n = len(lE)-1
    E = lE[n] # état actuel
    lE.append(E)
    return lE

def m(lE):
    lE.pop()
    return lE
    
def x(lE):
    return lE
    
func_dic = {'a':a, 'l':l, 'r':r, '(':e, ')':m, 'x':x}

def affiche(L,nom_fic):
    plt.clf()
    plt.figure(1)
    plt.axis('equal')
    plt.axis('off')
    lE = [[0.,1.,0.,0.]]
    for lettre in L:
        lE = func_dic[lettre](lE)
    plt.savefig(nom_fic,bbox_inches='tight')

# flocon de Von Koch
init = "allalla"
motif = "arallara"
alpha = pi/3

#exple 1
init = "a"
motif = "a(la)a(ra)a" 
alpha = 25.7*pi/180

#exple 2
#init = "a"
#motif = "a(la)a(ra)(a)" 
#alpha = 20*pi/180

#exple 3
#init = "a"
#motif = "aar(ralala)l(larara)" 
#alpha = 22.5*pi/180

texte = init
for i in range(5):
    texte = texte.replace('a',motif)
affiche(texte,'Ereecriture_1.pdf')


#########           exemples avec apex
#exple 1
#motifx = 'a(lx)a(rx)lx'
#alpha = 20.0*pi/180

#exple 2 
#motifx = 'a(lx)(rx)ax'
#alpha = 25.7*pi/180

#exple 3 
motifx = 'ar((x)lx)la(lax)rx'
alpha = 22.5*pi/180

"""
texte = 'x'
for i in range(6):
    texte = texte.replace('a','aa')
    texte = texte.replace('x',motifx)
    
affiche(texte,'Creecriture_6.pdf')
"""
