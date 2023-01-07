from datetime import datetime

file = open('dane/temperatury.txt' ,'r').read().split('\n')[:-1]
file= [i.split(';') for i in file]

#5.1
ans = []
temp = []

for i in file:
    tmp = int(i[1])
    ok = tmp > 20
    
    if ok:
        temp.append(i[0])
    else:
        ans.append( (temp, len(temp)))
        temp = []
ans.append( (temp, len(temp)))

ans = sorted(ans, key=lambda x:x[1])[-1][0]
print(ans[0], ans[-1])
print()

#5.2

def f(t):
    h = 90 * ( 1 + (1/13) * ((t-24)/2) )
    l = 120 * ( 1 + (2/29) * ((t-24)/2) )
    k = 80 * ( 1 + (1/17) * ((t-24)/2) )

    h = int(h)
    l = int(l)
    k = int(k)

    return [h, l, k]

from collections import defaultdict as dd
ans = {6: [90, 120, 80],
       7: [0,0,0],
       8: [0,0,0]}

for i in file[1:]:
    tmp = int(i[1])
    d= datetime.strptime(i[0], '%Y-%m-%d').month

    vals =f(tmp)
    ans[d] = [i + j for i,j in zip(ans[d], vals)]

print(ans)
print()

#5.3
temp = 90 *7 + 120 *5 + 80 * 6
ans = dd(lambda:0)
ans[file[0][0]] = temp

for i,v in enumerate(file[1:]):
    tmp = int(v[1])
    vals= f(tmp)
    d= v[0]
    ans[d] = vals[0] * 7 + vals[1] * 5 + vals[2] * 6
    ans[d] += ans[file[i][0]]
    if ans[d] > 45000:
        print(d, ans[d])
        break

#5.4

def f1(t):
    global o
    h = (90+o) * ( 1 + (1/13) * ((t-24)/2) )
    l = (120+o) * ( 1 + (2/29) * ((t-24)/2) )
    k = (80+o)* ( 1 + (1/17) * ((t-24)/2) )

    h = int(h)
    l = int(l)
    k = int(k)

    return [h, l, k]


mn = 10**9
ok = False
o = 1.33
for i in range(30):
    tmp = 23 - (i//2)
    vals = f1(tmp)
    utarg = vals[0]*(7+o) + vals[1]*(5+o) + vals[2]*(6+o)
    if utarg < 1000 and not ok:
        print(i+1)
        ok = True
    mn = min(utarg, mn)
print(mn)











