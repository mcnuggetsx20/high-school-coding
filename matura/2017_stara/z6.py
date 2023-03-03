def f(name):
    tab = open(f'dane/{name}.txt', 'r').read().split('\n')[:-1]
    tab = [ dict(zip(tab[0].split('\t'), i.split('\t'))) for i in tab[1:]]
    globals()[name] = tab

f('osoby')
f('wycieczki')
f('rezerwacje')


from collections import defaultdict as dd

#6.1
ans = dd(lambda:0)
imiona = {i['id_osoby']: i['imie'] + ' ' + i['nazwisko'] for i in osoby }

for i in rezerwacje:
    os = i['id_osoby']
    imie = ' '.join(imiona[os].split()[::-1])
    ans[imie] += 1
temp = []
for i in ans:
    if ans[i] > 3: temp.append(i)
temp.sort()
for i in temp: print(*i.split()[::-1])

#6.2
print()
ans = dd(lambda: 0)
cennik = {i['id_wycieczki']: int(i['cena']) for i in wycieczki}

for i in rezerwacje:
    os = i['id_osoby']
    imie = imiona[os]
    baza = cennik[ i['id_wycieczki']]
    cena = int(i['dorosli']) * baza + int(i['dzieci']) * baza*0.5
    ans[imie] += cena
ans = sorted(ans.items(), key=lambda x:x[1])
print(*ans[-1])

#6.3
print()
ans = dd(lambda: 0)
msc = {i['id_wycieczki']: int(i['data_od'].split('-')[1]) for i in wycieczki}

for i in rezerwacje:
    mies = msc[i['id_wycieczki']]
    ans[mies] += 1

for i in sorted(ans.items(), key=lambda x:x[0]): print(*i)

#6.4
print()
wyloty = {i['id_wycieczki'] :i['wylot'] for i in wycieczki}
kraje = {i['id_wycieczki'] :i['kraj'] for i in wycieczki}
ans = dd(lambda: dd(lambda: 0))

for i in rezerwacje:
    ind = i['id_wycieczki']
    lotnisko = wyloty[ind]
    kraj = kraje[ind]
    ans[lotnisko][kraj] += 1
for i in ans:
    print(i)
    for j in ans[i]:
        print('\t', j, ans[i][j])
    print()










