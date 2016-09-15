# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ce script temporaire est sauvegardé ici :
/home/remy/.spyder2/.temp.py
"""
import os.path

"""
cheminabs_vers_moi = __file__ 

cheminabs_vers_mon_doss = os.path.dirname(__file__)
# un autre moyen : get current working directory
cheminabs_vers_mon_doss1 = os.getcwd()

mon_nom = os.path.basename(__file__)

print ("cheminabs_vers_moi = "+cheminabs_vers_moi)
print("cheminabs_vers_mon_doss = "+cheminabs_vers_mon_doss)
print("cheminabs_vers_mon_doss1 = "+cheminabs_vers_mon_doss1)
print("mon_nom = "+mon_nom)
"""

"""
mes_voisins = os.listdir(chemin_vers_mon_doss)
for machin in mes_voisins:
  print(machin)
"""

"""
moi = open(cheminabs_vers_moi)
print(type(moi))
mon_nb_lignes = 0
for lili in moi:
    mon_nb_lignes += 1
    
print("mon_nb_lignes = "+str(mon_nb_lignes))

#pour afficher les 5 dernières lignes
mon_num_lign = mon_nb_lignes -6

moi.seek(0)
i = 0
for lili in moi:
    if i > mon_num_lign :
        print(str(i)+" : "+lili)
    i += 1
    
#afficher mes 5 dernières lignes
    
moi.close()
#tagada#
"""
cible = open('cible.py') 
print type(cible)
