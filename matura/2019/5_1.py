from utils import *

nagrody = Table('Dane_PR2/nagrody.txt').group('id_aktora')
aktorzy = Table('Dane_PR2/aktorzy.txt').find(nagrody)

mp = dict()
for i in aktorzy:
    mp[i.kraj_urodzenia] = 0
for i in aktorzy:
    mp[i.kraj_urodzenia] +=1

for i in sorted(mp.items(), key = lambda x:x[1]):
    print(i[0],i[1])



