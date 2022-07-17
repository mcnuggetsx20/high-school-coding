from utils import *

uslugi = Table('Dane/uslugi.txt')
tablice = Table('Dane/tablice.txt')
nip = Table('Dane/nip_firm.txt')

ans = []

tar = nip.find(['BARTEX'])[0].NIP

for i in uslugi:
    if i.NIP == tar:
        ans.append((i.ozn, i.nr))

ans = sorted(ans, key=lambda x:x[1], reverse=True)

for i in ans:
    print(i[0], i[1])



