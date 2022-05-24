statki = open('Dane_2203/statki.txt', 'r').read().split('\n')[1:-1]
przyb = open('Dane_2203/przybycia.txt', 'r').read().split('\n')[1:]

mpst = dict()
ans = dict()

for i in range(len(statki)):
    statki[i] = statki[i].split(';')
    mpst[statki[i][0]] = statki[i][1:]

for i in range(len(przyb)):
    przyb[i] = przyb[i].split(';')

for i in przyb:
    a = i[-1]
    imo = i[2]
    if a not in ans.keys():
        ans[a] = ['',0]

    if int(mpst[imo][1]) > ans[a][1]:
        ans[a][1] = int(mpst[imo][1])
        ans[a][0] = mpst[imo][0]

for i in sorted(ans.keys()):
    print(i, ans[i])





