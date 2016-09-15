# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 16:12:03 2013

@author: remy
"""

def indice(lili,obj):
    # n nb de valeurs de la liste
    n = len(lili)
    #indice dans la liste
    i = 0
    while i< n:
        if lili[i] == obj:
            return i
        else:
            i = i + 1
    return -1
        
def top10(L):
    n = len(L)
    Imax = ["" for i in range(10)]
    Vmax = ["" for i in range(10)]
    Imax[0] = 0
    Vmax[0] = L[0]
    p = 1
    i = 1
    #traitement des premières valeurs
    while i < 10:
        if L[i] <= Vmax[p-1]:
            Vmax[p] = L[i]
            Imax[p] = i
        else:
            j = p-1
            while (j>=0) & (L[i] > Vmax[j]):
                Vmax[j+1] = Vmax[j]
                Imax[j+1] = Imax[j]
                j = j-1
            Vmax[j+1] = L[i]
            Imax[j+1] = i
        i += 1
        p += 1
    
    #traitement des autres valeurs
    while i < n:
        if L[i] > Vmax[p-1]:
            j = p-1
            while (j>=0) & (L[i] > Vmax[j]):
                Vmax[j] = Vmax[j-1]
                Imax[j] = Imax[j-1]
                j = j-1
            Vmax[j+1] = L[i]
            Imax[j+1] = i
        i += 1
    return Imax
    
lili = [1,2,1,4,6,14,22,45,78,54,42,12,63,7,15,29,35,85,23]
t10 = top10(lili)
v10=[lili[t10[i]] for i in range(10)]
print(t10)
print(v10)