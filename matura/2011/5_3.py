from utils import *

osoby = Table('Dane_PR/osoby.txt')
psy = Table('Dane_PR/psy.txt')

mp = dict()

for i in osoby:
    mp[i.id_osoby] = 0

for i in psy:
    mp[i.id_osoby] += int(i.medale)

for i in sorted(mp.items(), key=lambda x:x[1], reverse=True):
    name = osoby.find([i[0]])[0].imie
    sur = osoby.find([i[0]])[0].nazwisko
    print(name, sur, i[1])
    break
