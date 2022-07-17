from utils import *

uslugi = Table('Dane/uslugi.txt')
nip = Table('Dane/nip_firm.txt')

mp = dict()

for i in nip:
    mp[i.NIP] = 0

for i in uslugi:
    mp[i.NIP] += int( i.rodzaj_uslugi == 'L' )

mp = sorted(mp.items(), key = lambda x:x[1], reverse=True)

print( nip.find( [mp[0][0]] )[0].firma, mp[0][1])


