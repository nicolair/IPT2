# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 19:23:09 2013

@author: remy
"""

def cherchemot(M,T):
    c = M[0]
    i = 0
    o = -1
    m = len(M)
    t = len(T)
    cont = True
    while cont:
        while i + m < t and T[i] != c :
            i += 1
        if i + m == t :
            cont = False
        else :
            if M == T[i:i+m]:
                o = i
                cont = False
            else:
                i += 1
    return o
    
    
texte = "tagada tsoin tsoin"
mot = "tso"
print(cherchemot(mot,texte))