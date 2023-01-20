def parse(name):
    tab = open(f'dane/{name}.txt', 'r').read().split('\n')[:-1]
    tab = [ dict(zip(tab[0].split('\t'), i.split('\t'))) for i in tab[1:]]
    globals()[name] = tab

parse('klienci')
parse('pokoje')
parse('noclegi')

#5.1
from collections import defaultdict as dd
from datetime import datetime
ans = dd(lambda:0)

imiona = { i['nr_dowodu'] : i['imie'] + ' ' + i['nazwisko'] for i in klienci}

for i in noclegi:
    ind = i['nr_dowodu']
    p = datetime.strptime(i['data_przyjazdu'], '%Y-%m-%d')
    w = datetime.strptime(i['data_wyjazdu'], '%Y-%m-%d')

    diff = abs(p-w).days
    ans[ imiona[ind]] += diff

ans = sorted(ans.items(), key=lambda x:x[1])
print(*ans[-1])

#5.2
print()
ans = dd(lambda:0)

cennik = { i['nr_pokoju'] : int(i['cena']) for i in pokoje }

for i in noclegi:
    ind = i['nr_dowodu']
    p = datetime.strptime(i['data_przyjazdu'], '%Y-%m-%d')
    w = datetime.strptime(i['data_wyjazdu'], '%Y-%m-%d')

    diff = abs(p-w).days
    cena = cennik[ i['nr_pokoju'] ] * diff

    imie = imiona[ind]
    ans[imie] += cena

for i in ans:
    if ans[i] > 2000: print(i)

#5.3
print()
s = { i['nr_pokoju'] : i['standard'] for i in pokoje }
m = { i['nr_dowodu'] : i['miejscowosc'] for i in klienci }
ans = set()

for i in noclegi:
    ind = i['nr_dowodu']
    miej = m[ind]
    stand = s[ i['nr_pokoju']]
    if stand != 'N' or miej.strip() in ['Opole', 'Katowice']: ans.add( i['nr_pokoju'])

for i in pokoje:
    if i['nr_pokoju'] not in ans: print(i['nr_pokoju'])

