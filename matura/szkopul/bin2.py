n = int(input())

ans2 = 0
ans8 = 0
while n:
    a = input().strip()
    b = int(a, 2)
    ans2 += not b%2
    ans8 += not b%8
    n-=1
print(ans2, ans8)
