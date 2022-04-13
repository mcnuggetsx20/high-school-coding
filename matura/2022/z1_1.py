file = open('Dane_2203/szachy.txt', 'r').read().split('\n\n')[:-1]
tab = []
mx=0
ans =0

for i in file:
    tab.append(i.split())

for i in range(len(tab)):
    c=0
    for k in range(8):
        ok = True
        for j in tab[i]:
            if j[k] != '.':
                ok=False
            if not ok:
                break
        if ok:
            c+=1
    mx = max(mx, c)
    ans += int(bool(c))
print(ans, mx)





