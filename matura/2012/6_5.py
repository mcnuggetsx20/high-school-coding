from utils import *

uslugi = Table('Dane/uslugi.txt')
tablice = Table('Dane/tablice.txt')
nip = Table('Dane/nip_firm.txt')

mp = dict()
for i in uslugi:
    kon = tablice.find( [i.ozn] )[0].powiat == 'Konin'

    if not kon:
        continue

    if i.NIP not in mp:
        mp[i.NIP] = [0, 0]

    mp[i.NIP][0] += int( i.rata )
    mp[i.NIP][1] += 1

for i in mp:
    name = nip.find( [i] )[0].firma
    avg = mp[i][0] / mp[i][1]
    #avg = round(avg, 2)
    print(name , avg)





