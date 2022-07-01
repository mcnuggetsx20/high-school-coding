from utils import *

studenci = Table('dane/studenci.txt')
meldunek = Table('dane/meldunek.txt')
wypozyczenia = Table('dane/wypozyczenia.txt')

mp = dict()
ans = 0
for i in wypozyczenia:
    room = meldunek.find(i.pesel)
    if not len(room): continue

    mp[ room[0].id_pok ] = set()

for i in wypozyczenia:
    room = meldunek.find(i.pesel)
    if not len(room): 
        ans += 1
        continue

    mp[ room[0].id_pok ].add(i.tytul)

for i in mp:
    ans += len(mp[i])
print(ans)





