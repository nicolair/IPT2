p = 5
# Initialisation
f = 1
n = 1
# f designe la factorielle de n

while n < p:
    # bloc d'instructions
    n += 1
    f *= n
    # f designe encore la factorielle de n
print p,n,f

n = 22
p = 2
while n % p != 0:
    p += 1
if p < n :
    print "compose"
else:
    print "premier"

n = 16
d = 2 # 1 et n sont des diviseurs
p = 2
while p*p < n:
    if n % p == 0:
        d += 2
    p += 1
if p*p == n:
    d += 1
print "nb diviseurs de " + str(n) + " = " + str(d) 


n = 22
code = ''
while n > 0 :
    if n % 2 == 0:
        n = n // 2
        code = code + 'P'
    else:
        n = (n-1) // 2
        code = code + 'I'
print code

n = 22
code = ''
while n > 0 :
    if n % 2 == 0:
        n = n // 2
        code = '0' + code
    else:
        n = (n-1) // 2
        code = '1' + code
code = '0b' + code
print code
print bin(22) # verification


n = 22
code = ''
while n > 0 :
    r = n % 3 
    n = n // 3
    code = str(r) + code
print int(code,3)
code = '0t' + code
print code

n = 2554 ; p = 39
i = 0
while n > p :
  n -= p
  i += 1
print(n,i)


l = 12 # nb total de lignes
c = 8  # nb de colonne
q = 4  # nb de caracteres dans une cellule

############ Initialisation
i = 0  # compteur multi-usage

bord = ''  #nom chaine pour bord horizontal
cell = '|' #nom chaine pour cellule dans une ligne 
lign = ''  #nom chaine pour ligne
 
# c(q+1) + 1 caractères dans une ligne
n = c*(q+1) + 1

########## Calculs
# constitution d'un bord horizontal
while i < n:
    bord += '-'
    i += 1

#constitution d'une cellule
i = 0
while i < q:
    cell += ' '
    i += 1
    
#constitution d'une ligne
i = 0
while i < 8:
    lign += cell
    i += 1
lign += '|'

###########  Affichage
i = 0
#ligne 0
print bord
i += 1

# lignes 1 à l-2
while i < l-1:
    print lign
    i += 1

# ligne l-1 (bord)
print bord

######### Affichage cercle approximatif
r = 10
e = 4
vide = '  '
bord = '**'
x = 0
while x <= 2*r:
    y = 0
    ligne = ''
    while y <= 2*r:
        if abs((x-r)**2 + (y-r)**2 - r**2) < e:
            ligne = ligne + bord
        else:
            ligne = ligne + vide
        y += 1
    print ligne 
    x += 1

############# Suite de Syracuse    
n = 0
u = 15
while n < 20:
    n += 1
    if u % 2 == 0:
        u = u // 2
    else:
        u = 3*u + 1
    print u

    

n = 0
u = 15
while u > 1 and n < 20:
    n += 1
    if u % 2 == 0:
        u = u // 2
    else:
        u = 3*u + 1
print n


m = 0 #max des i(x)
xmax = 0
x = 0
Niter = 30 #nb max d'iterations
X = 50 #plus gde valeur ini suite
while x <= X:
    x += 1
    u = x
    n = 0
    while u > 1 and n < Niter:
        n += 1
        if u % 2 == 0:
            u = u // 2
        else:
            u = 3*u + 1
    if n > m:
        m = n
        xmax = x
print m, xmax
