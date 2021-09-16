pliczek = open('dane/98/oceny.txt', 'r').read().split('\n')
helper = open('dane/98/uczniowie.txt', 'r').read().split('\n')

tab = dict()
grades ={
        'IVA' : [0, 0],
        'IVB' : [0, 0],
        'IVC' : [0, 0],
        'IVD' : [0, 0],
        'IVE' : [0, 0],
        }
for i in range(len(pliczek)-1):
    pliczek[i] = pliczek[i].split()

for i in range(len(helper)-1):
    helper[i] = helper[i].split()
    if helper[i][-2] == 'IV':
        tab.update({helper[i][0] : helper[i][-2] + helper[i][-1]})

for i in range(len(pliczek)-1):
    if pliczek[i][3] == '1' and pliczek[i][2] in tab.keys():
        grades[tab[pliczek[i][2]]][0] += int(pliczek[i][-1])
        grades[tab[pliczek[i][2]]][1] += 1
for i in grades:
    print(i,'{0:.2f}'.format( grades[i][0] / grades[i][1]))
