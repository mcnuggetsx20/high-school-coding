def f(name):
    tab = open(f'dane/{name}.txt', 'r').read().split('\n')[:-1]
    tab = [ dict(zip(tab[0].split('\t'), i.split('\t'))) for i in tab[1:]]
    globals()[name] = tab

def join(main, sec, key):
    sec = {i[key]: i for i in sec}
    res = [{**i, **sec[i[key]]} for i in main]
    return res

f('osoby')
f('wycieczki')
f('rezerwacje')

temp = join(rezerwacje, osoby, 'id_osoby')
for i in temp:
    print(i)




