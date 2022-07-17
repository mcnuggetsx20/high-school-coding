from utils import *

uslugi = Table('Dane/uslugi.txt')

l,w = 0, 0

for i in uslugi:
    l += int(i.rata) * int( i.rodzaj_uslugi == 'L' )
    w += int(i.rata) * int( i.rodzaj_uslugi == 'W' )
print(w, l)


