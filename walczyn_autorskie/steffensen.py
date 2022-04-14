from math import *
def f(x):
    return sin(x**2 - x + 1/3)+x/2

x=-1
mx=20
prec=0.00001
while mx:
    h=f(x)
    if abs(h) <=prec:
        print(x)
        break;
    g = (f(x+h)-h)/h
    x1 = x
    x = x- (h/g)
    if(abs(x1-x)<=prec):
        print(x)
        break;
    mx-=1








