dane_ankiet = open('dane/dane_ankiet.txt','r').read().split('\n')[:-1]
lok = open('dane/lok.txt','r').read().split('\n')[:-1]
zain = open('dane/zain.txt','r').read().split('\n')[:-1]

dane_ankiet = [dict(zip(dane_ankiet[0].split('\t'), i.split('\t'))) for i in dane_ankiet][1:]
lok = [dict(zip(lok[0].split('\t'), i.split('\t'))) for i in lok][1:]
zain = [dict(zip(zain[0].split('\t'), i.split('\t'))) for i in zain][1:]

#6.1
m = 0
k = 0

for i in dane_ankiet:
    imie = i['Imie'][-1]
    k += imie == 'a'
    m += imie != 'a'
print(k, m)

#6.2
print()
from collections import defaultdict as dd
ans = dd(lambda:0)
woj = {i['Id']: i['Wojewodztwo'] for i in dane_ankiet}

for i in lok:
    ind = i['Id']
    #print(woj[ind], ind)

    ok = (woj[ind] == 'Mazowieckie') and (i['Pora_roku'].strip() == 'lato')
    if not ok: continue

    srodek = i['Srod_lok']

    ans[srodek] += 1

for i in ans:
    print(i,ans[i])

#6.3
print()
ans = dd(lambda:0)
for i in dane_ankiet:
    w = woj[ i['Id']]
    ans[w] += 1
for i in ans:
    if ans[i] > 20:
        print(i, ans[i])

#6.4
print()
inf = {i['Id']: (i['Nazwisko'] + ' ' +i['Imie'], int(i['Wiek']), i['Wyksztalcenie'], i['Dochod']) for i in dane_ankiet}
tab = dd(lambda: [])
for i in zain:
    ind = i['Id']
    #if i['Zainteresowania'] in ['informatyka','gry komputerowe'] or inf[ind][1] <= 50 or ind[ind][2] not in ['wyzsze', 'srednie']: continue
    tab[ind].append(i['Zainteresowania'])

ans = []
for i in tab:
    v = tab[i]
    ind = i
    if 'informatyka' in v or 'gry komputerowe' in v or inf[ind][1] <= 50 or inf[ind][2] not in ['wyzsze', 'srednie']: continue
    ans.append( inf[ind][0]+ ': ' + woj[ind])

ans.sort()
for i in ans:
    print(i)

#6.5
print()
tab = dd(lambda: False)
for i in lok:
    ind= i['Id']
    if i['Srod_lok'] == 'rower': tab[ind] = True

s = 0
d = 0
for i in dane_ankiet:
    ind = i['Id']
    if woj[ind] != 'Zachodniopomorskie' or not tab[ind] or i['Imie'][-1] != 'a': continue
    s += int(i['Dochod'])
    d +=1
print(s/d)





