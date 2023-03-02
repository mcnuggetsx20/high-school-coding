file = open('dane/pomiary.txt', 'r').read().split('\n')[:-1]
file = [ dict(zip(file[0].split(';'), i.split(';'))) for i in file[1:]]

#5.1
godz = ['0' + str(i) for i in range(5, 10)]
godz += [str(i) for i in range(10, 13)]
avg = 0
c = 0
for i in file:
    pom = float(i['czujnik5'].replace(',', '.'))
    g = i['godzina'].split(':')
    if g[0] == '12' and g[1] != '00': continue
    if g[0] not in godz: continue

    avg += pom
    c += 1
print( round(avg/c, 2))

#5.2
print()
from collections import defaultdict as dd
ans = dd(lambda:[])

for i in file:
    for j in i:
        if 'cz' not in j: continue
        temp = float(i[j].replace(',', '.'))
        temp = int(temp + 273.15)
        ans[j].append(temp)
for i in ans:
    ans[i] = sorted(ans[i], key = lambda x:ans[i].count(x))
    print(i, ans[i][-1])

#5.3
print()
ans = dd(lambda:[])

for i in file:
    pom = float(i['czujnik10'].replace(',', '.'))
    m = i['data'].split('-')[1]
    ans[m].append(pom)

for i in ans:
    print(i, round(sum(ans[i])/len(ans[i]), 2))

#5.4
print()

tab = [i for i in range(-9, 15)]
ans = 0
for i in file:
    for j in i:
        if 'cz' not in j: continue

        temp = float(i[j].replace(',', '.'))
        ans += int(temp) in tab
        ans += temp == 15
print(ans, len(file)*10-ans)

#5.5
print()
first = True
second = True
dni = ['0' + str(i) for i in range(5, 10)]
dni += '10'
for i in file:
    temp = []
    for j in i:
        if 'cz' not in j: continue
        temp.append(float(i[j].replace(',', '.')))

    data = i['data'].split('-')
    d = data[-1]
    m = data[1]

    if d in dni:
        temp[0] -= 1.2
        temp[1] -= 1.2
        temp[8] -= 1.2

    if m in ['07','08']:
        temp[7] = round(1.07 * temp[7], 2)

    if i['data'] == '2016-05-05' and first:
        first = False
        for j in [0,1,7,8]: print(temp[j], end= ' ')
        print()
        for j in [0,1,7,8]: print(round(temp[j] + 0.9, 2), end= ' ')
        print()


    if i['data'] == '2016-07-07' and second:
        second = False
        for j in [0,1,7,8]: print(temp[j])
        for j in [0,1,7,8]: print(temp[j])


