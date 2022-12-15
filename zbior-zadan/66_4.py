#66.4
file = open('dane/66/trojki.txt', 'r').read().split('\n')[:-1]
file = [[int(i) for i in i.split()] for i in file]

def check(a):
    a = sorted(a)
    return int(a[0] + a[1] > a[2])

ans = 0
c = 0
temp = 0

for i in file:
    curr = check(i)
    temp = curr* (temp + 1)
    ans = max(ans, temp)
    c += curr

print('liczba trojek:', c)
print('najdluzszy ciag:', ans)


