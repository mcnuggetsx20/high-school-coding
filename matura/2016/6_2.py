file = open('dane/dane_6_2.txt', 'r').read().split('\n')[:-1]

for i in file:
    a = i.split()
    if len(a)==1: continue

    ans = ''
    k = int(a[1])%26
    for j in a[0]:
        num = (ord(j) -65 + 26 -k)%26 + 65
        ans += chr(num)
    print(ans)

