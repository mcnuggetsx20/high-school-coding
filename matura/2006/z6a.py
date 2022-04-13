file = open('DANE/dane.txt', 'r').read().split()

mp = dict()
c = 0

for i in file:
    if i not in mp.keys():
        mp[i]=0
    mp[i]+=1

for i in mp:
    c += int(mp[i]>1)
print(c)


