file = open('dane/dane.txt' ,'r').read().split('\n')[:-1]

ans = 0
for i in file:
    ans += i[0] == i[-1]
print(ans)

#6b
ans = 0
for i in file:
    j = str(int(i,8))
    ans += j[0] == j[-1]
print(ans)

#6c
mx = (0, 0)
mn = (10**20, 0)
for i in file:
    j = int(i,8)
    ok = True
    for k in range(1, len(i)):
        if int(i[k]) < int(i[k-1]): ok = False; break
    if ok:
        if mx[0] < j: mx = (j, i)
        if mn[0] > j: mn = (j, i)
print(mn[-1], mx[1])

