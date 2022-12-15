n = int(input())
k = int(input())

while n:
    ans = ''
    a = input()
    for i in a:
        temp = (ord(i) - 65 + k)%26 + 65
        ans += chr(temp)
    print(ans)
    n-=1
