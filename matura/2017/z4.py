with open('dane/cennik.txt', 'r') as file:
    cennik = file.read().split('\n')[:-1]
cennik = [i.split() for i in cennik]
cennik = { i[0] : float(i[1].replace(',', '.')) for i in cennik}

with open('dane/cukier.txt', 'r') as file:
    cukier = file.read().split('\n')[:-1]
cukier = [i.split() for i in cukier]

from collections import defaultdict
from math import ceil

mp = defaultdict(lambda: 0)

def disc(n):
    return  bool(n//10000) * 10 + bool(n//1000) * 5 + bool(n//100) * 5

ans2 = 0
zest = defaultdict(lambda: 0)
rab = defaultdict(lambda: 0)
ans3 = 0
ans4 = 0
c = 5000

for v, i in enumerate(cukier):
    il = int(i[2])
    rab[i[1]] += il
    mp[i[1]] += il
    y = i[0].split('-')[0]
    ans2 += il * cennik[y]

    zest[y] += il

    ans3 += disc(rab[i[1]]) * il

    c -= il
    try:
        if cukier[v+1][0].split('-')[1]!= i[0].split('-')[1]:
            diff = 5000 - c
            c += ceil(diff/1000)*1000
            ans4 += ceil(diff/1000)>=4

    except IndexError:
        pass

diff = 5000 - c
c += ceil(diff/1000)*1000
ans4 += ceil(diff/1000)>=4

for i in sorted(mp.items(), key =lambda x: x[1], reverse=True)[:3]:
    print(i)

print(ans2)

for i in zest:
    print(zest[i], '\t', i)

print(ans3/100)
print(ans4)
