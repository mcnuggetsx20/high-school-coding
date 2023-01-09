N = 10 ** 6
sieve = [True] * (N+1)

sieve[0] = False
sieve[1] = False

for i in range(2, int(N**0.5) + 1):
    if sieve[i] == True:
        j = 2*i
        while j<=N:
            sieve[j] = False
            j += i

tab = [i for i in range(len(sieve)) if sieve[i] ]


file = open('dane/liczby.txt', 'r').read().split()
file = [ int(i) for i in file]

#3.3
from collections import defaultdict as dd
mp = dd(lambda: 0)

ans = 0
for i in file:
    for j in tab:
        diff = i -j
        if diff <=0 or j > i//2: break
        mp[i] += sieve[diff]

mp =  sorted(mp.items(), key=lambda x:x[1])[::-1]
print(*mp[0])
print(*mp[-1])

#3.4
print()

ans=  dd(lambda:0)
for i in file:
    a = hex(i)[2:]
    for j in a:
        ans[j] +=1

for i in range(10):
    j = str(i)
    print(j, ans[j])

for i in range(6):
    print(chr(65 + i), ans[ chr(97+i) ])
