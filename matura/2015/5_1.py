from utils import *

mandaty = Table('dane/mandaty.txt')
wykroczenia = Table('dane/wykroczenia.txt')

mp = dict()
for i in mandaty:
    mp[i.kod_wyk] = 0

for i in mandaty:
    mp[i.kod_wyk] +=1

mp = sorted(mp.items(), key = lambda x : x[1], reverse=True)

print(wykroczenia.find( [mp[0][0]] )[0].nazwa, mp[0][1])
    


