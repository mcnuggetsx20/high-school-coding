def a(name):
    file = open(f'dane/{name}.txt').read().split('\n')[:-1]
    file = [dict(zip(file[0].split('\t'), i.split('\t'))) for i in file[1:]]
    globals()[name] = file

from collections import defaultdict as dd

def join(t1, t2, k):
    t2 = dd(lambda: {'missing': ''}) | {i[k]: i for i in t2}
    return [i | t2[i[k]] for i in t1]

a('gracze')
a('klasy')
a('jednostki')

#6.1
print('6.1')
ans = dd(lambda: 0)

for i in gracze:
    rok = i['data_dolaczenia'].split('-')[0]
    if rok != '2018': continue
    kraj = i['kraj']
    ans[kraj] += 1
ans = sorted(ans.items(), key=lambda x:x[1])[-5:][::-1]
for i in ans: print(*i)

print('\n6.2') #6.2
temp = join(jednostki, klasy, 'nazwa')
ans = dd(lambda: 0)
for i in temp:
    if 'elf' not in i['nazwa']: continue
    ans[i['nazwa']] += int(i['strzal'])
for i in ans: print(i, ans[i])

print('\n6.3') #6.3
trash = []
for i in jednostki:
    if i['nazwa'] == 'artylerzysta': trash.append(i['id_gracza'])

for i in gracze:
    if i['id_gracza'] not in trash: print(i['id_gracza'])

print('\n6.4') #6.4
temp = join(jednostki, klasy, 'nazwa')
ans = dd(lambda: 0)

for i in temp:
    speed = int(i['szybkosc'])
    klasa = i['nazwa']
    pos = list(map(int, [i['lok_x'], i['lok_y']]))
    ok = abs(pos[0]-100) + abs(pos[1] -100) <= speed
    if not ok: continue
    ans[klasa] += 1
for i in sorted(ans.items(), key=lambda x:x[0]): print(*i)

print('\n6.5') #6.5
board = dd(lambda:set())
for i in join(jednostki, gracze, 'id_gracza'):
    pos = f"{i['lok_x']} {i['lok_y']}"
    board[pos].add(i['id_gracza'])
    board[pos].add(i['kraj'])
ansa = 0
ansb= 0
for i in board: 
    if len(board[i]) <= 2: continue 
    ansa += 1; ansb += 'Polska' in board[i] 
print(ansa)
print(ansb)

    



