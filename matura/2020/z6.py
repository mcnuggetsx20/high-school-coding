file = open('dane/statek.txt', 'r').read().split('\n')[:-1]
file = [ dict(zip(file[0].split('\t'), i.split('\t'))) for i in file]
file = file[1:]

#podpunkt 1
from collections import defaultdict as dd
mp = dd(lambda:[0,0])

for i in file:
    if i['Z/W'] == 'W': continue
    tow = i['towar']
    mp[tow][0] += 1
    mp[tow][1] += int(i['ile ton'])
ans = sorted(mp.items(), key = lambda j:j[1][0])[::-1]
print(ans[0][0], ans[0][1][1])


#podpunkt 2
from datetime import datetime

prev = datetime.strptime(file[0]['data'], "%Y-%m-%d")
ans = 0

for i in file[1:]:
    curr = datetime.strptime(i['data'], "%Y-%m-%d")
    ans +=  abs(curr-prev).days > 21
    prev = curr

print(ans)


#podpunkt 3
mp = dd(lambda:0)
daty = ['2016-02-19', '2018-08-05']

for i in file:
    if i['data'] in daty:
        ans = sorted(mp.items(), key = lambda j:j[1])
        print(*ans[0], *ans[-1])
        daty.remove(i['data'])

    tow = i['towar']
    I = i['Z/W']
    mp[tow] += int(i['ile ton']) * ( (I=='Z') - (I=='W') )


#podpunkt 4
mp = dd(lambda: {'Z':0, 'W':0})

for i in file:
    if i['towar'] != 'T5': continue
    key = '-'.join(i['data'].split('-')[:2])
    #month = i['data'].split('-')[1]
    zal = int(i['ile ton']) * (i['Z/W'] == 'Z')
    wyl = int(i['ile ton']) * (i['Z/W'] == 'W')
    mp[key]['Z'] += zal
    mp[key]['W'] += wyl
for i in mp:
    print(i, mp[i])


#podpunkt 5
k = 5 * 10**5
ans = [k, '']
mn = 10**9
for p, i in enumerate(file):
    c = int(i['cena za tone w talarach']) * int(i['ile ton'])
    I = i['Z/W']
    k += c * ( (I=='W') - (I=='Z') )
    mn = min(mn, k)
    try:
        if i['data'] != file[p+1]['data']:
            ans = max(ans, [k, i['data']])
    except:
        continue
ans = max(ans, [k, file[-1]['data']])
print('talarow na koniec:', k)
print('maksymalnie:', *ans)

print(5*10**5 - mn)



