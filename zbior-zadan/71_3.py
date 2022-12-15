from math import floor
file = open('dane/71/funkcja.txt', 'r').read().split('\n')[:-1]
file = [ [float(i) for i in i.split()][::-1] for i in file]

def WartoscFunkcji(x):
    global file
    ind = file[floor(x)]
    a= ind[0]
    b= ind[1]
    c= ind[2]
    d= ind[3]

    return a*x**3 + b*x**2 + c*x + d

def ZnajdzMscZerowe():
    ToReturn = []
    Start = WartoscFunkcji(0)
    for i in range (0, 5*10**6):
        Teraz = WartoscFunkcji(i/10**6)
        if Teraz*Start < 0:
            ToReturn.append(i/10**6)
        Start = Teraz
    return ToReturn

print(ZnajdzMscZerowe())

