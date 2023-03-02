def parse(name):
    t = open(f'dane/{name}.txt', 'r').read().split('\n')[:-1]
    header = t[0].split('\t')
    t = [ dict(zip(header, i.split('\t'))) for i in t[1:]]
    globals()[name] = t

parse('marki')
parse('perfumy')
parse('sklad')

#6.1
from collections import defaultdict as dd
sklady = dd(lambda: set())
for i in sklad:
    ind = i['id_perfum']
    sklady[ind].add(i['nazwa_skladnika'].strip())

nazwy = {i['id_perfum']: i['nazwa_p'] for i in perfumy}

ans = set()

for i in sklad:
    ind = i['id_perfum']
    skl = sklady[ind]
    name = nazwy[ind]

    if 'absolut jasminu' in skl: ans.add(name)
print(ans)

#6.2
print()
ans = dd(lambda: (1000000, ''))

for i in perfumy:
    rod = i['rodzina_zapachow']
    np = i['nazwa_p']
    cena = int(i['cena'])

    ans[rod] = min(ans[rod], (cena,np))
ans = sorted(ans.items(), key=lambda x: x[0])
for i in ans:
    print(*i)

#6.3
print()
nazwy_marek = {i['id_marki']:i['nazwa_m'] for i in marki}
ans = dd(lambda: set())

for i in perfumy:
    nm = nazwy_marek[i['id_marki']]
    skladniki = sklady[i['id_perfum']]

    for j in skladniki: ans[nm].add(j)

ans = sorted(ans.items(), key=lambda x: x[0])
for i in ans:
    ok = True
    for j in i[1]:
        if 'paczula' in j: 
            ok = False
            break
    if ok: print(i[0])

#6.4
print()

ans = []

for i in perfumy:
    nm = nazwy_marek[i['id_marki']]
    rod = i['rodzina_zapachow']

    if rod == 'orientalno-drzewna' and nm == 'Mou De Rosine': ans.append( (int(i['cena']) * 0.85,nazwy[i['id_perfum']] ))
ans.sort()
for i in ans:
    print(i[1], round(i[0], 2))

#6.5
print()

ans = dd(lambda: set())
for i in perfumy:
    rod = i['rodzina_zapachow']
    nm = nazwy_marek[i['id_marki']]

    ans[nm].add(rod)
ans = sorted(ans.items(), key=lambda x: x[0])
for i in ans: 
    if len(i[1]) > 1: continue
    print(*i)
    










