import random

def los(n,p):
    if(p>1):
        print('za duze p')
    tab=[]
    start = 0
    last = 1000
    odd = n-int(n*p)
    for i in range(odd):
        a = 2*random.randint(start, last) - 1
        tab.append(a)
        start = a
        last=a+1000
    start = 0
    last = 1000
    for i in range(n-odd):
        a = 2*random.randint(start, last)
        tab.append(a)
        start = a
        last=a+1000
    return tab

def bsrch(tar):
    global n
    global p
    odd = n-int(n*p)
    tab = los(n, p)
    print(tab)
    if tar%2:
        l=0
        r=odd
    else:
        l = odd
        r=n
    last=-1
    while l <=r:
        m=(l+r)//2
        if m==last:
            break
        if tab[m]<tar:
            l=m
        else:
            r=m
        last=m
    if tab[m]!=tar:
        m+=1
    for i in range(m, len(tab)):
        if tab[i]==tar:
            print(i)
        else:
            break
#tutaj znajduja sie parametry losowania
n=7
p=0.5

#a to wywolanie funkcji znajdywania
bsrch(10)
