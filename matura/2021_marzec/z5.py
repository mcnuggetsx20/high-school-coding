file = open('dane/telefony.txt' ,'r').read().split('\n')[:-1]
file = [dict(zip(file[0].split(), i.split())) for i in file[1:]]

#5.1
from collections import defaultdict as dd
ans = dd (lambda:0)

for i in file:
    ans[i['nr']] += 1

ans = sorted(ans.items(), key=lambda x:x[1])
print(ans[-1:-4:-1])

#5.2
print()

ans = dd (lambda:[0,0])
for i in file:
    n = len(i['nr'])
    if n == 10:continue

    d = i['data']
    ok = n==7

    ans[d][ok] += 1

for i in ans:
    print(i, ans[i])

#5.3
from datetime import datetime
print()
ans = [0,0]
for i in file:
    ok = i['nr'][:2] == '12' and len(i['nr']) == 7
    if not ok : continue
    ans[0] += 1

    r= datetime.strptime(i['rozpoczecie'], '%H:%M:%S')
    z= datetime.strptime(i['zakonczenie'], '%H:%M:%S')
    
    ans[1] += abs(z-r).seconds

from math import ceil
ans[1] = ceil(ans[1]/60)
print(ans)

#5.4
print()
zagraniczne = 0
minuty = 0
ab = 0
ok = False
ans= dd(lambda:0)

for i in file:
    r= datetime.strptime(i['rozpoczecie'], '%H:%M:%S')
    z= datetime.strptime(i['zakonczenie'], '%H:%M:%S')
    d = abs(z-r).seconds/60
    n = len(i['nr'])

    if n == 10:
        zagraniczne += ceil(d)
    else:
        minuty += d
        if minuty >= 800 and not ok:
            minuty -= 800
            ok = True
            ab = 50
            ans[n] = minuty

        if ok:
            ans[n] += d
print('abonament', ab)
print('stacjonarne', ceil(ans[7]/100) * 5)
print('komorkowe', ceil(ans[8]/100) * 6)
print('zagraniczne', zagraniczne)
print('suma', ceil(ans[7]/100) * 5 + ceil(ans[8]/100) * 6 + zagraniczne + ab)


    











