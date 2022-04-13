from math import *

r =10
l= -10
prec = 0.00001

def f(m):
    return sin(m**2 - m + 1/3) + m/2

if(f(l) * f(r) > 0):
    print("Niestety zla funkcja")
    exit()

while(True):
    m = (l+r)/2
    y = f(m)
    if(abs(y - 0) <= prec):
        print(m)
        break
    elif(y < 0):
        l = m
    elif(y > 0):
        r = m




