import datetime
klasa = open('Dane_2205/klasa.txt', 'r').read().split('\n')[:-1]
uczen = open('Dane_2205/uczen.txt', 'r').read().split('\n')[:-1]
ewidencja = open('Dane_2205/ewidencja.txt', 'r').read().split('\n')[:-1]

def manage(file):
    temp = file[0].split(';')
    file = file[1:]
    for i, j in enumerate(file):
        a = file[i].split(';')
        file[i]= dict(zip(temp, a))
    return file

klasa = manage(klasa)
uczen = manage(uczen)
ewidencja = manage(ewidencja)

idName = dict()
obecni = []

ctrl = '2022-04-06'

for i in uczen:
    idName[i['IdUcznia']] = i['Imie'] + ' ' + i['Nazwisko']

for i in ewidencja:
    if i['Wejscie'][:10] == ctrl:
        obecni.append(i['IdUcznia'])

for i in uczen:
    if i['IdUcznia'] not in obecni:
        print(i['Imie'], i['Nazwisko'])


