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
top = dict()

for i in uczen:
    idName[i['IdUcznia']] = i['Imie'] + ' ' + i['Nazwisko']
    top[i['IdUcznia']] = 0

for i in ewidencja:
    we = datetime.datetime.strptime(i['Wejscie'], '%Y-%m-%d %H:%M:%S')
    wy = datetime.datetime.strptime(i['Wyjscie'], '%Y-%m-%d %H:%M:%S')
    delta = abs(wy-we).seconds / 3600
    top[i['IdUcznia']] += delta

top = sorted(top.items(), key=lambda x:x[1],reverse=True)
for i in top:
    print(idName[i[0]], i[1])



