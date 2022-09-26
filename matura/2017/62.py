file = open('dane/dane.txt', 'r').read().split('\n')[:-1]
file = [i.split() for i in file]

ans = 0
for i in file:
    ans += int(i != i[::-1])
print(ans)




