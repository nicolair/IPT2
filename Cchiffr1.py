#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 18:32:56 2018

@author: remy
"""

def verifie(L) :
    for k in L:
        if type(k) != int or k < 0 or k > 25:
            return False
    return True

def chiffrement_cesar(L,d):
    C = []
    for k in L:
        C.append((k+d) % 26)
    return C

def dechiffrement_cesar(L,d):
    return(chiffrement_cesar(L,-d))
    
def frequences(L):
    lifreq = 26*[0]
    for k in L:
        lifreq[k] += 1
    return lifreq

def indice_max(T):
    imax = 0
    for k in range(1,len(T)):
        if T[k] > T[imax]:
            imax = k
    return imax

def dechiffrement_auto(L):
    imax = indice_max(frequences(L))
    #imax devrait désigner 4 pour 'e'
    cle = (imax - 4) % 26
    return dechiffrement_cesar(L,cle)

def chiffrement_vigenere(L,C):
    c = []
    for k in range(len(L)):
        cle = k % len(C)
        c.append((L[k] + cle) % 26)
    return c
    
    