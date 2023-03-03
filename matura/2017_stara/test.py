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

temp = join(rezerwacje, osoby, 'id_osoby')


