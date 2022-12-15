file = open('Dane_PR2/kursy.txt', 'r').read().split('\n')[:-1]
file = [i.split(';') for i in file]
for i in range(1, len(file)):
    file[i] = dict(zip(file[0], file[i]))
file =file[1:]

from collections import defaultdict

mp = defaultdict(lambda: 0)

#podpunkt 1
for i in file:
    key = i['Poczatek'] + ' ' + i['Koniec']
    price = int(i['Cena']) / int(i['Odleglosc'])
    mp[key] = max(mp[key], round(price,2))

ans = sorted(mp.items(), key=lambda x:x[1])
print(*ans[-1])

#podpunkt 2
ans = 0
for i in file:
    ans += int(i['Cena']) * (int(i['Odleglosc']) > 400)
print(ans)

#podpunkt 3
mp = defaultdict(lambda: 0)

for i in file:
    key = i['Poczatek'] + ' ' + i['Koniec']
    item = int(i['Waga'])
    mp[key] += item
ans = sorted(mp.items(), key =lambda j:j[1])[::-1]
print(*ans[0])
print()


#popdunkt 4
mp = defaultdict(lambda: 0)

for i in file:
    key = i['Koniec']
    mp[key] += 1
ans = sorted(mp.items(), key = lambda j: j[1])[::-1]
for i in ans:
    if i[1] >=8:
        print(*i)
print()


#podpunkt 5
from datetime import timedelta, datetime

prev = [file[1]['Data'], file[1]['Poczatek'], file[1]['Koniec']]
ind = 0
tab = []
temp = []
for i in file[1:]:
    curr = [i['Data'], i['Poczatek'], i['Koniec']]

    date1 = datetime.strptime(curr[0], "%d-%m-%Y")
    date2 = datetime.strptime(prev[0], "%d-%m-%Y")

    c1 = abs(date1-date2).days != 1
    c2 = curr[1] != prev[2]

    if c1 or c2:
        prev = curr.copy()
        ind += 1
        tab.append((temp, len(temp)))
        temp = []
        temp.append(i)
        continue
    temp.append(i)

    prev = curr.copy()

tab = sorted(tab, key = lambda j:j[1])[::-1]
ans = tab[0][0]
print(ans[0]['Data'], ans[-1]['Data'])
