n = int(input())

def fact(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

N = 0
while n:
    a = input()
    ans = 0
    for i in a:
        ans += fact(int(i))

    if ans == int(a):
        N+=1
        print(a)
    n-=1
if not N:
    print('brak')
