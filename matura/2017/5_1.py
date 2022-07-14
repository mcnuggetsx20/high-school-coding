from utils import *

druzyny = Table('dane/druzyny.txt')
sedziowie = Table('dane/sedziowie.txt')
wyniki = Table('dane/wyniki.txt')

mp = {
    'T' : 0,
    'L' : 0,
    'P' : 0,
        }

for i in wyniki:
    op = i.Id_druzyny
    op = druzyny.find([op])[0].Miasto
    mp[i.Rodzaj_meczu] += int( op == 'Kucykowo')

for i in mp:
    print(i, mp[i])

############ b:

mp = dict()
for i in wyniki:
    y = i.Data_meczu.split('-')[0]
    mp[y] = 0

for i in wyniki:
    op = i.Id_druzyny
    op = druzyny.find([op])[0].Miasto
    y = i.Data_meczu.split('-')[0]
    mp[y] += int( op== 'Kucykowo' )

for i in sorted(mp.items(), key = lambda x:x[1], reverse=True):
    print(i[0], i[1])
    break


