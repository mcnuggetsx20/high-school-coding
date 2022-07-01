from utils import *

studenci = Table('dane/studenci.txt')
meldunek = Table('dane/meldunek.txt')
#wypozyczenia = Table('dane/wypozyczenia.txt')

logged = set()

for i in meldunek:
    logged.add(i.pesel)

ans = []
for i in studenci:
    if i.pesel not in logged:
        ans.append(i.nazwisko + ' ' + i.imie)
ans.sort()
for i in ans:
    print(i)





