n = int(input())

def check(n):
    for i in range(1000):
        if 3**i == n:
            return True
        if 3**i > n:
            return False

ans = 0
while n:
    a = int(input())
    ans += check(a)
    n-=1
print(ans)
