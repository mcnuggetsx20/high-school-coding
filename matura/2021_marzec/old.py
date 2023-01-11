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
imiona = {i['id_zawodnika'] : i['imie'] + ' ' + i['nazwisko'] for i in zawodnicy}
starty = {i['id_startu'] : imiona[ i['id_zawodnika']] for i in startujacy}

ans = dd(lambda: 10000000000000000000000000000000)

for i in czasy:
    c = list(map(int,i['czas'].split(':')))
    ind = i['id_startu']
    
    temp = 60000 * c[0] + 1000*c[1] +  c[2]

    ans[ind] = min(ans[ind], temp)
ans = sorted(ans.items(), key=lambda x:x[1])[0]

temp = ans[1]
print(temp//60000)
temp %=60000
print(temp//1000)
temp %=1000
print(temp)

print(starty[ans[0]], ans[1])

#6.2
print()
ans = dd(lambda:set())
for i in startujacy:
    if i['obywatel_kraju'] != 'Polska': continue

    ind = i['id_zawodnika']
    ans[ind].add(i['rok'])

ans = { i: len(ans[i]) for i in ans}
ans = sorted(ans.items(), key = lambda x:x[1])[-1]
print(imiona[ans[0]], ans[1])

#6.3
print()
ans= dd(lambda: [0,[]])
uro = {i['id_zawodnika']: i['data'] for i in zawodnicy}

for i in startujacy:
    ind = i['id_zawodnika']
    u = int(uro[ind].split('-')[0])
    rok = i['rok']

    if ans[rok][0] < u:
        ans[rok][0] = u
        ans[rok][1]= [imiona[ind]]

    elif ans[rok][0] == u:
        ans[rok][1].append(imiona[ind])
for i in ans:
    print(i, ans[i])

#6.4
print()
ans = dd(lambda:0)
c= [i['id_startu'] for i in czasy]

for i in startujacy:
    rok = i['rok']
    if i['id_startu'] in c: continue

    grupa = i['kod_grupy']
    ans[rok] += 1

ans = sorted(ans.items(), key = lambda x:x[1])[-1]
print(ans)

#6.5
print()
ans = dd(lambda: dd(lambda: set()))
for i in startujacy:
    rok = i['rok']
    kraj = i['obywatel_kraju']
    grupa = i['kod_grupy']

    ans[rok][grupa].add(kraj)
for i in ans:
    ans[i] = [j for j in ans[i] if len(ans[i][j])==1]
    ans[i] = (ans[i], len(ans[i]))

nazwy = {i['kod_grupy']: i['nazwa'] for i in grupy}

for i in ans:
    print(i, ans[i])

ans = sorted(ans.items(), key=lambda i: i[1][1])[-1]
print(ans[0],end=' ')
for i in ans[1][0]:
    print(nazwy[i], end=', ')
print()









