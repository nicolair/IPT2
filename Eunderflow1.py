x = 2.0
xx = 2.5
y = 2.
i = 0
while  xx != y :
    x , xx = xx , 2.5 * xx - x
    y *= 2
    print(xx,y,xx - y)
    i += 1
print(i)
"""
grand = 1.
petit = 1.
while x - xx != 0:
    x = 2.**i + 2.**(-i)
    xx = 2.**(i+1) + 2.**(-i-1)
    i += 1
print(i)
"""