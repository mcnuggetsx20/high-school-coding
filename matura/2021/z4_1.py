file = open('DANE_2105/instrukcje.txt', 'r').read().split('\n')[:-1]

tab = []

for i in file:
    a = i.split()
    #print(a)
    if a[0] == 'DOPISZ':
        tab.append(a[1])

    elif a[0] == 'ZMIEN':
        tab[-1] = a[1]

    elif a[0] == 'USUN':
        tab.pop(-1)

    else:
        try:
            ind = tab.index(a[1])
        except ValueError:
            continue

        asc = ord(tab[ind])
        tab[ind] = chr( asc +1)
        if asc == 90:
            tab[ind] = 'A'
for i in tab:
    print(i, end='')
print()


