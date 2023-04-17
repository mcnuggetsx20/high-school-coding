file = open('dane/statek.txt').read().split('\n')[:-1]
file = [dict(zip(file[0].split('\t'), i.split('\t'))) for i in file[1:]]

from collections import defaultdict as dd

#6.1
ans1 = dd(lambda:0)
ans2 = dd(lambda:0)

for i in file:
    if i['Z/W'] != 'Z': continue
    ile = int(i['ile ton'])
    ans1[i['towar']] += 1
    ans2[i['towar']] += ile
mx = max(ans1, key=ans1.get)
print('6.1\n', mx, ans2[mx])

#6.2
from datetime import datetime, timedelta
prev = file[0]['data']
prev = datetime.strptime(prev, '%Y-%m-%d')

ans = 0
for i in file[1:]:
    curr = datetime.strptime(i['data'], '%Y-%m-%d')
    ans += abs(prev-curr).days > 21
    prev = curr
print('\n6.2\n', ans)

#6.3
print('\n6.3')
ans = dd(lambda:0)
daty = ['2016-02-19', '2018-08-05']
for i in file:
    if i['data'] in daty:
        mx = max(ans, key=ans.get)
        mn = min(ans, key=ans.get)
        print(mx, ans[mx],mn ,ans[mn])
        daty.pop(0)

    status = i['Z/W'] =='Z'
    ile = int(i['ile ton'])
    ind = i['towar']

    ans[ind] += ile * status
    ans[ind] -= ile * (not status)

#6.4
print('\n6.4')
zal = dd(lambda:0)
wyl = dd(lambda:0)
for i in file:
    if i['towar'] != 'T5': continue
    m = i['data'][:-3]
    status = i['Z/W'] =='Z'
    zal[m] += int(i['ile ton']) * status
    wyl[m] += int(i['ile ton']) * (not status)

miss = ['2016-05', '2016-10', '2016-12', '2017-09', '2017-12', '2018-05']
for i in miss: zal[i], wyl[i] = 0,0

zal = sorted(zal.items(),key=lambda x:x[0])
for i in zal: print(i[0], '\t', i[1], '\t', wyl[i[0]])

#6.5
print('\n6.4')
def solve(tal):

    #tal = 5 * 10**5
    ansa2 = 0
    mxdzien = 0
    prev = 0
    mn = 0

    for i in file:
        curr = i['data']
        if curr != prev:
            if ansa2 < tal: ansa2 = tal; mxdzien = prev
            mn = min(mn, tal)
        prev = curr

        status = i['Z/W'] =='Z'
        ile = int(i['ile ton'])
        cena = int(i['cena za tone w talarach'])
        kwota = ile*cena
        tal += kwota * (not status); tal -= kwota * status

    ansa1 = tal
    return ansa1, ansa2, mxdzien, mn 
print(solve(5*10**5)[:-1])
print(solve(0)[-1] * -1)







    


