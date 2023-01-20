def parse(name):
    tab = open(f'dane/{name}.txt', 'r').read().split('\n')[:-1]
    tab = [ dict(zip(tab[0].split('\t'), i.split('\t'))) for i in tab[1:]]
    globals()[name] = tab

parse('klienci')
parse('agenci')
parse('oferta')
parse('zainteresowanie')

#6.1
imiona = {i['Id_agenta'] : f"{i['Imie']} {i['Nazwisko']}" for i in agenci}
ag = {i['Id_oferty'] : i['Id_agenta'] for i in oferta}

from collections import defaultdict as dd
ans = dd(lambda:0)
for i in zainteresowanie:
    ind = i['Id_oferty']
    ans[ind] += 1
ans = sorted(ans.items(), key=lambda x:x[1])[-1]
print(imiona[ag[ans[0]]], ans[0])

#6.2
print()
ans = dd(lambda:[0,0])
w = set()
for i in oferta:
    c = int(i['Cena'])
    ind= i['Woj ']
    ans[ind][0] += c
    ans[ind][1] += 1
    w.add(ind)
w = list(w)
w.sort()
for i in w:
    print(i, round(ans[i][0]/ans[i][1],2))

#6.3
print()

for i in oferta:
    bas = i['Id_oferty'].strip()[-2:] == 'MT'
    st = i['Status'].strip() == 'A'
    if not bas or not st: continue

    ind = i['Id_oferty']
    name = imiona[ag[ind]]
    print(ind, name, i['Woj '], i['Pow'], i['Cena'])

#6.4
print()

tab = set()
for i in oferta:
    y = i['Data_zglosz'].split('-')[0] == '2017'
    st = i['Status'].strip() == 'S'
    if not y or not st: continue

    tab.add(i['Id_agenta'])

for i in agenci:
    if i['Id_agenta'] in tab: continue
    print(imiona[i['Id_agenta']])

#6.5
print()

for i in oferta:
    st = i['Status'].strip() == 'A'
    ok = int(i['Pow']) > 180 and st and int(i['L_laz']) >= 2
    if not ok: continue

    ind = i['Id_oferty']
    p = int(i['L_pokoi'])
    l = int(i['L_laz'])
    print(ind, i['Pow'], p, l, i['Cena'], imiona[ag[ind]])


