file = open('dane/identyfikator.txt', 'r').read().split()

#4.1
from collections import defaultdict as dd
ans = dd(lambda:0)
mx = 0
for i in file:
    a = i[3:]
    a = list(map(int, list(a)))
    ans[i] = sum(a)
    mx = max(mx, sum(a))

for i in ans:
    if ans[i] == mx:
        print(i)

#4.2
print()

ans = []
for i in file:
    a = i[3:]
    seria = i[:3]
    ok = (a==a[::-1]) or (seria==seria[::-1])
    if ok: ans.append(i)
print('\n'.join(ans))

#4.3
print()
w = [7,3,1,7,3,1,7,3]
for i in file:
    seria = list(i[:3])
    num = list(map(int, list(i[4:])))

    kont = int(i[3])
    seria = [ord(i)-55 for i in seria]

    temp = 0
    for j,v in enumerate(seria + num):
        temp += v * w[j]

    if temp%10 != kont: print(i)







