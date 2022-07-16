from utils import *

#osoby = Table('Dane_PR/osoby.txt')
psy = Table('Dane_PR/psy.txt')

m = 0
f = 0
for i in psy:
    m += int(i.plec=='samiec')
    f += int(i.plec =='samica')
print(m, f)

