def f(name):
    a = open(f'dane/{name}.txt' ,'r').read().split('\n')[:-1]
    a = [dict(zip(a[0].split('\t'), i.split('\t'))) for i in a[1:]]
    globals()[name] = a

from collections import defaultdict as dd
def join(t1, t2, k):
    t2 = dd(lambda: {'missing': ''}) | {i[k]: i for i in t2}
    return [i | t2[i[k]] for i in t1]

f('wizytydane')
f('wizytyzabiegi')
f('klienci')
f('zabiegi')

#6.1
temp = join(wizytydane, wizytyzabiegi, 'id_wizyty')
temp = join(temp, klienci, 'id_klienta')
temp = join(temp, zabiegi, 'kod_zabiegu')

ans = 0
for i in temp:
    name = i['imie'] + ' ' + i['nazwisko']
    if name != 'Alicja Kowalska': continue
    ans += int(i['cena (zl)'])
print(ans)

#6.2
ans = dd(lambda: 0)

for i in temp:
    name = i['imie'] + ' ' + i['nazwisko']
    ans[name] += 1
ans = sorted(ans.items(), key=lambda x: x[1])[-1]
print(*ans)

#6.3
temp = join(wizytyzabiegi, zabiegi, 'kod_zabiegu')
temp = join(temp, wizytydane, 'id_wizyty')
ans = list()
for i in temp:
    zab = i['zabieg']
    if zab != 'Magia Hawajow': continue

    ans.append(i['data'])
ans.sort()
print(len(ans), ans[::-1])

#6.4
from datetime import datetime, timedelta
start = datetime.strptime('6.12.2017', '%d.%m.%Y')
end = datetime.strptime('15.01.2018', '%d.%m.%Y')

ans = set()
ans2 = 0
temp = join(wizytyzabiegi, wizytydane, 'id_wizyty')
temp = join(temp, zabiegi, 'kod_zabiegu')
for i in temp:
    data = datetime.strptime(i['data'], '%Y-%m-%d')
    ok = (data - start).days >= 0 and (data-end).days <= 0
    if not ok: continue

    if i['dzial'] == 'MAKIJAZ': 
        ans.add(i['id_klienta'])
        cena =int(i['cena (zl)'])
        ans2 += 0.8*cena

print(len(ans), ans2)

#6.5
temp = join(zabiegi, wizytyzabiegi, 'kod_zabiegu')
for i in temp:
    if 'missing' in i and i['dzial'] == 'FRYZJER MESKI': print(i['zabieg'])





