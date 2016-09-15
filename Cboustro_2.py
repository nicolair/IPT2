# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:28:32 2013

@author: remy
"""
"""
def suivant(i,j):
    if i - j*(-1)**j == 0:
        i += (-1)**j
        j += 1
    else:
      i += 2*(-1)**j
    return i,j
#print(suivant(-3,3))

def num(i,j):
    if i-j>0 or i+j<0 or not( (i-j) % 2 == 0):
        return -1
    P = 0,0
    n = 0
    while P[0] != i or P[1] != j:
        P = suivant(P[0],P[1])
        n += 1
    return n
print(num(3,7))
# à titre de vérification
i = 3
j = 7
print((j*(j+1)+j+i*(-1)**j)/2)
"""

    
def boustro2(n):
    # initialisations
    P = [0,0,1]
    Valeur = {(0,0):1}
    c = 1
    def Vsuivant(P):
        sens = P[2]
        if P[0] - sens*P[1] == 0:
            P[0] += sens
            P[1] += 1
            P[2] *= -1
            return 0
        a = P[0]
        P[0] += 2*sens
        return  Valeur[a,P[1]] + Valeur[a+sens,P[1]-1] 
    # boucle principale
    while c < n:
        v = Vsuivant(P)
        Valeur[P[0],P[1]] = v
        c += 1
    return  Valeur
    
print(boustro2(10))