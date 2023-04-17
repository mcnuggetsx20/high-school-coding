file = open('dane/sygnaly.txt').read().split('\n')[:-1]

#4.1
c = 1
ans = ''
for i in file:
    if c==40: ans+=i[9]; c= 0
    c += 1
print('4.1\n', ans)

#4.2
mx = 0
ans = ''
for i in file:
    temp = len(set(i))
    if mx < temp: mx = temp; ans = i
print('\n4.2\n', ans, mx)

#4.3
ans = []
for i in file:
    mx = ord(max(i)); mn = ord(min(i))
    if abs(mx - mn) <= 10: ans.append(i)
print('\n4.3\n', ans)




