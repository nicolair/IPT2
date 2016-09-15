nini = 25
n = nini
mot = "."
while n > 0:
  mot = str(n % 2) + mot
  n = n // 2
print('0b'+mot)
print(bin(nini))


n = 25
e = 0
while n > 0:
  if n % 2 == 1:
    print(e)
  n = n // 2
  e += 1


n = 250 ; a = 7
p = a ; x = 1
while n > 0:
  if n % 2 == 1:
    x = x*p
  n = n // 2
  p = p*p
print(x) 



n = 250 ; a = 7
p = a ; x = 1 ; c = 1
while n > 0:
  if n % 2 == 1:
    x = x*p ; c += 1
  n = n // 2
  p = p*p ; c += 1
print(c) 
