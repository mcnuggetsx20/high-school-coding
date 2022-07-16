from utils import *

mandaty = Table('dane/mandaty.txt')
wykroczenia = Table('dane/wykroczenia.txt')
kierowcy = Table('dane/kierowcy.txt')

mp = dict()

for i in mandaty:
    a = i.data_wyk.split('-')[1]
    mp[a] = [0, 0]

for i in mandaty:
    a = i.data_wyk.split('-')[1]
    mp[a][1] +=1

    kod = i.kod_wyk
    kwota = int( wykroczenia.find( [kod] )[0].mandat )
    mp[a][0] += kwota
mp = sorted(mp.items(), key = lambda x:x[1][1])
for i in mp:
    print(i)


