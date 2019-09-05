import random as rd
import math, scipy.constants as sc
import matplotlib.pyplot as plt
    
def conformation(n:int):
    theta = []
    for i in range(n):
        theta.append((2*rd.random()-1)*math.pi)
    return theta

def conformation_init(n:int):
    return n*[0]
    
def allongement(theta,l):
    a = 0
    for t in theta:
        a += math.cos(t)
    return l*a
    
def nouvelle_conformation(theta,k:int):
    n = len(theta)
    #theta configuration de longueur n
    theta_n = []
    for t in theta:
        theta_n.append(t)
    #i indice aléatoire à partir duquel k modif
    #i + k <= n => i < n - k +1
    i = rd.randrange(n-k + 1)
    for j in range(i , i + k):
        theta_n[i] = (2*rd.random()-1)*math.pi
    return theta_n
        
def selection_conformation(thetaA, thetaB, 
                           F: float, l:float, T:float):
    coeff = 1/(K_B * T)
    zA = allongement(thetaA,l)
    EA = - zA*F
    zB = allongement(thetaB,l)
    EB = - zB*F
    theta = thetaB
    if EA <= EB:
        P = math.exp(coeff*(EA - EB))
        alea = rd.random()
        if rd.random() > P:
            theta = thetaA
    return theta
    
def plot_conformation(theta):
    x = []
    y = []
    for t in theta:
        x.append(math.cos(t))
        y.append(math.sin(t))
    plt.clf()
    plt.plot(x,y)
    plt.show()


#           Initialisation
def init(n:int, l:float):
    theta = conformation(n)
    al = allongement(theta,l)
    print("allongement initial:",al)
    #initialisation de L, m1, m2
    #L file des 500 derniers allongements
    #m1 moyenne des allongements
    #m2 moyenne des carrés des allongements
    L = [al]
    for i in range(499):
        theta_n = nouvelle_conformation(theta,k)
        theta = selection_conformation(theta,
                                       theta_n,F,l,T)
        L.append(allongement(theta,l))
    m1 = sum(L)/500
    m2 = 0
    for a in L:
        m2 += a**2
    m2 = m2/500
    V = m2 - m1**2
    return [theta,L,m1,m2]


def monte_carlo(F:float, n:int, l:float,
                k:int, epsilon:float):
    i = 500
    data = init(n,l)
    [theta, L, m1, m2] = data 
    V = m2 - m1**2
    while V > epsilon:
        theta_n = nouvelle_conformation(theta,k)
        theta = selection_conformation(theta,
                                       theta_n,F,l,T)
        a_debut = L.pop(0)
        a_fin = allongement(theta,l)
        L.append(a_fin)
        delta_m1 = (a_fin - a_debut)/500 
        m1 += delta_m1
        m2 += delta_m1*(a_fin + a_debut)
        V = m2 - m1**2
        i += 1
    plot_conformation(theta)
    print("nb itérations :",i)
    return m1

#              Paramètres
#constante de Boltzman
K_B = sc.Boltzmann 
K_B = 1.
#nb de monomères
n = 40    
#longueur d'un monomère
l = 1
#nb de monomères modifiés
k = 10
#force
F = 10.
#température
T = 1.
#test d'arrêt variance
eps = 1.0e-1

z = monte_carlo(F,n,l,k,eps)
print("allongement final :",z)