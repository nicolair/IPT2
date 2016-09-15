def valeurMax(lili):
    vmax = lili[0]
    for v in lili:
      if vmax < v:
        vmax = v
    return vmax

def indicesValeurMax(lili):
    vmax = lili[0]
    livm = [0]
    i = 1 
    l = len(lili)
    while i < l:
      if lili[i] > vmax:
        livm = [i]
      elif lili[i] == vmax:
        livm.append(i)
      i += 1
    print livm
    return livm

L = [0, 4 ,5,7,6,8,1,4]
print valeurMax(L)

print indicesValeurMax(L)