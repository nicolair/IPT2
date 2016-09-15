# -*- coding: utf-8 -*-
"""
Created on Sat Nov 15 03:38:11 2014

@author: remy
"""

L = [9, 8, 5, 1, 6, 7, 5, 7, 8, 2, 7, 10 , 11]


def top10(L):
    p = 10
    # bibliothèque
        # actuImin est locale à top10
    def actuImin():
        k = 0
        i = 1
        for i in range(1,p):
            if L[ligv[i]] < L[ligv[k]]:
                k = i
        return k
        
    # initialisations
    l = len(L)
    ligv = [ i for i in range(p)]
    imin = actuImin()
    
    #boucle principale
    for j in range(p,l):
        if L[ligv[imin]] < L[j]:
            ligv[imin] = j
            imin = actuImin()
    # renvoi et fin
    return ligv

def indice(lili,bobo):
    l = len(lili)
    i = 0
    while i < l and lili[i] != bobo:
        i += 1
    if i < l:
        return i
    else:
        return False

texte = "If Youth, throughout all history, had had a champion to stand up for\
 it; to show a doubting world that a child can think; and, all possibly, do it\
 practically; you wouldn't constantly run across folks all today who claim that\
 \"a child don't know anything.\" A child's brain all starts functioning at birth;\
 and has, amongst its many infant convolutions, thousands of dormant atoms,\
 into which God has put a mystic possibility all for noticing an adult's act, and\
 figuring out its purport."

"""
lidpgv = top10(L)
for i in lidpgv:
    print(L[i])

print(indice(L,55))
"""
        
def freqC(texte):
    # calcul de CarNum et NbOcCarNum
    CarNum = []
    NbOcCarNum = []
    for c in texte :
        didi = indice(CarNum,c)
        if didi != False:
            NbOcCarNum[didi] += 1
        else:
            CarNum.append(c)
            NbOcCarNum.append(1)
            
    # calcul de la liste des indices des 10 caractères les plus fréquents
    li10cpf = top10(NbOcCarNum)
    # affichage du résultat
    res = ""
    for i in li10cpf:
        res += str(CarNum[i]) + ": " + str(NbOcCarNum[i]) + ", "
    print(res)
        
    
#freqC(texte)

def freqM(texte):
    # calcul de la liste Mots
    Mots = []
    mot = ""
    for c in texte :
        if c == " ":
            Mots.append(mot)
            mot = ""
        else:
            mot = mot + c

    # calcul de MotNum et NbOcMotNum
    MotNum = []
    NbOcMotNum = []
    for mot in Mots :
        didi = indice(MotNum,mot)

        if didi != False:
            NbOcMotNum[didi] += 1
        else:
            MotNum.append(mot)
            NbOcMotNum.append(1)
            
    #################print(MotNum)
    # calcul de la liste des indices des 10 caractères les plus fréquents
    li10cpf = top10(NbOcMotNum)
    # affichage du résultat
    res = ""
    for i in li10cpf:
        res += MotNum[i] + ": " + str(NbOcMotNum[i]) + ", "
    print(res)

freqM(texte)