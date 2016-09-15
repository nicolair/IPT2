# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 19:08:37 2013

@author: remy
"""
def changer(sens):
    if sens == "gd":
        return "dg"
    if sens == "dg":
        return "gd"

def tronq(texte,L):
    i = 0
    tronq = ""
    while i < L :
        tronq = tronq + texte[i]
        i += 1
    return tronq

def compl(texte,L):
    l = len(texte)
    for i in range(L -l):
        texte = texte + " "
    return texte
        
def boustro1(texte,p,q):
    # tronquer ou compléter
    if len(texte) < p*q:
        texte = compl(texte,p*q)
    else :
        texte = tronq(texte,p*q)
    #print(len(texte))
    rep = ["" for j in range(q)]
    i = 0
    j = 0
    sens = "gd"
    for c in texte:
        #print(i,j, rep[j],c)
        if sens == "gd" :
            rep[j] = rep[j] + c
        if sens == "dg" :
            rep[j] = c + rep[j]
        i += 1
        if i % p == 0 :
            sens = changer(sens)
            j += 1
    return rep
    
texte = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
lili = boustro1(texte,30,10)
for i in range(10):
    print(lili[i])