from collections import defaultdict as dd
from datetime import datetime, timedelta
def a(name):
    file = open(f'dane/{name}.txt', 'r').read().split('\n')[:-1]
    file = [dict(zip(file[0].split('\t'), i.split('\t'))) for i in file[1:]]
    globals()[name] = file

def join(t1, t2, key):
    t2 = dd(lambda: {'missing': None}) | {i[key]: i for i in t2}
    return [i | t2[i[key]] for i in t1]

a('klienci')
a('pokoje')
a('noclegi')

#5.1
ans = dd(lambda: 0)
for i in join(noclegi, klienci, 'nr_dowodu'):
    start = datetime.strptime(i['data_przyjazdu'], '%Y-%m-%d')
    end = datetime.strptime(i['data_wyjazdu'], '%Y-%m-%d')
    ans[f"{i['imie']} {i['nazwisko']}"] += (end-start).days
ans = sorted(ans.items(), key=lambda x:x[1]); print(ans[-1])

#5.2
ans = dd(lambda: 0)
temp = join(noclegi, klienci, 'nr_dowodu')
temp = join(temp, pokoje, 'nr_pokoju')
for i in temp:
    start = datetime.strptime(i['data_przyjazdu'], '%Y-%m-%d')
    end = datetime.strptime(i['data_wyjazdu'], '%Y-%m-%d')
    c = (end-start).days * int(i['cena'])

    ans[f"{i['imie']} {i['nazwisko']}"] += c

for i in ans:
    if ans[i] <= 2000: continue
    print(i)

#5.3
temp = join(noclegi, klienci, 'nr_dowodu')
temp = join(temp, pokoje, 'nr_pokoju')
trash = []
for i in temp:
    if i['standard'] != 'N': continue
    if i['miejscowosc'].strip() in ['Opole', 'Katowice']: trash.append(i['nr_pokoju'])
for i in pokoje:
    if i['nr_pokoju'] not in trash and i['standard'] == 'N': print(i['nr_pokoju'])



