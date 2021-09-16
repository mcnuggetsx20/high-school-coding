pliczek = open('dane/98/przedmioty.txt', 'r').read().split('\n')

helper = dict()
tabelka = dict()
dates = [str(i) for i in range(9, 13)]
miesiace = ['wrz', 'paz', 'lis', 'gru']

for i in dates:
    tabelka.update({i: [0 for i in range(28)]})

for i in range(1, len(pliczek)-1):
    a = pliczek[i].split('\t')
    helper.update({a[0] : a[1]})
pliczek = open('dane/98/oceny.txt', 'r').read().split('\n')

for i in range(1, len(pliczek)-1):
    a = pliczek[i].split('\t')
    if a[-1] == '5' and a[1][-5] + a[1][-4] in dates:
        tabelka[a[1][-5] + a[1][-4]][int(a[-2])] += 1

for i in tabelka:
    print(i)
    for j in range(1, len(tabelka[i]) - 1):
        print(helper[str(j)], tabelka[i][j])



