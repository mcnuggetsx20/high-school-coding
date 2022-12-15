n, m = map(int, input().split())
ans = [0, 10**9]
while n:
    a = list(map(int, input().split()))
    ans[0] = max(ans[0], max(a))
    ans[1] = min(ans[1], min(a))
    n-=1
print(' '.join(list(map(str, ans[::-1]))))
