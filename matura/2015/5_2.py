from utils import *

mandaty = Table('dane/mandaty.txt')
wykroczenia = Table('dane/wykroczenia.txt')
kierowcy = Table('dane/kierowcy.txt')

mp = dict()

for i in kierowcy:
    #if i.data_prawa_jazdy.split('-')[0] == '2013':
    mp[i.pesel] = 0

for i in mandaty:
    kod = i.kod_wyk
    pkt = wykroczenia.find([kod])[0].punkty
    mp[i.Pesel] += int( pkt )

ans = []
for i in kierowcy:
    if i.data_prawa_jazdy.split('-')[0] == '2013' and mp[i.pesel] > 20:
        print(i.pesel, mp[i.pesel])



