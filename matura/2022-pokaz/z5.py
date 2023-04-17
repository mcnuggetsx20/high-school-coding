from collections import defaultdict as dd
def a(name):
    file = open(f'dane/{name}.txt', 'r').read().split('\n')[:-1]
    file = [dict(zip(file[0].split(';'), i.split(';'))) for i in file[1:]]
    globals()[name] = file

def join(t1, t2, k):
    t2 = dd(lambda: {'missing': ''}) | {i[k]: i for i in t2}
    return [i | t2[i[k]] for i in t1]

a('statki')
a('przybycia')
a('kody')

#5.1
ans = dd(lambda: 0)
for i in przybycia:
    rok = i['Data_przybycia'][-4:]
    ans[rok] += 1
for i in sorted(ans.items(), key = lambda x:x[0]): print(*i)

#5.2
print()
ans = dd(lambda: [0, 0])
for i in join(przybycia, statki, 'Nr_IMO'):
    nab = i['Nabrzeze']
    name = i['Nazwa_statku']
    lad = int(i['Ladownosc'])
    if ans[nab][1] < lad: ans[nab] = [name, lad]
for i in sorted(ans.items(), key = lambda x:x[0]): print(*i)

#5.3
print()
trash = set()
for i in join(przybycia, kody, 'Bandera'):
    kont = i['Kontynent']
    nab = i['Nabrzeze']
    if kont == 'EUROPA': trash.add(nab)
ans = set()
for i in przybycia:
    nab = i['Nabrzeze']
    if nab not in trash: ans.add(nab)
for i in ans: print(i)


