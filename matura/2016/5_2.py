from utils import *

#studenci = Table('dane/studenci.txt')
meldunek = Table('dane/meldunek.txt')
#wypozyczenia = Table('dane/wypozyczenia.txt')

rooms = dict()
for i in meldunek:
    rooms[i.id_pok] = 0

for i in meldunek:
    rooms[i.id_pok] +=1

s = 0
for i in rooms:
    s+= rooms[i]

ans = s / len(rooms)
print(round(ans,4))



