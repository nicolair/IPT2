def tri_chaine(L):
    n = len(L)
    for i in range(1,n):
        j = i
        x = L[i]
        while 0 < j and x[1] < L[j-1][1]:
            L[j] = L[j-1]
            j = j - 1
        L[j] = x
        
L = [['Brésil',76], ['Kenya',26017], ['Ouganda',8431]]
print(L)
tri_chaine(L)
print(L)

def f(X):
    # fonction définissant l'équation différentielle
    global r, a, b
    #on suppose que X est un tuple
    # pour assigner les variables en une seule instruction
    s , i , r , d = X
    return np.array([-r*s*i, -r*s*i-(a+b)*i, a*i, b*i])
    
def f(X, Itau):
    # fonction définissant l'équation différentielle
    # Itau est la valeur de I(t-p*dt)
    global r, a, b
    s , i , r , d = X
    return np.array([-r*s*Itau, -r*s*Itau-(a+b)*i, a*i, b*i])
    
# méthode d'Euler
for i in range(N):
    t = t + dt
    if i < p:
        Itau = 0.05
    else:
        Itau = XX[i-p][1]
    X = X + dt * f(X, Itau)
    tt.append(t)
    XX.append(X)