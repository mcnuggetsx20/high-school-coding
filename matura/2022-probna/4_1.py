file = open('dane/ekodom.txt', 'r').read().split('\n')
file = [i.split() for i in file]
file = [ dict(zip(file[0], i)) for i in file[1:]][:-1]



from datetime import datetime

woda = 5000
lower = datetime.strptime('01.04.2022', '%d.%m.%Y')
upper = datetime.strptime('30.09.2022', '%d.%m.%Y')

bo = 0
siec = False

ans1a = []
ans1b = 0
ans3a = 0
ans3b = 0
temp = []

from collections import defaultdict as dd
mp = dd(lambda: 0)

for i in file:
    woda += int(i['retencja'])
    woda -= 190

    data = datetime.strptime(i['Data'], '%d.%m.%Y')
    wd = data.weekday() + 1
    woda -= 70* (wd==3)

    mp[data.month] += int(i['retencja'])

    if (data - lower).days >= 0 >= (data - upper).days:
        if i['retencja'] == '0':
            bo += 1
            temp.append(i['Data'])
        else:
            bo = 0
            ans1a.append( (temp, len(temp)) )
            temp = []

        if bo%5 == 0 and bo:
            woda -= 300
            ans1b += 1
    ans3a += woda <= 0
    ans3b -= woda * (woda < 0)
    woda = max(0, woda)

ans1a = sorted(ans1a, key=lambda x:x[1])[-1]
print(ans1a[1], ans1a[0][0], ans1a[0][-1])
print(ans1b)
print()
for i in sorted(mp.items(), key = lambda x:x[0]):
    print(i[0], '\t', i[1])
print()
print(ans3a)
print(ans3b)





