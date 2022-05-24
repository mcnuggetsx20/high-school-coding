file = open('Dane_2203/brenna.txt', 'r').read().split('\n')[1:-1]

for i in range(len(file)):
    file[i] = file[i].split()
    file[i][2] = float(file[i][2].replace(',', '.'))
    file[i][3] = float(file[i][3].replace(',', '.'))
#file.append(['','','',''])

mp = dict()

for i in file:
    if i[1] not in mp.keys():
        mp[i[1]]=[0,0]

    mp[i[1]][1] += 1
    mp[i[1]][0] += i[2]

for i in mp:
    mp[i][0] = round(mp[i][0] / mp[i][1],2)
    print(i, mp[i])


