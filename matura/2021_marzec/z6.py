def parse(name):
    tab = open(f'dane/{name}.txt', 'r').read().split('\n')[:-1]
    tab = [dict(zip(tab[0].split('\t'), i.split('\t'))) for i in tab[1:]]
    globals()[name] = tab
    return

parse('grupy')
parse('czasy')
parse('startujacy')
parse('zawodnicy')

#6.1

imiona1 = {i['id_zawodnika']:i['imie'] + ' ' + i['nazwisko'] for i in zawodnicy}
imiona = {i['id_startu']: imiona1[i['id_zawodnika']] for i in startujacy}

from collections import defaultdict as dd
ans = dd(lambda:10**10)

for i in czasy:
    ind = i['id_startu']
    czas = i['czas'].split(':')
    czas = 60000 * int(czas[0]) + 1000*int(czas[1]) + int(czas[-1])
    imie = imiona[ind]
    ans[imie] = min(ans[imie], czas)
ans = sorted(ans.items(), key=lambda x:x[1])
print(*ans[0])

ans = dd(lambda:0)
#6.2
for i in startujacy:
    ind = i['id_zawodnika']
    kraj = i['obywatel_kraju']
    if kraj != 'Polska': continue
    ans[ind] += 1

ans = sorted(ans.items(), key=lambda x:x[1])[-1]
print(imiona1[ans[0]], ans[1])

#6.3
print()
wiek = {i['id_zawodnika']: int(i['data'].split('-')[0]) for i in zawodnicy}

ans = dd(lambda:[])

for i in startujacy:
    rok = int(i['rok'])
    zaw = i['id_zawodnika']
    age = rok - wiek[zaw]

    ans[rok].append( (age, zaw))
for i in ans:
    print(i)
    ans[i].sort()
    for j in ans[i]:
        if j[0] != ans[i][0][0]: continue
        print(imiona1[j[1]])
    print()

#6.4
print()
c = [i['id_startu'] for i in czasy]
ans = dd(lambda:0)

for i in startujacy:
    ind = i['id_startu']
    rok = i['rok']
    if ind in c: continue
    ans[rok] += 1

ans = sorted(ans.items(), key=lambda x:x[1])
print(*ans[-1])

#6.5
print()
g = {i['kod_grupy']: i['nazwa'] for i in grupy}

ans = dd(lambda: dd(lambda:set()))
ans2 = dd(lambda: [])
for i in startujacy:
    gr= i['kod_grupy']
    rok = i['rok']
    kraj = i['obywatel_kraju']

    ans[rok][gr].add(kraj)
for i in ans:
    for j in ans[i]:
        if len(ans[i][j]) != 1: continue
        ans2[i].append(g[j])

ans = sorted(ans2.items(), key=lambda x: x[0])

for i in ans:
    print(i[0], len(i[1]))

ans2 = sorted(ans2.items(), key=lambda x: len(x[1]))
print(*ans2[-1])

#6.6
print()

ans = dd(lambda: set())

for i in startujacy:
    ind = i['id_zawodnika']
    kraj = i['obywatel_kraju']
    ans[ind].add(kraj)

for i in ans:
    if len(ans[i])==1: continue
    print(f'{imiona1[i]}: {ans[i]}')




