from collections import defaultdict as dd
def a(name):
    file = open(f'dane/{name}.txt').read().split('\n')[:-1]
    file = [dict(zip(file[0].split('\t'), i.split('\t'))) for i in file[1:]]
    globals()[name] = file

def join(t1, t2, k):
    t2 = dd(lambda: {'missing': ''}) | {i[k]: i for i in t2}
    return [i | t2[i[k]] for i in t1]

a('komputery')
a('awarie')
a('naprawy')

#6.1
ans = dd(lambda:0)
for i in komputery:
    ind = i['Pojemnosc_dysku']
    ans[ind] += 1
ans = sorted(ans.items(),key=lambda x:x[1])[-10:][::-1]
print(6.1)
for i in ans:print(*i)

#6.2
temp = join(naprawy, awarie, 'Numer_zgloszenia')
temp = join(temp, komputery, 'Numer_komputera')
ans = dd(lambda:0)

for i in temp:
    if i['Sekcja'] != 'A' or i['Rodzaj'] != 'wymiana': continue
    ind = i['Numer_komputera']
    ans[ind] += 1

print('\n6.2')
for i in ans: 
    if ans[i] >= 10: print(i, ans[i])

#6.3
print('\n6.3')
sekcje = dd(lambda:0)
for i in komputery: sekcje[i['Sekcja']] += 1
ans = dd(lambda: dd(lambda: 0))
temp = join(awarie, komputery, 'Numer_komputera')
for i in temp:
    data= i['Czas_awarii'].split()[0]
    ans[data][i['Sekcja']] += 1
for i in ans:
    for j in ans[i]:
        if ans[i][j] == sekcje[j]: print(i, j)

#6.4
from datetime import timedelta, datetime
ans = dd(lambda:0)
ans2 = dd(lambda: [0,0])

temp = join(awarie, naprawy, 'Numer_zgloszenia')
for i in temp:
    start = datetime.strptime(i['Czas_awarii'], '%Y-%m-%d %H:%M:%S')
    end = datetime.strptime(i['Czas_naprawy'], '%Y-%m-%d %H:%M:%S')
    ans[i['Numer_zgloszenia']] = abs(start-end).seconds
    ans2[i['Numer_zgloszenia']] = [start, end]
ans =max(ans, key=ans.get) 
print('\n6.4\n', ans)
print(*ans2[ans])

#6.5
temp = join(awarie, komputery, 'Numer_komputera')
ans = 0
trash = []
for i in temp:
    if int(i['Priorytet']) >= 8: trash.append(i['Numer_komputera'])
for i in komputery:
    ans +=  i['Numer_komputera'] not in trash
print('\n6.5\n', ans)





