pliczek = open('dane/98/oceny.txt', 'r').read().split('\n')

tab = dict()
for i in range(len(pliczek) - 1):
    ind = pliczek[i].split('\t')[1]
    if ind not in tab.keys():
        tab.update({ind : [0, False]})
    temp = tab[ind][1]
    tab[ind][0] += 1 * int(pliczek[i][-1] == '1')
    tab[ind][1] = tab[ind][0] > 10
    if not temp and tab[ind][1]:
        print(ind)
