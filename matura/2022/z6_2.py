import datetime
klasa = open('dane/klasa.txt', 'r').read().split('\n')[:-1]
uczen = open('dane/uczen.txt', 'r').read().split('\n')[:-1]
ewidencja = open('dane/ewidencja.txt', 'r').read().split('\n')[:-1]

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

start = datetime.datetime.strptime('08:00', '%H:%M')

daty = dict()

for i in ewidencja:
    data = datetime.datetime.strptime(i['Wejscie'][:10], '%Y-%m-%d')
    godz = datetime.datetime.strptime(i['Wejscie'][11:], '%H:%M:%S')
    #2022-04-04 07:02:00
    if data not in daty:
        daty[data] = 0
    delta = datetime.timedelta(days = 0)
    daty[data] += int(godz-start < delta)

for i in daty:
    print(i, daty[i])



