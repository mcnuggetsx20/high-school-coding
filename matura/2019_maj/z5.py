file = open('dane/pogoda.txt','r').read().split('\n')[:-1]
file = [dict(zip(file[0].split(';'), i.split(';'))) for i in file[1:]]

#5.1
ans = 0
for i in file:
    t = float(i['Temperatura'].replace(',','.'))
    o = int(i['Opad'])
    ans += t >= 20 and o <= 5
print(ans)

#5.2
print()
ans = []
temp = [1]
last = float(file[0]['Temperatura'].replace(',','.'))

for i in range(1, len(file)):
    t = float(file[i]['Temperatura'].replace(',','.'))
    if t > last:
        temp.append(i+1)
    else:
        if len(temp) > len(ans): ans = temp.copy()
        temp = []
    last = t

if len(temp) > len(ans): ans = temp.copy()
print(ans[0], ans[-1])

#5.3
print()
from collections import defaultdict as dd
ans = dd(lambda:[0,0])

for i in file[:301]:
    ind = i['Kategoria_chmur'] + i['Wielkosc_chmur']
    ans[ind][0] += int(i['Opad'])
    ans[ind][1] += 1

ans = sorted(ans.items(), key=lambda x:x[0])
for i in ans:
    print(i[0], round(i[1][0] / i[1][1], 2))

#5.4 zadanie to jest skandaliczne, jesli takie trafi sie na maturze <=> kaplica
print()
ans = dd(lambda:0)
c = 0
rozm = 0
typ = '0'

ans[0] += 1
ansb = 1
ansc = 1

for i in range(1, len(file)):
    t = float(file[i]['Temperatura'].replace(',','.'))
    #wczoraj
    if not rozm:
        rozm = 1
        c += 1
        typ = ['S', 'C'][t>=10]
    elif rozm  < 5:
        if c == 3:
            rozm = min(5, rozm + 1)
            c= 0
        c+= 1
    elif rozm == 5:
        if int(file[i-1]['Opad']) >= 20:
            rozm = 0
            typ='0'
            c = 0
            #print(1, file[i]['Dzien'], end=' ')
    
    print(typ, rozm, i+1)
    ans[rozm] += 1

    ansb += i+1 <= 300 and rozm == int(file[i]['Wielkosc_chmur'])
    ansc += i+1 <= 300 and typ == file[i]['Kategoria_chmur']

print()
ans = sorted(ans.items(), key=lambda x:x[0])
for i in ans: print(*i)
print(ansb)
print(ansc)





