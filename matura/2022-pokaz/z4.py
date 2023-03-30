file = open('dane/brenna.txt' ,'r').read().split('\n')[:-1]
file = [dict(zip(file[0].split('\t'), i.split('\t'))) for i in file[1:]]
from datetime import datetime, timedelta
from collections import defaultdict as dd
from statistics import mean

#4.1
ans = dd(lambda: [-10**9, 10**9])
for i in file:
    data = i['data'].split()[0]
    T = float(i['temperatura'].replace(',', '.'))
    ans[data][0] = max(ans[data][0], T)
    ans[data][1] = min(ans[data][1], T)
for i in ans: ans[i] = abs(ans[i][0] - ans[i][1])
ans = sorted(ans.items(), key=lambda x:x[1])[-1]
print(ans)

#4.2
ans = dd(lambda: [])
for i in file:
    data = i['data'].split()[1]
    T = float(i['temperatura'].replace(',', '.'))
    ans[data].append(T)
for i in ans: print(i, round(mean(ans[i]), 2))

#4.3
print()
ans= []
temp = []
for i in file:
    T = float(i['temperatura'].replace(',', '.'))
    O = float(i['opad'].replace(',','.'))
    ok = T * O > 0
    if ok: temp.append(i)
    else: 
        if len(ans) < len(temp): ans = temp.copy()
        temp = []
s = 0
for i in ans:
    O = float(i['opad'].replace(',','.'))
    s += O
print(ans[0]['data'], ans[-1]['data'], s)

#4.4
wys = 0
plug = False
ansa = 0
ansb = dd(lambda: 0)
for i in file:
    data = i['data'].split()[0]
    T = float(i['temperatura'].replace(',', '.'))
    O = float(i['opad'].replace(',','.'))
    snieg = T<=0 and O > 0
    rain = T > 0 and O > 0

    if plug: 
        plug = False
        wys = 0
        if not rain: ansa += 1; ansb[data]+=1; continue 

    if snieg: wys += O
    elif rain: wys = 0

    if wys > 4: plug = True
print(ansa)
ansb = sorted(ansb.items(), key = lambda x:x[1])[-1]
print(*ansb)

