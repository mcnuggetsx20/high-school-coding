from utils import *

mandaty = Table('dane/mandaty.txt')
wykroczenia = Table('dane/wykroczenia.txt')
kierowcy = Table('dane/kierowcy.txt')

karani = set()

for i in mandaty:
    karani.add(i.Pesel)

mp = dict()
for i in kierowcy:
    if i.pesel not in karani:
        if i.miasto not in mp:
            mp[i.miasto] = 0
        mp[i.miasto] += 1

print( len(kierowcy) - len(karani) )

mp = sorted(mp.items(), key = lambda x: x[1], reverse=True)
for i in mp:
    print(i[0])
    break

