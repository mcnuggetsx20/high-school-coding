jezyki = open('dane/jezyki.txt','r').read().split('\n')[:-1]
panstwa = open('dane/panstwa.txt','r').read().split('\n')[:-1]
uzytkownicy = open('dane/uzytkownicy.txt','r').read().split('\n')[:-1]

jezyki = [ dict(zip( jezyki[0].split('\t'), i.split('\t'))) for i in jezyki[1:]]
panstwa = [ dict(zip( panstwa[0].split('\t'), i.split('\t'))) for i in panstwa[1:]]
uzytkownicy = [ dict(zip( uzytkownicy[0].split('\t'), i.split('\t'))) for i in uzytkownicy[1:]]

#5.1
from collections import defaultdict as dd

ans = dd(lambda:0)
for i in jezyki:
    ans[ i['Rodzina'] ] += 1
ans = sorted(ans.items(),key=lambda x:x[1])[::-1]
for i in ans: print(*i)

#5.2
print()

ans = set()
for i in uzytkownicy:
    if i['Urzedowy']=='nie':continue
    ans.add( i['Jezyk'])

print(len(jezyki) - len(ans))

#5.3
print()

k = {i['Panstwo']: i['Kontynent'] for i in panstwa}
ans = dd(lambda:set())
for i in uzytkownicy:
    p = i['Panstwo']
    j = i['Jezyk']
    kont=  k[p]
    ans[j].add(kont)

for i in ans:
    if len(ans[i])>=4: print(i)

#5.4
print()
rodziny = {i['Jezyk']: i['Rodzina'] for i in jezyki}
ans = dd(lambda:0)

for i in uzytkownicy:
    j = i['Jezyk']
    p = i['Panstwo']
    rod = rodziny[j]

    kont = k[p]
    if rod == 'indoeuropejska' or kont not in ['Ameryka Polnocna', 'Ameryka Poludniowa']: continue
    ans[j] += float(i['Uzytkownicy'].replace(',', '.'))

ans = sorted(ans.items(), key=lambda j:j[1])[::-1][:6]
for i in ans:
    print(i[0], rodziny[i[0]], round(i[1], 2))

#5.5
print()
popus = {i['Panstwo']:i['Populacja'] for i in panstwa}
ans = []

for i in uzytkownicy:
    if i['Urzedowy'] == 'tak': continue
    p = i['Panstwo']
    pop = float(popus[p].replace(',','.'))
    uz = float(i['Uzytkownicy'].replace(',','.'))

    temp = uz/pop
    if temp < 0.3:continue
    j = i['Jezyk']
    ans.append( (p, j, round(temp *100, 2)) )
for i in ans: print(*i)

    










