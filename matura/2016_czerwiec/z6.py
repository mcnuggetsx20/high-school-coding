file = open('dane/liczby.txt', 'r').read().split()

#6.1
ans = 0
for i in file: ans += i[-1] == '8'
print(ans)

#6.2
ans = 0
for i in file: ans += i[-1] == '4' and '0' not in i
print(ans)

#6.3
ans = 0
for i in file: ans += i[-1] == '2' and i[-2] == '0'
print(ans)

#6.4
ans = 0
for i in file: 
    if i[-1] == '8': ans += int(i[:-1], 8)
print(ans)

#6.5
ans = dict()
for i in file:
    s = int(i[-1])
    ans[i] = int(i[:-1], s)
ans = sorted(ans.items(),key=lambda x:x[1])
print(ans[-1], ans[0])



