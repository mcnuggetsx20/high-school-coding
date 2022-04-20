file = open('Dane_2203/brenna.txt', 'r').read().split('\n')[1:-1]

for i in range(len(file)):
    file[i] = file[i].split()
    file[i][2] = float(file[i][2].replace(',', '.'))
    file[i][3] = float(file[i][3].replace(',', '.'))

mp = dict()
ok = False
temp = ''

for j in range(len(file)):
    i = file[j]
    a = i[2] > 0 and i[3] > 0
    if a and not ok:
        ok = True
        temp = i[0] + ' ' + i[1]
        mp[temp] = ['', '', 0, -1]

    if ok:
        mp[temp][3]+=1
        mp[temp][2]+=i[3] * 100

    if not a and ok:
        ok = False
        mp[temp][0]=i[0]
        mp[temp][1]=i[1]
        mp[temp][2] = int(mp[temp][2]) // 100

mx = 0
curr = ''
for i in mp:
    if mx < mp[i][3]:
        mx = mp[i][3]
        curr = i
print(curr, mp[curr][0], mp[curr][2])


