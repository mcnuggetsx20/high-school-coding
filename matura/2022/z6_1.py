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

save = []
ans=  0
profs = dict()
ucz = dict()

for i in klasa:
    profs[i['IdKlasy']] = i['ProfilKlasy']

for i in uczen:
    ind = i['IdKlasy']
    if i['Imie'][-1] == 'a' and profs[ind] == 'biologiczno-chemiczny':
        print(i['Imie'], profs[ind])
        ucz[i['IdUcznia']] = True

for i in ewidencja:
    if i['IdUcznia'] in ucz.keys():
        ans += 1

print(ans)


