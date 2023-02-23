from utils import *

aktorzy = Table('Dane_PR2/aktorzy.txt')
nagrody = Table('Dane_PR2/nagrody.txt')
filmy = Table('Dane_PR2/filmy.txt')

mn = 10**9
ans = ''
for i in nagrody:
    f = int(filmy.find([i.id_filmu])[0].rok)
    uro = int(aktorzy.find([i.id_aktora])[0].data_ur.split('-')[0])
    age = abs(f -uro)
    if age < mn:
        ans = aktorzy.find([i.id_aktora])[0].imie
        ans += ' ' + aktorzy.find([i.id_aktora])[0].nazwisko
        mn = age
print(ans, mn)


