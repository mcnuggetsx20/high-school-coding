file = open('dane/punkty.txt', 'r').read().split('\n')[:-1]
file = [i.split() for i in file]

N = 10**5
sieve = [True] * (N+1)
sieve[0] = False
sieve[1] = False

#4.1
for i in range(2, N+1):
    for j in range(i, N//i):
        sieve[i*j] = False

ans = 0
for i in file:
    a = int(i[0])
    b = int(i[1])
    ans += sieve[a] and sieve[b]
print(ans)

#4.2
print()

ans = 0
for i in file:
    a = set(i[0])
    b = set(i[1])
    ans += a == b
print(ans)

#4.3
print()

ans = []
for i in file:
    for j in file:
        x1 = int(i[0])
        y1=  int(i[1])
        x2 = int(j[0])
        y2 = int(j[1])
        d = ( (x1 - x2)**2 + (y1- y2)**2 )**0.5
        ans.append( (d, [i, j]) )
ans.sort()
ans = ans[-1]
print(ans[1], int(ans[0]))

#4.4
print()

boki = 0
wewn = 0
zewn = 0

for i in file:
    x=  int(i[0])
    y = int(i[1])

    b = (x == 5000 and y<=5000) or (x <= 5000 and y == 5000)
    w = x < 5000 and y < 5000
    z = x > 5000 or y > 5000

    boki += b
    wewn += w
    zewn += z
print(wewn, boki, zewn)


