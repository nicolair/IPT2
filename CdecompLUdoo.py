# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 07:30:19 2015

@author: remy
"""
#print(sum(k for k in range(5) ))


def lulu(A,p):
  # initialisation de L et U
  L = [[0 for j in range(p)] for i in range(p)]
  U = [[0 for j in range(p)] for i in range(p)]
  for i in range(p):
    L[i][i] = 1.
        
  for i in range(p):
    #calcul de la ligne i de U
    for j in range(i,p):
      #(ligne i de L) (col j de U) -> U[i][j]
      s = sum(L[i][k]*U[k][j] for k in range(0,i))
      U[i][j] = A[i][j]- s
                
    #calcul de la colonne i de L
    for j in range(i+1,p):
      #(ligne j de L) (colonne i de U) -> L[j][i]
      if abs(U[i][i])< 0.01:
        return(["erreur",[i,j]])
      s = sum(L[j][k]*U[k][i] for k in range(0,i))
      L[j][i] = (A[j][i]- s)/U[i][i]
  return([L,U])
    
p = 3
A = [[1.,2.,3.],[4.,5.,6.],[7.,8.,10.]]

truc = lulu(A,p)
L = matrix(truc[0])
U = matrix(truc[1])
print(L*U)


def resinf(L,Y,p):
  X = [[0] for i in range(p)]
  for i in range(p):
    #calcul de X[i][0]
    s = sum(L[i][j]*X[j][0] for j in range(0,i))
    X[i][0] = Y[i][0] - s
  return(X)

L = [[1,0,0],[2,1,0],[3,2,1]]  
Y = [[1],[1],[1]]
X = resinf(L,Y,p)
print(X)


def ressup(U,Y,p):
  X = [[0] for i in range(p)]
  i = p-1
  while i >= 0:
    s = sum(U[i][j]*X[j][0] for j in range(i+1,p))
    X[i][0] = (Y[i][0] - s)/U[i][i]
    i += -1
  return(X)
  
U = [[1,2,3],[0,4,5],[0,0,6]]
Y = [[4],[5],[6]]
X = ressup(U,Y,p)
print(X)

def res(A,Y,p):
    truc = lulu(A,p)
    if truc == "erreur":
        return("erreur")
    L = truc[0]
    U = truc[1]
    X = resinf(L,Y,p)
    X = ressup(U,X,p)
    return(X)
    
Y = [[1],[0],[0]]
X = res(A,Y,p)
print(X)
A = matrix(A)
X = matrix(X)
print(A*X)