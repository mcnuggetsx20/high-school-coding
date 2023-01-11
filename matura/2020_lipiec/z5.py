file = open('dane/myjnia.txt', 'r').read().split('\n')[:-1]
file = [i.split(';') for i in file]

#5.1
from collections import defaultdict as dd
ans = dd(lambda:0)

for i in file:
    pr = int(i[1])

    ans[pr] += 1
for i in sorted(ans.items(), key=lambda x:x[0]):
    print(*i)

#5.2
print()
ans = dd(lambda:set())

for i in file:
    miasto = i[2][:2]

    ans[miasto].add(i[2])

J = 0
D = 0
for i in ans:
    J += len(ans[i]) == 1
    D += len(ans[i]) == 2

print(J,D)

#5.3
print()
czas = 6*60
limit=  20*60
ans = 0
for i in file:
    czas += int(i[0])
    ans += czas < limit
    if czas >= limit:
        print(last//60,end=':')
        last%=60
        print(last)
        break
    last = czas
print(ans)

#5.4
print()
ans = dd(lambda: set())

czas = 0
for i in file:
    czas += int(i[0])
    godz = czas//60 + 1
    ans[godz].add(i[2])
ans = {i:len(ans[i]) for i in ans}
ans = sorted(ans.items(), key=lambda x:x[0])[:6]
for i in ans:
    print(*i)

#5.5
print()

czas = int(file[0][0])
nast = czas + int(file[0][1])
ans = []
rez = 0
mx =  0
temp = 0

for i,v in enumerate(file[1:]):
    i += 1
    czas += int(v[0])
    
    ocz = max(0, nast - czas)
    file[i][0] = czas
    if ocz > 5:
        temp += 1
        ans.append(v[2])
        rez += 1
        file[i] = file[i-1]
        continue

    nast += czas + ocz + int(v[1])
    mx = max(mx, temp)
    temp = 0
mx = max(mx,temp)

print(ans[1])
print(rez)  
print(mx)



