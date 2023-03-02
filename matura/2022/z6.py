def parse(name):
    temp = open(f'dane/{name}.txt', 'r').read().split('\n')[:-1]
    temp= [ dict(zip(temp[0].split(';'), i.split(';'))) for i in temp[1:]]
    globals()[name]  = temp
parse('ewidencja')
parse('klasa')
parse('uczen')

#6.1
h = {i['IdUcznia']:i for i in uczen}
pr ={i['IdKlasy']: i['ProfilKlasy'] for i in klasa}
ans = 0
for i in ewidencja:
    ind = h[i['IdUcznia']]
    klasa = ind['IdKlasy']
    prof = pr[klasa] == 'biologiczno-chemiczny'
    imie = ind['Imie'][-1]=='a'

    ans += prof and imie
print(ans)

#6.2
print()

from datetime import datetime
from collections import defaultdict as dd
ans = dd(lambda:set())
obe = dd(lambda:set())
for i in ewidencja:
    d = datetime.strptime(i['Wejscie'], '%Y-%m-%d %H:%M:%S')
    h = d.hour < 8 or (d.hour == 8 and d.minute==0)
    day = d.day
    if h: ans[day].add(i['IdUcznia'])

for i in ans: 
    print(len(ans[i]))






