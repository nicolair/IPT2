# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 10:39:28 2014

@author: remy
"""
"""
#script 1
resultat = ""
for c in "Bonsoir":
    resultat = resultat + c
print(resultat)

#script 1
resultat = ""
for c in "Bonsoir":
    resultat = resultat + c
    print(resultat)
    
#script 3
resultat = ""
for c in "Bonsoir":
    resultat =  c + resultat
print(resultat)


#script 1
def fonction_q2(chaine):
    resultat = True
    for c in chaine :
        if c == "A" or c == "C" or c == "G" or c == "T":
            resultat = False
    return resultat

#script 2
def fonction_q2(chaine):
    resultat = False
    for c in chaine :
        if c == "A" or c == "C" or c == "G" or c == "T":
            resultat = True
    return resultat

#script 3
def fonction_q2(chaine):
    c_valids = "ACGT"
    resultat = True
    for c in chaine :
        if c not in c_valids:
            resultat = False
    return resultat

    

#script 4
def fonction_q2(chaine):
    c_valids = "ACGT"
    resultat = True
    for c in chaine :
        temp = False
        for cv in c_valids:
            if c == cv:
              temp = True
        if not temp:
            resultat = False
    return resultat

print(fonction_q2("TAGADA"))    
  

#script1
def fonction_q3 (carac, chaine):
    i = -1
    k = 0
    while i == -1 and k <len(chaine):
        if carac == chaine[k]:
            i = i + 1
            k = k + 1
    return i



#instruction 1
donnees_phylo = [[0,1,0],[0,0,0],[1,0,0]] 
#instruction 2
donnees_phylo = [[0,0,1],[1,0,0],[0,0,0]]

def add_caractere(d_phyl,nouv_carac):
    if len(d_phyl) == len(nouv_carac):
        for i in range(len(d_phyl)):
            d_phyl[i] = d_phyl[i] + [nouv_carac[i]]

def add_espece(d_phyl,nouv_espece):
    if len(d_phyl[0]) == len(nouv_espece):
        d_phyl.append(nouv_espece)


donnees_phylo = [[0,0,0,0],[0,0,0,0],[0,0,1,0]]
#add_caractere(donnees_phylo,[1,1,0])
add_espece(donnees_phylo, [1,0,2,3])
print(donnees_phylo)
"""
def est_ancetre1(esp_1, esp_2):
    """
    renvoie True si esp_1 est ancetre de esp_2
    false sinon
    """
    resultat = True
    if len(esp_1) == len(esp_2):
        for i in range(len(esp_1)):
            if esp_2[i] == 0 and esp_1[i] == 1:
                resultat = False
    print(i)
    return resultat

def est_ancetre2(esp_1, esp_2):
    """
    renvoie True si esp_1 est ancetre de esp_2
    false sinon
    """
    resultat = True
    if len(esp_1) == len(esp_2):
        i = 0
        while i < len(esp_1) and resultat:
            if esp_2[i] == 0 and esp_1[i] == 1:
                resultat = False
            i += 1
    #print(i)
    return resultat

def nombre_descendants(d_phyl,esp):
    """
    renvoie le nb de descendants de espece
    compte tenu des donnees de d_phyl
    """
    nb_desc = 0
    for esp_connue in d_phyl:
        if est_ancetre2(esp,esp_connue):
            nb_desc += 1
    return nb_desc

donnees_phylo = [[0,1,0,0,0,1],[0,0,0,1,0,1],[1,0,0,0,0,0]] 
    
"""    
e1 = [0,0,0,1,0,1]
e2 = [0,0,1,0,0,1]
print(est_ancetre1(e1,e2))
print(est_ancetre2(e1,e2))
"""