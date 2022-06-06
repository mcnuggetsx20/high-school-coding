plik = open("Dane_2205/soki.txt")
dane = plik.read().split('\n')
import datetime
from traceback import print_tb
del dane[-1]
del dane[0]

dzien = datetime.timedelta(1)
glowny = 30000
filiaBoost = 0
filiaIlosc = 0
dodaj = 12000
pocz = datetime.date(2021,1,2)
for i in range(0, len(dane)):
    ilosc = int(dane[i].split('\t')[-1])
    data = dane[i].split('\t')[1].split(".")
    DataTeraz = datetime.date(int(data[2]),int(data[1]), int(data[0]))
    if DataTeraz == pocz + dzien:
        pocz = DataTeraz
        if DataTeraz.isoweekday() == 6 or DataTeraz.isoweekday() == 7:
            glowny += 5000
        else:
            glowny += dodaj
    if glowny >= ilosc:
        glowny -= ilosc
    else:
        filiaBoost += ilosc
        filiaIlosc += 1
print(filiaIlosc,filiaBoost)
print('---')


glowny = 30000
filiaBoost = 0
filiaIlosc = 0
dodaj = 13200
pocz = datetime.date(2021,1,2)
for i in range(0, len(dane)):
    ilosc = int(dane[i].split('\t')[-1])
    data = dane[i].split('\t')[1].split(".")
    DataTeraz = datetime.date(int(data[2]),int(data[1]), int(data[0]))
    if DataTeraz == pocz + dzien:
        pocz = DataTeraz
        if DataTeraz.isoweekday() == 6 or DataTeraz.isoweekday() == 7:
            glowny += 5000
        else:
            glowny += dodaj
    if glowny >= ilosc:
        glowny -= ilosc
    else:
        filiaBoost += ilosc
        filiaIlosc += 1
#print(filiaIlosc,filiaBoost)
#print('---')
print(13200)
