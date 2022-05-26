file = open('Dane_2205/soki.txt', 'r').read().split('\n')[:-1]

temp = file[0].split('\t')
file = file[1:]
for i, j in enumerate(file):
    a = file[i].split('\t')
    file[i]= dict(zip(temp, a))

mp = dict()
for i in file:
    a = i['magazyn']
    if a not in mp:
        mp[a] = 0
    mp[a]+=int(i['wielkosc_zamowienia'])
print(mp)

