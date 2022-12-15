n = int(input())

tab = [chr(i) for i in range(65, 91)][::-1]
while n:
    ans = ''
    a, k = input().split(); k = int(k)

    for i in a:
        temp = (tab.index(i) + k) % 26
        ans += tab[temp] 
    print(ans)
    n-=1

