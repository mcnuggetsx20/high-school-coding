class line:
    def __init__(self, headers, rows):
        for i, j in enumerate(headers):
            setattr(self, headers[i], rows[i])

def convert(table):
    headers = table[0].split(';')
    table = table[1:]
    for i,j in enumerate(table):
        rows = j.split(';')
        table[i] = line(headers, rows)
    return table

### usage example
klasa = open('Dane_2205/klasa.txt', 'r').read().split('\n')[:-1]
uczen = open('Dane_2205/uczen.txt', 'r').read().split('\n')[:-1]
ewidencja = open('Dane_2205/ewidencja.txt', 'r').read().split('\n')[:-1]

klasa = convert(klasa)
uczen = convert(uczen)
ewidencja = convert(ewidencja)

for i in uczen:
    print(i.Imie, i.IdKlasy)


