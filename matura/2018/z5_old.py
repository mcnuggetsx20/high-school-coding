file = open('dane/woda.txt', 'r').read().split('\n')[:-1]
file = [i.split('\t') for i in file]

#podpunkt 1
from collections import defaultdict as dd
mp = dd(lambda: 0)

for i in file:
    year = i[0].split('-')[0]
    mp[year] += int(i[1])
ans = sorted(mp.items(), key=lambda j:j[1])[::-1]
print(ans[0][0])


#podpunkt 2
tab =[]
temp = []

for i in file:
    c1 = int(i[1]) < 10**4
    if c1:
        tab.append((temp, len(temp)))
        temp = []
        continue
    temp.append(i)
ans = sorted(tab, key = lambda j:j[1])[::-1][0][0]
print(ans[0][0], ans[-1][0])
print()


#podpunkt 3
mp = dd(lambda:0)

for i in file:
    year = i[0].split('-')[0]
    if year != '2008': continue

    month = i[0].split('-')[1]
    mp[month] += int(i[1])
for i in mp:
    print(i, mp[i])
print()


#podpunkt 4
from math import ceil
wat = 5 * 10**5
first = False
b = 0
for i in file:
    pom = ceil(0.02 *wat)
    b += wat >= 8 * 10**5
    nad = max(0, wat-10**6)
    wat -= nad + pom

    wat += int(i[1])

    if nad and not first:
        print(i[0])
        first = True

print(b)

wat = 5 * 10**5
c = 0
for i in file:
    pom = ceil(0.02 *wat)
    nad = max(0, wat-10**6)
    c = max(c, wat)
    wat -= pom

    wat += int(i[1])
print(c)
