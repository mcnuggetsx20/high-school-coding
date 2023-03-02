ile = open('Dane_PR2/dzialki.txt', 'r').read().split('\n\n')

for i in range(len(file)):
    a = file[i].split()
    a.reverse()
    tab = []
    for j in a:
        tab.append(j[::-1])
    for j in range(len(file)):
        if tab == file[j].split():
            print(i+1, j+1)



