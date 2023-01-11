file = open('dane/galerie.txt','r').read().split('\n')[:-1]

keys = ['kod', 'miasto', 'wym']
for i, v in enumerate(file):
    v = v.split()
    sl= list(map(int, v[2:]))
    temp = []

    for j in range(0, len(sl)-1, 2):
        temp.append( (sl[j], sl[j+1]) )

    file[i] = dict(zip(keys, [v[0], v[1], temp]))

#4.1
from collections import defaultdict as dd
ans = dd(lambda: 0)

for i in file:
    ind = i['kod']
    ans[ind] += 1

for i in ans:
    print(i, ans[i])

#4.2
print()
ans = dd(lambda: [0,0])

for i in file:
    ind= i['miasto']

    for j in i['wym']:
        ans[ind][0] += j[0] * j[1]
        ans[ind][1] += 1 * bool(j[0] * j[1])

for i in ans:
    print(i, ans[i])

ans = sorted(ans.items(),key=lambda x:x[1][0])
print(ans[-1], ans[0])

#4.3
print()
ans = dd(lambda: set())
for i in file:
    ind= i['miasto']

    for j in i['wym']:
        if j[0] * j[1]:
            ans[ind].add( j[0] * j[1])

ans = { i: len(ans[i]) for i in ans}
ans = sorted(ans.items(), key =lambda x:x[1])
print(ans[-1], ans[0])



