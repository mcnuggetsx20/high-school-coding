file = open('dane/pogoda.txt', 'r').read().split('\n')[1:-1]
file = [i.split() for i in file]
from datetime import datetime, timedelta
from math import ceil
from collections import defaultdict as dd

data = datetime.strptime('31.03.2015','%d.%m.%Y')
zbiornik = 25000
ans1a = 0
ans1b = 0
ans1c = 0
ok = True
ans2 = []
ans3 = dict()
ans4 = dd(lambda: 0)

mies = 'kwiecien maj czerwiec lipiec sierpien wrzesien'

for i in file:
    op = float(i[1].replace(',', '.')); T = int(i[0]); data += timedelta(1); month = data.month
    ans1a += T <= 15; ans1b += T>15 and op<=0.61; ans1c += T>15 and op > 0.61

    zbiornik = min(25000, zbiornik + 700*op)
    if op == 0: ubytek = ceil(0.03*0.01 * (T**1.5) * zbiornik); zbiornik = max(0, zbiornik -ubytek)

    if T <= 15 or op > 0.61: continue

    wodo = 0
    if zbiornik < 12000 * (1+ (T>30) ): 
        wodo = abs(zbiornik - 25000); zbiornik = 25000; 
        if ok: ans2 = [data,wodo]; ok = False

    ans4[month] += wodo

    zbiornik -= 12000 * (1 + (T>30) )

    ans3[datetime.strftime(data, '%d.%m.%Y')] = zbiornik
    
print(ans1a,ans1b, ans1c)
print(*ans2)
#print(ans3)

for i in ans4:
    print(mies.split(' ')[i-4], ceil(ans4[i]/1000) * 11.74)






