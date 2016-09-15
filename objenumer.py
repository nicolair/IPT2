stringy = 'tagada + 2pi'
print(type(stringy))
lili = ["riri","fifi","loulou",type]
print(type(lili))
# on peut tout mettre dans une liste!
# mais pas vraiment utile.
rangy = range(5)
print(rangy)
print(type(rangy))
# executer aussi en python 2


tutu = "machin", 4, stringy , type
print(type(tutu))
# on peut tout mettre dans un tuple!
cloclo = {1,2,2}
print(type(cloclo))
print(cloclo)
notes = {"riri":10.1, "fifi":15, "loulou":0.7}
print(type(notes))



# executer en P2 ou P3
lili = range(5)
fifi = lili
fifi[3] = 54555
print(lili)
stringy = "meuh meuh"
chacha = stringy
chacha[3] = "B"
print(chacha)
# lili mauvais nom assigner une vraie liste

truc = "tagada"
for charly in truc:
    print(charly)
for i in range(5):
  print(i)
n = 5 ; f = 1
for i in range(5):
  f *= i
print(f)


st = "L'apostrophe ' est ennuyeux. " 
st = st + 'Le guillemet " perturbe'
print(st)
#echappement
st = "meli melo \"' '\" melo meli"
print(st)


st = "L'apostrophe ' est ennuyeux."
l = len(st)
print(st[3])
print(st[l - 3])
print(st[-3])
stringounet = st[0:5]
print(stringounet)
print(st[5:])
print(st[5:-2])


st = "L'apostrophe ' est ennuyeux."
stringounet = "e ' e"
print(stringounet in st)

lili = [1,2]
superlili = lili*4
print(superlili)


n = 4
MId= [[0 for j in range(n)] for i in range(n)]
print(MatId)
for i in range(n):
    MatId[i][i] = 1
print(MatId)

ligne = [1, 2 , 3, 4]
matrice = [ ligne for i in range(4)]
print(matrice)
print(matrice[1][2])
matrice[1][2] = "tagada"
print(matrice)