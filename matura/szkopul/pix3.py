n, m = map(int, input().split())

ans = 0
check = [[False] * m for i in range(n)]
prev = list(map(int, input().split()))

for k,i in enumerate(prev[:-1]):
    temp = abs(i - prev[k+1]) > 128
    check[0][k] = temp or check[0][k]
    check[0][k+1] = temp or check[0][k+1]

for i in range(1, n):
    curr = list(map(int, input().split()))
    for k,j in enumerate(curr):
        try:
            temp = abs(j - curr[k+1]) > 128
            check[i][k] = temp or check[i][k]
            check[i][k+1] = temp or check[i][k+1]

        except IndexError:
            pass

        temp = abs(j - prev[k]) > 128
        check[i-1][k] = temp or check[i-1][k]
        check[i][k] = temp or check[i][k]

    prev = curr.copy()

for i in check:
    for j in i:
        ans += j
print(ans)
