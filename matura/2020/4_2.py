file = open('Dane_PR2/pary.txt', 'r').read().split()

ex = ''
ans = 0
for i in range(1, len(file), 2):
    for j in range(1, len(file[i])):
        if file[i][j] != ex:
            ans = 1
            ex = file[i][j]
        else:
            ans += 1

                














