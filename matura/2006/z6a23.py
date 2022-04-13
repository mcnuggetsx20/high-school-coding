file = open('DANE/dane.txt', 'r').read().split()

mp = dict()
c = 0

for i in file:
    if i not in mp.keys():
        mp[i]=0
    mp[i]+=1

for i in mp:
    if c < mp[i]:
        c = mp[i]
        a = i
print(c, a)

