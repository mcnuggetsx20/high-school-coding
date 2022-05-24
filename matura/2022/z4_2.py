file = open('Dane_2205/liczby.txt', 'r').read().split()

def factorize(n):
    ans = 0
    tab = set()
    i = 2
    while(i*i <=n):
        while(not(n%i)):
            ans +=1
            tab.add(i)
            n/=i
        i+=1
    if n > 1:
        ans +=1
        tab.add(n)
    return [ans, len(tab)]

mx = 0
ans1 = 0
ans2 = 0
mx2 = 0
for i in file:
    comp = factorize(int(i))
    a = comp[0]
    b = comp[1]

    ans1 = [ans1, i][int(a>mx)]
    mx = max(mx, a)

    ans2 = [ans2, i][int(b>mx2)]
    mx2=max(mx2,b)
print(mx, ans1)
print(mx2, ans2)


