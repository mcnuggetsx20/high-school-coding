n, m = map(int, input().split())

ans = 0
while m:
    a = input()
    cord = [1,1]
    for i in a:
        cord[0] += i=='E'
        cord[0] -= i=='W'

        cord[1] -= i=='N'
        cord[1] += i=='S'

        if cord[0] > n or cord[0] < 1 or cord[1] > n or cord[1] < 1:
            ans += 1
            break
    m-=1
print(ans)
