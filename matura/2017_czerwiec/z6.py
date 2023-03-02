def f(name):
    file = open(f'dane/{name}.txt' ,'r').read().split('\n')[:-1]
    file = [dict(zip(file[0].split('\t'), i.split('\t'))) for i in file[1:]]
    globals()[name] = file

f('zestawy')
f('pakiety')
f('programy')

from collections import defaultdict as dd
zaw = dd(lambda:set())

for i in zestawy:
    pak = i['Id_pakietu']
    pro = i['Id_programu']
    zaw[pro].add(pak)

for i in programy:
    rodz = i['rodzaj']
    if rodz != 'edytor dokumentow tekstowych': continue

    ind = i['Id_programu']
    if len(zaw[ind]) < 2: continue
    print(i['program'], i['cena'], len(zaw[ind]))

#6.2
print()
nazwy_pak = {i['Id_pakietu']: i['nazwa_pakietu'] for i in pakiety}
ans = set()
temp = []
for i in programy:
    ind = i['Id_programu']
    if 'zarzadzanie' in i['rodzaj']: temp.append(ind)

for i in zestawy:
    if i['Id_programu'] in temp:
        ans.add(i['Id_pakietu'])

for i in ans:
    print(nazwy_pak[i])

#6.3
print()
zaw1 = dd(lambda: list())
for i in zestawy:
    zaw1[i['Id_pakietu']].append(i['Id_programu'])

ceny = {i['Id_programu']: int(i['cena']) for i in programy}
ans = dd(lambda: 0)

for i in zaw1:
    for j in zaw1[i]:
        ans[i] += ceny[j]
ans = sorted(ans.items(), key = lambda x: x[1])[-3:][::-1]
firmy ={i['Id_pakietu']: i['firma'] for i in pakiety}

for i in ans:
    print(nazwy_pak[i[0]], firmy[i[0]], i[1])

#6.4
print()
for i in programy:
    if i['Id_programu'] not in zaw: print(i['program'])

#6.5
print()
ans = dd(lambda: [0, 0])
for i in pakiety:
    ind = i['Id_pakietu']
    name = nazwy_pak[ind]
    temp = zaw1[i['Id_pakietu']]
    a, b = False, False
    for j in temp:
        cena = ceny[j]
        ans[name][0] += not cena
        ans[name][1] += bool(cena)
print('#nazwa/darmowe/komercyjne')
for i in ans:
    if ans[i][0] and ans[i][1]: print(i, ans[i])




