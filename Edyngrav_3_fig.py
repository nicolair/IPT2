# -*- coding: utf-8 -*-
import math
import matplotlib
#sortie du module graphique
#vers des fichiers pdf plutôt que vers fenêtre interactive
matplotlib.use('pdf')
import matplotlib.pyplot as plt
#################################

def smul(nono, lili):
    lirev = []
    for v in lili:
        lirev.append(nono*v)
    return lirev

def vsom(l1,l2):
    nb = len(l1)
    lirev = []
    for i in range(nb):
        lirev.append(l1[i] + l2[i])
    return lirev

def vdif(l1,l2):
    nb = len(l1)
    lirev = []
    for i in range(nb):
        lirev.append(l1[i] - l2[i])
    return lirev

###########################         
       
def euler(f,y0,z0,h,n):
    #initialisations
    y , z = y0 , z0
    Ly , Lz = [y] , [z]
    for i in range(n-1): #n-1 car ini connu  
        fy = f(y)
        y += z*h
        z += fy*h
        Ly.append(y)
        Lz.append(z)
    return Ly, Lz

def verlet(f,y0,z0,h,n):
    #initialisations
    y , z = y0 , z0
    Ly , Lz = [y] , [z]
    for i in range(n-1): 
        fy = f(y) 
        y += z*h + h*h*fy/2 #y suivant
        ffy = f(y) # valeur de f au y suivant
        z += h*(fy +ffy)/2
        Ly.append(y)
        Lz.append(z)
    return Ly, Lz

def f(u):
    omega = 2*math.pi
    return -omega*omega*u
    
############################

def norme2(v):
    return (v[0]**2 + v[1]**2 + v[2]**2)**0.5
    
def force2(m1,p1,m2,p2):
    #force par 2 sur 1
    G = 6.67e-11
    v = vdif(p1,p2)
    coeff = G*m1*m2*norme2(v)**(-3)
    return smul(coeff,v)

def forceN(j,m,pos):
    force = [0.,0.,0.]
    N = len(m)
    for k in range(N):
        if k!= j:
            f = force2(m[k],pos[k],m[j],pos[j])
            force = vsom(force, f)
    return force
    
def pos_suiv(m,pos,vit,h):
    N = len(m)
    L = []
    for j in range(N):
        force = forceN(j,m,pos)
        acc_pos1 = smul(h,vit[j])
        new_pos = vsom(pos[j],acc_pos1)# Euler
        coeff = h*h/(2*m[j])
        acc_pos2 = smul(coeff,force) # Verlet
        new_pos = vsom(new_pos,acc_pos2)
        L.append(new_pos)
    return L
    
def etat_suiv(m,pos,vit,h):
    N = len(m)
    new_pos = pos_suiv(m,pos,vit,h)
    new_vit = []
    for j in range(N):
        coeff = h/(2*m[j])
        f = forceN(j,m,pos)
        ff = forceN(j,m,new_pos)
        acc_v = vsom(f,ff)
        acc_v = smul(coeff,acc_v)
        new_vit.append(vsom(vit[j],acc_v))
    return new_pos, new_vit
    
    
m = [1e12,5e10]
pos = [[0,0,0],[1,0,0]]
vit = [[0,0,0],[0,9,0]]
h = 1e-2

liste_pos = []
for k in range(600):
    pos, vit = etat_suiv(m,pos,vit,h)
    liste_pos.append(pos)

x0, y0, x1, y1 = [],[],[],[]
X0, Y0, X1, Y1 = [],[],[],[]
M = m[0]+m[1] 
c0 = m[0]/M
c1 = m[1]/M
for pos in liste_pos:
    xG = c0*pos[0][0] + c1*pos[1][0]
    yG = c0*pos[0][1] + c1*pos[1][1]
    x0.append(pos[0][0])
    X0.append(pos[0][0] - xG)
    y0.append(pos[0][1])
    Y0.append(pos[0][1] - yG)
    x1.append(pos[1][0])
    X1.append(pos[1][0] - xG)
    y1.append(pos[1][1])
    Y1.append(pos[1][1] - yG)

plt.plot(x0,y0,color='red')
plt.plot(x1,y1,color='darkgreen')
plt.title(r'$(x0,y0)\;, \;(x1,y1)$')
plt.savefig('Edyngrav_3_fig.pdf')
plt.clf()




