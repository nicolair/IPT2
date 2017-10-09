#!/usr/bin/env python3
# -*- coding: utf-8 -*-
truc = """
Created on Fri Oct  6 15:45:24 2017

@author: remy
"""
Vache = '''
  
   ^__^             
   (oo)\_______     
   (__)\       )\/\ 
       ||----w |    
       ||     ||    
  
'''

       
print(Vache)
   

oct = '01234567'
lilicow = []
for c in Vache:
    lilicow.append(ord(c))

Ehcav = ''
chaine = ''    
for c in Vache:
    if c != '\n':
        chaine = c + chaine
    else:
        Ehcav = Ehcav + chaine + c
        chaine = ''
        
Ehcav = Ehcav.replace('(','truc')
Ehcav = Ehcav.replace(')','(')
Ehcav = Ehcav.replace('truc',')')
Ehcav = Ehcav.replace('\\','truc')
Ehcav = Ehcav.replace('/','\\')
Ehcav = Ehcav.replace('truc','/')

print(Ehcav)
       
renv = ''
chaine = ''
for c in Vache:
    if c != '\n':
        chaine = chaine + c
    else:
        renv = chaine + '\n' + renv
        chaine = ''
renv = renv.replace('_',chr(8254))
renv = renv.replace('^','v')
renv = renv.replace('w','U')
renv = renv.replace('\\','truc')
renv = renv.replace('/','\\')
renv = renv.replace('truc','/')

print(renv)

liV = Vache.splitlines()
liE = Ehcav.splitlines()
liR = renv.splitlines()


#on complète par des espaces pour que les lignes fassent 25 caractères
n = 21
for i in range(len(liV)) :
    p = len(liV[i])
    liV[i] = liV[i] + (n-p)*' '
for i in range(len(liE)) :
    p = len(liE[i])
    liE[i] = liE[i] + (n-p)*' '

for i in range(len(liV)):
    print(liV[i] + liE[i] + liR[i])

    
#pour les afficher cote à cote
"""       
i = 0    
for cha in Cow:
    print(i, cha)
    i += 1

CowX = ''
i = 0    
for cha in Cow:
    if cha == 'o' :
        CowX = CowX + 'x'
    else :
        CowX =CowX + cha
    i += 1
print(CowX)

CowD = ''
i = 0    
for cha in Cow:
    if cha == '\n' :
        CowD = CowD + cha +'x'
    else :
        CowD =CowD + cha
    i += 1
print(CowD)

CowL = '''

   ^__^                             
   (xx)\_______                   
   (__)\       )\/\             
    U  ||----w |           
       ||     ||  
       
       '''
"""