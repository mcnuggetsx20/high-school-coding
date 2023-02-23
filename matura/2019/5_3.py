from utils import *

aktorzy = Table('Dane_PR2/aktorzy.txt')
nagrody = Table('Dane_PR2/nagrody.txt')
filmy = Table('Dane_PR2/filmy.txt')

mx = 0
mp = dict()

for i in nagrody:
    mp[i.id_aktora] = 0

for i in nagrody:
    mp[i.id_aktora] +=1

best = sorted(mp.items(), key = lambda x:x[1], reverse=True)[0]
name = aktorzy.find([best[0]])[0]
name = name.imie +' ' + name.nazwisko

ans = []

print(name)
for i in nagrody:
    if i.id_aktora == best[0]:
        temp = filmy.find([i.id_filmu])[0]
        ans.append( [temp.rok, temp.tytul])
for i in ans:
    print(i[0], '\t', i[1])


