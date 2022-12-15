#63.3
file = open('dane/63/ciagi.txt', 'r').read().split('\n')

sieve = [0 for i in range(1, 2**20 + 2)]
sieve[0] = 1

for i in range(2, 2**20+1):
    for j in range(i, (2**20+1)// i):
        sieve[i*j] = 1

def solve(n):
    n = int(n, 2)
    for i in range(2, len(sieve)):
        if i >= n:
            return False
        if sieve[i] or n%i: continue

        if not sieve[int(n/i)]:
            return True

mx = 0
mn = 2**20
c= 0
for i in file:
    temp = solve(i)
    c += temp
    mx = max(int(i,2) * temp, mx)
    mn = min(int(i,2) + 2**20 * (not temp), mn)
print('Liczb polpierwszych jest:', c, '\nMax:', mx, '\nMin:', mn)


