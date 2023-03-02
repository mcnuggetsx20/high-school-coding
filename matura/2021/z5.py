file = open('dane/wodociagi.txt', 'r').read().split('\n')[:-1]
file = [i.split(';') for i in file[1:]]

mp = dict()

for i in file:
    m = int(i[0][5:7])
    temp = round(sum(list(map(int, i[1:]))) / m, 2)


    ind = i[0][:5]
    mp[ind] = temp

mp = sorted(mp.items(), key = lambda x:x[1])[::-1][:10]
for i in mp:
    print(*i)


#5.2
print()
from collections import defaultdict as dd
ans = dd(lambda: 0)

for i in file:
    kod = i[0][-3:]
    temp = sum(list(map(int, i[1:])))
    ans[kod] += temp
for i in ans:
    print(i, ans[i])

#5.3
from math import log, ceil
print()
ans = dd(lambda: dd(lambda: 0))

for i in file:
    kod = i[0][-3:]
    temp = list(map(int, i[1:]))
    for j, v in enumerate(temp):
        ans[kod][j] += v

for i in ans:
    temp = [ans[i][j] for j in ans[i]]
    mx = max(temp)
    print(i, mx)

#5.4
print()

ans = dd(lambda: 0)
for i in file:
    temp = list(map(int, i[1:]))
    for j, v in enumerate(temp):
        ans[j] += v

tab = []
for i in range(12):
    #pierwsza taka wartosc to nty element ciagu geom.
    #my mamy policzyc za ile lat to sie wydarzy czyli jakby jestesmy na 1 elemencie teraz, wiec odejmujemy 1 od wylicznej wartosci n
    n = ceil(log( (160000/ans[i]), 1.01) + 1) - 1
    tab.append( (2019+n, i+1))
    
tab.sort()
print(*tab[0])

#jebane gowno
for j in range(1,12):
    print(2019+j, end = ': ')
    for i in ans:
        ans[i] = ceil(ans[i] * 1.01)
        print(ans[i], end=' ')
    print()

#5.5
print()
p = [160000 + (i*1000) for i in range(1, 100)]
p = [160000] * 2 + p

ans = dd(lambda: 0)
for i in file:
    temp = list(map(int, i[1:]))
    for j, v in enumerate(temp):
        ans[j] += v

for i in range(12):
    temp = [ans[i]]
    for j in range(1, 50):
        temp.append( ceil(1.01 * temp[j-1]))
        if temp[-1] > p[j]:
            print(2019+j, i+1)
            break



