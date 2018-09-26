

def moyenne(liste_niveaux):
    cpt = 0
    m = 0.
    for niveau in liste_niveaux:
        m += niveau
        cpt += 1
    return m/cpt
    
    
def integrale_precise(liste_niveaux):
    N = len(liste_niveaux)
    integ = liste_niveaux[0]*0.5
    for i in range(1,N-1):
        integ += liste_niveaux[i]
    integ += liste_niveaux[N-1]*0.5
    return int
    
def moyenne_precise(liste_niveaux):
    integ = integrale_precise(liste_niveaux)
    return int / 1200
    
    
def ind_premier_pzd(liste_niveaux):
    N = len(liste_niveaux)
    m = moyenne_precise(liste_niveaux)
    i = 0
    while i < N - 1 and \\
     (liste_niveaux[i] < m or liste_niveaux[i+1] > m):
        i += 1
    if i == N-1:
        return -1
    else:
        return i
        
        
def ind_dernier_pzd(liste_niveaux, m):
    N = len(liste_niveaux)
    i = N-1
    while i > 0 and \\
     (liste_niveaux[i-1] < m or liste_niveaux[i] > m):
        i -= 1
    if i == 0:
        return -2
    else:
        return i-1
    
    
def decompose_vague(liste_niveaux):
    successeurs = construction_successeurs(liste_niveaux)
    nbv = len(successeurs) - 1 # nb de vagues
    vagues = []
    for i in range(nbv):
        sdeb = successeurs[i]
        sfin = successeurs[i+1]
        vagues.append(liste_niveaux[sdeb:sfin]
    return vagues
    
    
def proprietes(liste_niveaux):
    dt = 0.5 # en s freq = 2 Hz
    vagues = decompose_vagues(liste_niveaux)
    nbv = len(vagues) # nb de vagues
    lprop = []
    
    Z = ind_premier_pzd(liste_niveaux)
    vague = vagues[0]
    H = max(liste_niveaux[:Z]) - min(vague)
    T = len(vague)*dt
    lprop.append([H,T))
    
    for in in range(1,nbv - 1)
        H = max(vagues[i]) - min(vagues[i+1])
        T = len(vagues[i])*dt
        lprop.append([H,T])
        
    Z = ind_dernier_pzd(liste_niveaux)
    vague = vagues[nbv-1]
    T = len(vague)*dt
    H = max(vague) - min(liste_niveaux[Z:])
    
    return lprop
        
        
def hauteur_max(liste_niveaux):
    props_v = proprietes(liste_niveaux)
    hmax = 0
    for prop in props_v:
        if prop[0] > hmax:
            hmax = prop[0]
    return hmax
    
    

    