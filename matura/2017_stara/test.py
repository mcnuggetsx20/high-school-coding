def f(name):
    tab = open(f'dane/{name}.txt', 'r').read().split('\n')[:-1]
    tab = [ dict(zip(tab[0].split('\t'), i.split('\t'))) for i in tab[1:]]
    globals()[name] = tab

def join(main, sec, key):
    sec = {i[key]: i for i in sec}
    return [ i | sec[i[key]] for i in main]

f('osoby')
f('wycieczki')
f('rezerwacje')

#6.1
from collections import defaultdict as dd
ans = dd(lambda: 0)

for i in join(rezerwacje, osoby, 'id_osoby'):
    imie = i['nazwisko'] + ' ' + i['imie']
    ans[imie] += 1
ans = sorted(ans.items(), key=lambda x:x[0])
for i in ans:
    if i[1] <= 3:continue
    print(' '.join(i[0].split()[::-1]))

