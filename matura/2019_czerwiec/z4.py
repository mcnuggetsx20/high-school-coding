def parse(a): return list(map(int, open(f'dane/{a}.txt', 'r').read().split()))
liczby = parse('liczby')
pierwsze = parse('pierwsze')

#4.1
N = 10**7
sieve = [True] * (N+1)
sieve[0] = False
sieve[1] = False
for i in range(2, int(N**0.5)):
    for j in range(i, int(N//i + 1)):
        sieve[i*j] = False

for i in liczby:
    if 100 <= i <= 5000 and sieve[i]: print(i)

#4.2
print()

for i in pierwsze:
    j = int(str(i)[::-1])
    if sieve[j]: print(i)

#4.3
test = [i for i in range(0, 10)]
print()
ans = 0
for i in pierwsze:
    j = sum(list(map(int, list((str(i))))))
    while j not in test:
        j = sum(list(map(int, list((str(j))))))
    ans += j==1
print(ans)


