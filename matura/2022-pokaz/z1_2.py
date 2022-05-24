file = open('Dane_2203/szachy.txt', 'r').read().split('\n\n')[:-1]
tab = []
mn=10**9
ans = 0

for i in file:
    tab.append(i.split())

for i in tab:
    temp=[]
    ok = True
    for j in i:
        for k in j:
            if k !='.':
                temp.append(k)
    for j in temp:
        if temp.count(j)!=temp.count(j.upper()):
            ok =False
            break
    if ok:
        ans += 1
        mn = min(mn, len(temp))
    
print(ans, mn)








