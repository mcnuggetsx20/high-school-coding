file = open('dane/binarne.txt', 'r').read().split()

#4.1
ans = 0
mx = [0,0]

for i in file:
    ok = i[:len(i)//2] == i[len(i)//2:]
    if not ok: continue
    ans += 1
    if mx[0] < len(i):
        mx = [len(i), i]


print(ans, mx[::-1])

#4.2
ans = 0
mn = 10**9
for i in file:
    temp = [i[j:j+4] for j in range(0, len(i), 4)]
    for j in temp:
        a = int(j, 2)
        if a > 9:
            ans += 1
            mn = min(mn, len(i))
            break
print(ans, mn)

#4.3
ans = [0,0]

for i in file:
    j = int(i, 2)
    if j > 65535: continue
    if j > ans[0]:
        ans = [j, i]
print(*ans[::-1])





