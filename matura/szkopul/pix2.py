n, m = map(int, input().split())

ans = 0
while n:
    a = list(map(int, input().split()))
    ans += a != a[::-1]
    n-=1
print(ans)
