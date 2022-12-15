n = int(input())

ans = ['', 0]

for i in range(n):
    a = input()
    temp = len(set(a))
    if temp > ans[1]:
        ans[0] = a
        ans[1] = temp
print(*ans)


