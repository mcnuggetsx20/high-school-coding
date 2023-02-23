file = open('dane/liczby.txt' ,'r').read().split()
file = [int(i) for i in file]

#4.1
ans = 0
def check(n):
    while True:
        if n== 1:
            return True
        if n < 3:
            return False
        n/=3

for i in file:
    ans += check(i)
print(ans)

#4.2
print()

def fact(tab):
    ans = 0
    temp = 1
    for i in tab:
        for j in range(1, i+1):
            temp *= j
        ans += temp
        temp = 1
    return ans

ans = []
for i in file:
    a = list(str(i))
    a = [int(i) for i in a]
    if i == fact(a): ans.append(i)
print(*ans)

#4.3
print()


from math import gcd
temp = [file[0]]
ans = []


for i in file[1:]:
    temp.append(i)
    if gcd(*temp) == 1:
        while gcd(*temp) == 1:
            temp.pop(0)
    if len(ans) < len(temp):
        ans = temp.copy()
print(ans[0], len(ans), gcd(*ans))


