file = open('dane/ekodom.txt', 'r').read().split('\n')[:-1]
file = [dict(zip(file[0].split('\t'), i.split('\t'))) for i in file[1:]]

from collections import defaultdict as dd
from datetime import datetime
mp = dd(lambda:0)
woda = 5000
start = False
c=  0
temp1a = []
ans1a = []
ans1b = 0
ans3a = 0
ans3b = 0

for i in file:
    data = datetime.strptime(i['Data'], '%d.%m.%Y')
    i['retencja'] = int(i['retencja'])

    woda += i['retencja']
    woda -= 190
    if data.weekday() == 2: woda -= (260-190)

    if i['Data'] == '01.04.2022': start = True
    if start:
        c+= not i['retencja']
        c *= not i['retencja']
        if c and not (c%5): woda -= 300; ans1b +=1
    if i['Data'] == '01.10.2022': start = False

    if not i['retencja']:
        temp1a.append(i['Data'])
    else:
        if len(temp1a) > len(ans1a): ans1a = temp1a.copy()
        temp1a = []

    m = data.month
    mp[m] += i['retencja']

    if woda < 0: ans3a += 1; ans3b += abs(woda); woda = 0



if len(temp1a) > len(ans1a): ans1a = temp1a.copy()
temp1a = []

print(len(ans1a), ans1a[0],',',  ans1a[-1])
print(ans1b)
print()

for i in sorted(mp.keys()): print(i, mp[i])

print()
print(ans3a, ans3b)




