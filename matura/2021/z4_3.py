file = open('DANE_2105/instrukcje.txt', 'r').read().split('\n')[:-1]

mp = dict()

for i in range(65, 91):
    mp[chr(i)] = 0

for i in file:
    a = i.split()
    if a[0] == 'DOPISZ':
        mp[a[1]] += 1
for i in sorted(mp.items(), key=lambda x:x[1], reverse=True):
    print(i[0], i[1])
    break


