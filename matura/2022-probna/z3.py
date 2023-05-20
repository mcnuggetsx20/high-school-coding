file = open('dane/liczby.txt', 'r').read().split()
test = open('dane/liczby_przyklad.txt', 'r').read().split()
file = list(map(int, file))

from math import sqrt
N = int(1e6)
sieve = [True] * (N+1)
sieve[0] = False
sieve[1] = False
for i in range(2, int(sqrt(N))+1):
    for j in range(2, (N//i)+1):
        sieve[i*j] = False
#3.1
ans = 0
for i in file:
    ans += sieve[i-1]
print(ans)

#3.2
f = []
for i, v in enumerate(sieve):
    if v: f.append(i)

from collections import defaultdict as dd
mp = dd(lambda: 0)
for i in set(file):
    for j in f:
        if j <= i//2:
            if sieve[i-j]: 
                mp[i] += 1
        else: break
mp = sorted(mp.items(), key=lambda x:x[1])
print(mp[-1])
print(mp[0])

#3.3
print()
d = [str(i) for i in range(10)] + [chr(i) for i in range(65, 71)]
mp = dd(lambda: 0 )
for i in file:
    temp = hex(i)[2:].upper()
    for j in temp: mp[j] += 1
for i in d: print(i, mp[i])


