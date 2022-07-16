from utils import *

osoby = Table('Dane_PR/osoby.txt')
psy = Table('Dane_PR/psy.txt')

mp = dict()
for i in psy:
    mp[i.id_osoby] = 0
for i in psy:
    mp[i.id_osoby] +=1

ans = []
for i in mp:
    if mp[i] > 8:
        name = osoby.find([i])[0].imie
        sur = osoby.find([i])[0].nazwisko
        ans.append(sur+ ' ' + name)
ans.sort()
for i in ans:
    print(i)





