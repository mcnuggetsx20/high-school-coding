n = int(input())

ans = 0
while n:
    a = input()
    ans += a.count('0') > a.count('1')
    n-=1
print(ans)
