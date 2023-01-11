from collections import defaultdict as dd
from datetime import datetime

grupy = open('dane/grupy.txt', 'r').read().split('\n')[:-1]
zawodnicy = open('dane/zawodnicy.txt', 'r').read().split('\n')[:-1]
startujacy = open('dane/startujacy.txt', 'r').read().split('\n')[:-1]
czasy = open('dane/czasy.txt', 'r').read().split('\n')[:-1]

grupy = [dict(zip( grupy[0].split(), i.split('\t'))) for i in grupy[1:]]
zawodnicy = [dict(zip( zawodnicy[0].split(), i.split('\t'))) for i in zawodnicy[1:]]
startujacy = [dict(zip( startujacy[0].split(), i.split('\t'))) for i in startujacy[1:]]
czasy = [dict(zip( czasy[0].split(), i.split('\t'))) for i in czasy[1:]]

#6.1
imiona = {i['id_zawodnika']: i['imie'] + ' ' + i['nazwisko'] for i in zawodnicy}
starty = {i['id_startu']: imiona[ i['id_zawodnika']] for i in startujacy}

from collections import defaultdict as dd
from datetime import datetime, timedelta
ans = dd(lambda:10000000000000000000000000000000)
for i in czasy:
    a = list(map(int, i['czas'].split(':')))
    czas = a[0]*60000 + a[1] * 1000 + a[2]

    ind = starty[ i['id_startu']]
    ans[ind] = min(ans[ind], czas)

ans = sorted(ans.items(), key=lambda x:x[1])[0]
print(ans[0], end =' ')
temp = ans[1]

print(temp//60000,end=':')
temp %=60000
print(temp//1000, end=':')
temp %=1000
print(temp)

#6.2
print()
ans = dd(lambda:set())
for i in startujacy:
    if i['obywatel_kraju'] != 'Polska': continue

    ind = i['id_zawodnika']
    ind = imiona[ind]

    ans[ind].add(i['rok'])
ans = {i:len(ans[i]) for i in ans}
ans = sorted(ans.items(), key=lambda x:x[1])[-1]
print(*ans)

#6.3
print()
ans = dd(lambda: [0,[]])
lata = {i['id_zawodnika']: i['data'] for i in zawodnicy}

for i in startujacy:
    ind = i['id_zawodnika']
    rok = i['rok']
    ur = int(lata[ind].split('-')[0])

    if ur > ans[rok][0]:
        ans[rok][0] = ur
        ans[rok][1] = []
        ans[rok][1].append( imiona[ind])

    elif ur == ans[rok][0]:
        ans[rok][1].append( imiona[ind])

for i in ans:
    print(i, ','.join(ans[i][1]))

#6.4
print()
c = dd(lambda: False)
for i in czasy: c[ i['id_startu']] = True

ans = dd(lambda:0)
for i in startujacy:
    if c[i['id_startu']]: continue

    ans[ i['rok']] += 1
ans = sorted(ans.items(), key=lambda x:x[1])[-1]
print(*ans)

#6.5
print()
ans = dd(lambda: dd(lambda: set()))
nazwy = {i['kod_grupy']: i['nazwa'] for i in grupy}

for i in startujacy:
    rok = i['rok']
    ind = i['kod_grupy']

    ans[rok][ind].add(i ['obywatel_kraju'])
for i in ans:
    for j in ans[i]:
        ans[i][j] = len(ans[i][j])
    ans[i] = [j for j in ans[i] if ans[i][j]==1]
for i in ans:
    print(i, len(ans[i]))

ans = sorted(ans.items(), key=lambda x:len(x[1]))[-1]
temp = ','.join([nazwy[i] for i in ans[1]])
print(ans[0], temp)

#6.6
print()
ans = dd(lambda:set())
for i in startujacy:
    ind = i['id_zawodnika']
    ind = imiona[ind]

    ans[ind].add(i['obywatel_kraju'])

for i in ans:
    if len(ans[i]) == 1: continue

    print(i, '-', ','.join(ans[i]))

