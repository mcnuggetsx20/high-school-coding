def a(name):
    file = open(f'dane/{name}.txt', 'r').read().split('\n')
    file = [ dict(zip(file[0].split(';'), i.split(';'))) for i in file[1:]]
    globals()[name] = file

from collections import defaultdict as dd
from datetime import timedelta, datetime
def join(t1, t2, k):
    t2 = dd(lambda: {'missing': ''}) | {i[k]: i for i in t2}
    return [ i | t2[i[k]] for i in t1]

a('maturzysta')
a('przedmioty')
a('zdaje')

#5.1
ans = set()
temp = join(zdaje, przedmioty, 'Id_przedmiotu')
temp = join(temp, maturzysta, 'Id_zdajacego')

for i in temp:
    if i['Nazwa_przedmiotu'] != 'informatyka': continue

    name = i['Nazwisko'] + ' ' + i['Imie']
    ans.add(name)
ans = list(ans)
ans.sort()
for i in ans: print(i)

#5.2
print()
temp = join(zdaje, przedmioty, 'Id_przedmiotu')
ans = dd(lambda: 0)

for i in temp:
    if i['Typ'] != 'dodatkowy': continue
    p = i['Nazwa_przedmiotu']
    ans[p] += 1
ans = sorted(ans.items(), key=lambda x: x[1])[-1]
print(*ans)

#5.3
print()
temp = join(zdaje, przedmioty, 'Id_przedmiotu')
temp = join(temp, maturzysta, 'Id_zdajacego')
ans = dd(lambda: 0)

for i in temp:
    if i['Typ'] != 'dodatkowy': continue
    name = i['Nazwisko'] + ' ' + i['Imie']
    ans[name] += 1
ans = sorted(ans.items(), key=lambda x: x[1])
for i in ans: 
    if i[1] == ans[-1][1]: print(*i)

#5.4
print()
temp = join(przedmioty, zdaje, 'Id_przedmiotu')
for i in temp: 
    print(i)
    if 'missing' in i.keys(): print(i['Nazwa_przedmiotu'])

#5.5
print()
temp = join(zdaje, maturzysta, 'Id_zdajacego')
temp = join(temp, przedmioty, 'Id_przedmiotu')
ans = dd(lambda: [10**9, []])
base = datetime.strptime('2020-01-01', '%Y-%m-%d')
for i in temp:
    name = i['Imie'] + ' ' + i['Nazwisko']
    data = datetime.strptime(i['Data_urodzenia'], '%Y-%m-%d')
    age = abs(base - data).days
    ans[name][0] = age
    if i['Typ'] != 'dodatkowy': continue
    ans[name][1].append(i['Nazwa_przedmiotu'])
ans = sorted(ans.items(), key= lambda x:x[1][0])[0]
print(ans)

#5.6
print()
temp = join(zdaje, maturzysta, 'Id_zdajacego')
ans = set()
for i in temp: 
    if not (int(i['PESEL'][-2]) %2): continue
    ans.add(i['Id_zdajacego'])
print(len(ans))







