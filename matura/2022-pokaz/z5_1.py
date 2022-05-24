file = open('Dane_2203/przybycia.txt', 'r').read().split('\n')[1:]

for i in range(len(file)):
    file[i] = file[i].split(';')

mp = dict()

for i in file:
    a = i[1][-4:]
    if a not in mp.keys():
        mp[a] = 0
    mp[a] += 1

for i in mp:
    print(i, mp[i])
