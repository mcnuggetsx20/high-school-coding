file = open('dane/transport.txt', 'r').read().split('\n')[:-1]
file = [dict(zip(file[0].split('\t'), i.split('\t'))) for i in file[1:]]

#5.1
target ='ERA 092 TR'

for i in file:
    rej = i['Nr_rejestracyjny']
    if rej != target: continue

    rok = int(i['Rok_produkcji'])
    cena = int(i['Cena_zakupu'])
    prz = int(i['Przebieg'])

    amoc = (2017 - rok)* 0.05*cena
    amop = (prz//100000) * 0.02*cena
    print(amoc, amop, cena-amop-amoc)

from collections import defaultdict as dd
ans = dd(lambda: 0)
for i in file:
    rok = int(i['Rok_produkcji'])
    cena = int(i['Cena_zakupu'])
    prz = int(i['Przebieg'])

    amoc = (2017 - rok)* 0.05*cena
    amop = (prz//100000) * 0.02*cena
    war = cena - amoc- amop

    rej = i['Nr_rejestracyjny']
    ans[rej] = max(ans[rej], war)
ans = sorted(ans.items(), key = lambda x:x[1])[0]

for i in file:
    rej = i['Nr_rejestracyjny']
    if rej == ans[0]:
        print(i['Marka_i_model'], rej, ans[1])

#5.2
print()
ans = dd(lambda: [0, 0])
for i in file:
    marka = i['Marka_i_model'].split()[0]
    ans[marka][0] += 1
    ans[marka][1] += int(i['Przebieg'])

for i in ans:
    print(i, ans[i][0], int(ans[i][1]/ans[i][0]))

#5.3
print()
ans = dd(lambda: dd(lambda: 0))

for i in file:
    marka = i['Marka_i_model'].split()[0]
    rok = int(i['Rok_produkcji'])
    ans[marka][rok] += 1
for i in ans:
    print(i)
    for j in ans[i]:
        print(j, ans[i][j])
    print()

#5.4

ans = dd(lambda:0)
from datetime import datetime
base = datetime.strptime('2017-01-01', '%Y-%m-%d')

info = {i['Nr_rejestracyjny']: i['Marka_i_model'] for i in file}

for i in file:
    rej = i['Nr_rejestracyjny']
    data = datetime.strptime(i['Data_ostatniego_remontu'], '%Y-%m-%d')
    ans[rej] = abs(data-base).days
ans = sorted(ans.items(), key = lambda x:x[1])[-4:]
for i in ans:
    print(info[i[0]], i[0], i[1])





