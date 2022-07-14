from utils import *

aktorzy = Table('Dane_PR2/aktorzy.txt')
nagrody = Table('Dane_PR2/nagrody.txt')
filmy = Table('Dane_PR2/filmy.txt')

mp = dict()

for i in aktorzy:
    temp = nagrody.find([i.id_aktora])
    a = ''
    for j in temp:
        a += j.kategoria
    if 'pierwszo' in a and 'drugo' in a:
        #mp[i.id_aktora] = True
        r1 = list()
        r2 = list()
        for j in temp:
            if 'pierwszo' in j.kategoria:
                r1.append( int(filmy.find( [j.id_filmu] )[0].rok))
            if 'drugo' in j.kategoria:
                r2.append( int(filmy.find( [j.id_filmu] )[0].rok))
        r1.sort()
        r2.sort()
        mp[i.id_aktora] = [r1, r2] 

for i in mp:
    a = aktorzy.find([i])[0]
    print(a.imie, a.nazwisko)
    print(max(mp[i][1][-1] -mp[i][0][0] , mp[i][0][-1]-mp[i][1][0]))
    

