def a(name):
    file = open(f'dane/{name}.txt').read().split('\n')[:-1]
    file = [dict(zip(file[0].split(';'), i.split(';'))) for i in file[1:]]
    globals()[name] = file

from collections import defaultdict as dd
from datetime import datetime, timedelta

def join(t1, t2, k):
    t2 = dd(lambda: {'missing', ''}) | {i[k]: i for i in t2}
    return [i | t2[i[k]] for i in t1]

a('ceny_za_dobe')
a('samochody')
a('klienci')
a('wypozyczenia')

print('6.1') #6.1
cennik = {i['Klasa']: int(i['Cena']) for i in ceny_za_dobe}
temp = join(wypozyczenia, samochody, 'Nr_ew')
temp = join(temp, klienci, 'Nr_klienta')

ans = []
for i in temp:
    start= datetime.strptime(i['Wypozyczenie'], '%Y-%m-%d')
    end= datetime.strptime(i['Zwrot'], '%Y-%m-%d')
    diff = abs(start-end).days
    klasa= i['Nr_firmowy'][0]
    ans.append([i['Nazwisko'], i['Imie'], i['Nr_rej'], diff, diff* cennik[klasa] ])
ans.sort()
print(ans[0])
print(ans[-1])

print('\n6.2') #6.2
temp = join(wypozyczenia, samochody, 'Nr_ew')
ans = dd(lambda:0)
for i in temp:
    klasa= i['Nr_firmowy'][0]
    ans[klasa] += 1
ans = sorted(ans.items(), key=lambda x:x[0])
for i in ans: print(*i)

print('\n6.3') #6.3
temp = join(wypozyczenia, klienci, 'Nr_klienta')
ans = dd(lambda: 0)
for i in temp:
    imie = i['Imie'] + ' ' + i['Nazwisko']
    ans[imie] += 1
mx = max(ans, key=ans.get)
for i in ans:
    if ans[i] == ans[mx]: print(i, ans[i])

print('\n6.4') #6.4
temp = join(wypozyczenia, samochody, 'Nr_ew')
trash = []
for i in temp: trash.append(i['Nr_ew'])
ans = dd(lambda:dd(lambda:0))
for i in samochody:
    klasa= i['Nr_firmowy'][0]
    miej = i['Miejscowosc']
    if i['Nr_ew'] in trash: continue
    ans[klasa][miej] += 1

print('\tAniolkowo	Manipulatowo	Nieszczerzyn	Piarowa\t\tWielka Wola')
for i in ans:
    temp = sorted(ans[i].items(), key=lambda x:x[0])
    print(i, end='\t\t\t')
    for i in temp: print(i[1], end='\t\t\t')
    print()

print('\n6.5') #6.5
temp = join(wypozyczenia, klienci, 'Nr_klienta')
trash = set()
for i in temp: trash.add(i['Nr_klienta'])
print(len(klienci) - len(trash))





