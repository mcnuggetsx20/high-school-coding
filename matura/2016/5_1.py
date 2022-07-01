from utils import *

studenci = Table('dane/studenci.txt')
#meldunek = convert('dane/studenci.txt')
wypozyczenia = Table('dane/wypozyczenia.txt')

mp = dict()
ksiazki = dict()
for i in wypozyczenia:
    mp[i.pesel] = 0
    ksiazki[i.pesel] =[]

for i in wypozyczenia:
    mp[i.pesel] += 1
    ksiazki[i.pesel].append(i.tytul)

ans = sorted(mp.items(), key = lambda x:x[1], reverse=True)[0]

tar = studenci.find(ans[0])[0]
print(tar.imie, tar.nazwisko)

for i in ksiazki[ans[0]]:
    print(i)

