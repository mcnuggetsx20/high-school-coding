file = open('dane/napisy.txt', 'r').read().split()

#4.1

tab = [str(i) for i in range(10)]

ans = 0
for i in file:
    for j in i:
        ans += j in tab
print(ans)
print()

#4.2

ans = ''
for i,v in enumerate(file):
    if (i+1)%20: continue
    ind = (i+1)//20
    ans += v[ind-1]

print(ans)
print()

#4.3

ans = ''
for i in file:
    if i[::-1] == i: continue

    ok1 = (i[:-1] == i[:-1][::-1])
    ok2 = (i[1:] == i[1:][::-1])


    if not (ok1 or ok2): 
        continue

    ans += i[(49//2) + ok2]

print(ans)
print()
    

#4.4

ans = ''
ok = False
for i in file:
    if ok: break
    temp = [j for j in i if j in tab]
    if len(temp)%2: temp.pop(-1)
    if not temp: continue

    temp = [ int(temp[j] + temp[j+1]) for j in range(0, len(temp[:-1]), 2)]

    for j in temp:
        if j < 65 or j>90: continue
        ans += chr(j)

        if ans[-3:] == 'XXX':
            print(ans)
            ok = True
            break



