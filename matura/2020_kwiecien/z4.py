file = open('dane/dane4.txt', 'r').read().split()
file = list(map(int, file))

#4.1
ans = set()
for i, v in enumerate(file[:-1]):
    luka = abs(v - file[i+1])
    ans.add(luka)
print(min(ans), max(ans))

#4.2
from collections import defaultdict as dd
ans = []
base = abs(file[0]-file[1])
temp = [file[0], file[1]]

for i in range(1, len(file)-1):
    luka = abs(file[i] - file[i+1])

    if luka == base:
        temp.append(file[i+1])

    else:
        ans.append((len(temp), temp))
        temp = [file[i], file[i+1]]
        base = abs(file[i] - file[i+1])
ans.sort()
print(ans[-1][0], ans[-1][1][0], ans[-1][1][-1])

#4.3
ans = dd(lambda: 0)
for i, v in enumerate(file[:-1]):
    luka = abs(v - file[i+1])
    ans[luka] += 1
sec = dd(lambda:[])
for i in ans:
    sec[ans[i]].append(i)
sec = sorted(sec.items(), key=lambda x:x[0])[-1]
print(*sec)






