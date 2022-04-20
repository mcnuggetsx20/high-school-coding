kody = open('Dane_2203/kody.txt', 'r').read().split('\n')[1:-1]
przyb = open('Dane_2203/przybycia.txt', 'r').read().split('\n')[1:]

mpst = dict()
ans = dict()

for i in range(len(kody)):
    kody[i] = kody[i].split(';')
    mpst[kody[i][0]] = kody[i][2]

for i in range(len(przyb)):
    przyb[i] = przyb[i].split(';')

for i in przyb:
    nab = i[-1]
    ans[nab]=False

for i in przyb:
    nab = i[-1]
    ban = i[-2]
    if mpst[ban] == 'EUROPA':
        ans[nab] = True

for i in sorted(ans.keys()):
    if not ans[i]:
        print(i)





