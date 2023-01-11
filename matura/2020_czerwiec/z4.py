file = open('dane/pary.txt', 'r').read().split('\n')[:-1]
file = [ i.split() for i in file]

sieve = [True] * 101
sieve[0]=False
sieve[1] = False
for i in range(2, 11):
    for j in range(i, 101//i + 1):
        sieve[i*j] = False

#4.1
for i in file:
    a = int(i[0])
    if a%2: continue

    for j, v in enumerate(sieve):
        if not v: continue

        if v and sieve[a-j]:
            print(a, j, a-j)
            break

#4.2
print()
for i in file:
    a = i[1]
    
    mx = 1
    ans = a[0]
    temp = a[0]
    for j in range(1, len(a)):
        if a[j] == a[j-1]:
            temp += a[j]
        else:
            if len(temp) > mx:
                mx = len(temp)
                ans = temp
            temp = a[j]

    if len(temp) > mx:
        mx = len(temp)
        ans = temp

    print(ans, mx)

#4.3
print()
tab = []
for i in file:
    a = int(i[0])
    if a !=len(i[1]): continue
    tab.append( tuple(i))
tab.sort()
print(*tab[0])



