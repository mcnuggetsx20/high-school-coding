file = open('dane/liczby.txt', 'r').read().split()

#4.1
for i in file:
    j = i[::-1]
    j = int(j)
    print( (str(j)+'\n') * (not j%17),end = '')

print()

#4.2
from collections import defaultdict as dd
mp = dd(lambda:0)

for i in file:
    j = int(i[::-1])
    i = int(i)
    N = abs(j - i)
    mp[i] = N

mp = sorted(mp.items(), key=lambda x: x[1])
print(mp[-1])
print()

#4.3
sieve = [True] * 10001
sieve[0] = 0
sieve[1] = 0

for i in range(2, 10001):
    for j in range(i, 10001//i):
        sieve[i*j] = False

for i in file:
    j = int(i[::-1])
    i = int(i)
    print( (str(i) + '\n') * (sieve[i] and sieve[j]), end='')
print()

#4.4
print(len(set(file)))

mp = dd(lambda:0)

for i in file:
    mp[i] += 1
mp = [i[1] for i in mp.items()]
print(mp.count(2))
print(mp.count(3))


