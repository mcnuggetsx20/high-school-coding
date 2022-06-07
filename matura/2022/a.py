klasa = open('Dane_2205/klasa.txt', 'r').read().split('\n')[:-1]
uczen = open('Dane_2205/uczen.txt', 'r').read().split('\n')[:-1]
ewidencja = open('Dane_2205/ewidencja.txt', 'r').read().split('\n')[:-1]

class line:
    def __init__(self, names, vals):
        for i,j in enumerate(names):
            setattr(self, names[i], vals[i])

def convert(tar):
    title = tar[0].split(';')
    tar = tar[1:]
    for i, j in enumerate(tar):
        temp = j.split(';')
        tar[i] = line(title, temp) 
    return tar

klasa = convert(klasa)
uczen = convert(uczen)
ewidencja = convert(ewidencja)

for i in uczen:
    print(i.Imie, i.IdKlasy)
