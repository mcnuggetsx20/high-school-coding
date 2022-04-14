from math import *
def f(x):
    return sin(x**2 - x + 1/3)+x/2

a=-3
b=1
prec = 0.00001
mx = 20 

if(f(a)*f(b)>0):
    print('zla funkcja')
    exit()

while mx:
    x = (f(a)*b - f(b)*a)/(f(a)-f(b))
    v = f(x)
    if abs(v) <=prec:
        print(x)
        break
    if(v > 0):
        b=x
    else:
        a=x
    mx-=1






