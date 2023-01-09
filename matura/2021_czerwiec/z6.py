zespoly = open('dane/zespoly.txt', 'r').read().split('\n')
miasta = open('dane/miasta.txt', 'r').read().split('\n')
koncerty = open('dane/koncerty.txt', 'r').read().split('\n')

zespoly = [ dict(zip(zespoly[0].split(';'), i.split(';'))) for i in zespoly ][1:]
miasta = [ dict(zip(miasta[0].split(';'), i.split(';'))) for i in miasta ][1:-1]
koncerty = [ dict(zip(koncerty[0].split(';'), i.split(';'))) for i in koncerty ][1:-1]

#6.1
ans = 0
for i in koncerty:
    data = i['data'].split('-')[1]
    ans += data == '07'
print(ans)
print()

#6.2
from collections import defaultdict as dd
km = dict()
z = dict()
ans = dd(lambda:set())
mx = 0

for i in miasta:
    km[ i['kod_miasta'] ] = i['miasto']

for i in zespoly:
    z[ i['id_zespolu'] ] = int(i['liczba_artystow'])

for i in koncerty:
    ind = i['kod_miasta']
    miasto = km[ind]

    ind = i['id_zespolu']

    ans[miasto].add(ind)

for i in ans:
    v = ans[i]
    temp = 0
    for j in v:
        temp += z[j]
    ans[i] = temp
    mx = max(mx, temp)

ans = sorted(ans.items(), key=lambda x:x[1])[::-1]

for i in ans:
    if i[1] ==mx: print(*i)
print()

#6.3

woj = dict()
ans = dd(lambda:0)
mp = dd(lambda:0)
for i in miasta:
    woj[ i['kod_miasta'] ] = i['wojewodztwo']
    mp[ i['wojewodztwo'] ] += 1

for i in koncerty:
    kod = i['kod_miasta']
    w = woj[kod]
    ans[w] += 1

for i in ans:
    ans[i] = round(ans[i] / (mp[i]), 2)
ans = sorted(ans.items(), key=lambda x:x[1])[::-1]
for i in ans:
    print(*i)


#6.4
print()

daty = [i for i in range(20, 26)]

ans = set()
nazwy = dict()

for i in zespoly:
    nazwy[ i['id_zespolu'] ] = i['nazwa']

for i in koncerty:
    data = i['data'].split('-')
    if data[1] != '07' or int(data[2]) not in daty: continue

    ind = i['id_zespolu']
    ans.add(ind)

for i in zespoly:
    if i['id_zespolu'] in ans: continue

    print(i['nazwa'])
    
#6.5
print()

ans = dd(lambda: [0,0])
from datetime import datetime
for i in koncerty:
    data = datetime.strptime(i['data'], '%Y-%m-%d')
    ok = data.weekday() in [5, 6]
    
    ind = i['id_zespolu']
    nazwa = nazwy[ind]

    ans[nazwa][ok] += 1

for i in ans:
    if ans[i][0] > ans[i][1]: continue
    print(i, *ans[i][::-1])






