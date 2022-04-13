pliczek = open('dane/98/uczniowie.txt', 'r').read().split('\n')
tabelka = []
klasy = dict()
for i in range(1, len(pliczek)-1):
    tabelka.append(pliczek[i].split())
for i in tabelka:
    a = {i[-2] + i[-1] : [0, 0]} #wszyscy - dziewczyny
    klasy.update(a)
for i in tabelka:
    ind = i[-2] + i[-1]
    klasy[ind][0] += 1
    klasy[ind][1] += 1 * int(i[1][-1] == 'a')
for i in klasy: 
    if klasy[i][0] / klasy[i][1] < 2:
        print(i)
