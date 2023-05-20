def a(name):
    file = open(f'dane/{name}.txt').read().split('\n')[:-1]
    file = [ dict(zip(file[0].split(';'), i.split(';'))) for i in file[1:]]
    globals()[name] = file

from collections import defaultdict as dd
def join(t1, t2, k):
    t2 = dd(lambda: {'missing': None}) | {i[k] : i for i in t2}
    return [i | t2[i[k]] for i in t1]

a('klasa')
a('uczen')
a('ewidencja')

#6.1
temp = join(ewidencja, uczen, 'IdUcznia')
ans = 0
for i in join(temp, klasa, 'IdKlasy'): ans += i['ProfilKlasy'] == 'biologiczno-chemiczny' and i['Imie'][-1] == 'a'
print(ans, '\n')

#6.2
from datetime import datetime, timedelta
mp = dd(lambda: 0)
tab = dd(lambda: 0)
test = datetime.strptime('08:00:00', '%H:%M:%S')
for i in ewidencja:
    godz=  datetime.strptime(i['Wejscie'].split()[1], '%H:%M:%S')
    data =i['Wejscie'].split()[0]
    mp[data] += (test-godz).days < 0
    tab[data] += 1
    #print(data, i['IdUcznia'], (test-godz).days, godz)
for i in mp: print(i, tab[i]-mp[i])
print()

#6.3
ans = dd(lambda: 0)
for i in temp:
    start= datetime.strptime(i['Wejscie'].split()[1], '%H:%M:%S')
    end = datetime.strptime(i['Wyjscie'].split()[1], '%H:%M:%S')
    ans[ f"{ i['IdUcznia'] } { i['Imie'] } { i['Nazwisko'] }" ] += (end-start).seconds
for i in sorted(ans.items(), key=lambda x:x[1])[-3:]: print(i[0])
print()

#6.4
trash = []
for i in ewidencja:
    if i['Wejscie'].split()[0] != '2022-04-06': continue
    trash.append(i['IdUcznia'])
for i in uczen:
    if i['IdUcznia'] not in trash: print(i['Imie'], i['Nazwisko'])
    

















