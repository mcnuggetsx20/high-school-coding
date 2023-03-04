def f(name):
    tab = open(f'dane/{name}.txt', 'r').read().split('\n')[:-1]
    tab = [dict(zip(tab[0].split(';'), i.split(';'))) for i in tab[1:]]
    globals()[name] = tab

def join(a, b, k):
    b = {i[k]: i for i in b}
    return [ i | b[i[k]] for i in a]

f('ewidencja')
f('uczen')
f('klasa')

#6.1
temp = join(ewidencja, uczen, 'IdUcznia')
ans = 0

for i in join(temp, klasa, 'IdKlasy'):
    ok = i['Imie'][-1] == 'a' and i['ProfilKlasy'] == 'biologiczno-chemiczny'
    ans += ok
print(ans)

#6.2
print()
from collections import defaultdict as dd
ans = dd(lambda: 0)
for i in ewidencja:
    d = i['Wejscie'].split(' ')
    day = d[0]
    godz = d[1].split(':')
    ok = int(godz[0][1]) < 8 or godz == ['08', '00', '00']
    ans[day] += ok
ans = sorted(ans.items(), key= lambda x:x[0])
for i in ans: print(*i)

#6.3
print()
ans = dd(lambda: [0,0])
from datetime import datetime
for i in temp:
    wej = i['Wejscie']
    wyj = i['Wyjscie']
    wej = datetime.strptime(wej, '%Y-%m-%d %H:%M:%S')
    wyj = datetime.strptime(wyj, '%Y-%m-%d %H:%M:%S')

    ind = i['IdUcznia']
    name = i['Imie'] + ' ' + i['Nazwisko']
    ans[ind][0] += abs(wej-wyj).seconds
    ans[ind][1] = name

ans = sorted(ans.items(), key= lambda x:x[1])[::-1][:3]
for i in ans: print(i[1][1])

#6.4
print()
ans = []
for i in temp:
    d = i['Wejscie'].split(' ')
    day = d[0].split('-')[-1]
    if day != '06': continue
    ans.append( [i['IdUcznia'], i['Imie'] + ' ' + i['Nazwisko']] )

for i in uczen:
    a = [i['IdUcznia'], i['Imie'] + ' ' + i['Nazwisko']] 
    if a not in ans: print(a[-1])







