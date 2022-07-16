from utils import *

osoby = Table('Dane_PR/osoby.txt')
psy = Table('Dane_PR/psy.txt')

mp = dict()

for i in osoby:
    mp[i.id_osoby] = False

for i in psy:
    mp[i.id_osoby] = 'owczarek' in i.rasa or mp[i.id_osoby]

ans = 0
for i in mp:
    ans += int( mp[i] )
print(ans)


