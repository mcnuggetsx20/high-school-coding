from utils import *

studenci = Table('dane/studenci.txt')
#meldunek = Table('dane/meldunek.txt')
#wypozyczenia = Table('dane/wypozyczenia.txt')

m = 0
w = 0
for i in studenci:
    m +=  int(i.pesel[-2])%2 
    w += int( not int(i.pesel[-2])%2 )

print('mezczyzni: ' + str(m), '\nkobiety: ' + str(w))

