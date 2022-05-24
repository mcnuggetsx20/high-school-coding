file = open('Dane_2203/brenna.txt', 'r').read().split('\n')[1:-1]

for i in range(len(file)):
    file[i] = file[i].split()
    file[i][2] = float(file[i][2].replace(',', '.'))
    file[i][3] = float(file[i][3].replace(',', '.'))

ans= 0
s =0 
ok = False
for i in file:
    if ok:
        ok = False
        continue

    if i[2] <= 0 and i[3] >= 0:
        s += i[3]
        if s > 4:
            ans +=1
            ok = True
            s = 0

    elif i[2] >0 and i[3] > 0:
        s=0
print(ans)


