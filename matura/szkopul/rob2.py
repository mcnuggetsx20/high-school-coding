n, m = map(int, input().split())
N = n

tab = []
from collections import defaultdict

while N:
    tab.append( list(map(int, input().split())) )
    N-=1

mp = defaultdict(lambda: tab[0][0])

for j in range(m):
    a = input()
    x = 0
    y = 0
    for i in a:
        x += i=='E'
        x -= i=='W'

        y -= i=='N'
        y += i=='S'

        if x > n-1 or x < 0 or y > n-1 or y < 0:
            mp[j] = -1
            break

        mp[j] += tab[y][x]

for i in sorted(mp.items(), key = lambda x: x[1], reverse=True):
    print(i[0] + 1, i[1])
    break
