kluby = open('dane/kluby.txt', 'r').read().split('\n')[:-1]
sedziowie = open('dane/sedziowie.txt', 'r').read().split('\n')[:-1]
mecze = open('dane/mecze.txt', 'r').read().split('\n')[:-1]

kluby = [dict(list(zip(kluby[0].split(';'), i.split(';'))))  for i in kluby][1:]
sedziowie = [dict(list(zip(sedziowie[0].split(';'), i.split(';'))))  for i in sedziowie][1:]
mecze = [dict(list(zip(mecze[0].split(';'), i.split(';'))))  for i in mecze][1:]

#6.1
ans = 0
for i in mecze:
    ans += int(i['Sety_wygrane']) + int(i['Sety_przegrane']) == 5
print(ans)
print()

#6.2

from collections import defaultdict as dd
miasta = dict()

for i in kluby:
    miasta[ i['Id_klubu'] ] = i['Miasto']

ans = dd(lambda: 0)
for i in mecze:
    ind = i['Id_klubu']
    miasto = miasta[ind]
    ans[miasto] += 1

ans = sorted(ans.items(), key=lambda x:x[1])[::-1]
for i in ans:
    print( *i)
print()

#6.3

sedz = dict()
for i in sedziowie:
    sedz[ i['Id_sedziego'] ] = i['Imie'] + ' '+ i['Nazwisko']

av = 0
ans = dd(lambda:0)
for i in mecze:
    ind = i['Id_sedziego']
    sedzia = sedz[ind]
    ans[sedzia] += 1
    av += 1

av /= len(ans)

for i in ans:
    if ans[i] > av:
        print(i)
print()

#6.4
end = '2019-12-17'
tab = set()

test = '2019-11-12'
for i in mecze:
    if i['Data'] == end:
        break

    ind = i['Id_klubu']
    miasto = miasta[ind]

    if miasto.strip() in ['Licowo', 'Szymbark']:
        tab.add(i['Id_sedziego'])

for i in sedz:
    if i in tab: continue
    print(sedz[i])
print()

#6.5
kl = dict()
for i in kluby:
    ind = i['Id_klubu']
    kl[ind] = i['Nazwa']

ans = dd(lambda: [0]*2)
for i in mecze:
    ind = i['Id_klubu']
    win = int(i['Sety_wygrane']) > int(i['Sety_przegrane'])
    ans[ind][not win] += 1

for i in ans:
    if ans[i][0] < ans[i][1]: continue
    nazwa = kl[i]
    miasto = miasta[i]
    print(nazwa, miasto, *ans[i])







