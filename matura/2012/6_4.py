from utils import *

uslugi = Table('Dane/uslugi.txt')
tablice = Table('Dane/tablice.txt')
nip = Table('Dane/nip_firm.txt')

ans = set()

for i in uslugi:

    o = i.ozn
    o = tablice.find( [o] )[0]
    if o.rodzaj == 'z':
        ans.add(o.powiat)

ans =list(ans)
ans.sort()
for i in ans:
    print(i)
    






