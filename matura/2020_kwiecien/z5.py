file = open('dane/pogoda.txt', 'r').read().split('\n')[1:-1]
file = [i.split() for i in file]
from datetime import datetime, timedelta
from math import ceil

data = datetime.strptime('31.03.2015','%d.%m.%Y')
zbiornik = 25000
ans1a = 0
ans1b = 0
ans1c = 0
ok = True
ans2 = []
for i in file:
    op = float(i[1].replace(',', '.')); T = int(i[0]); data += timedelta(1)
    ans1a += T <= 15; ans1b += T>15 and op<=0.61; ans1c += T>15 and op > 0.61

    zbiornik = min(25000, zbiornik + 700*op)
    if op == 0: ubytek = ceil(0.03*(10**-2) * (T**1.5) * zbiornik); zbiornik = max(0, zbiornik -ubytek)
    print(data, zbiornik, op, T)

    if T <= 15 or op > 0.61: continue

    if zbiornik < (12000 * (1+T>30)): 
        wodo = abs(zbiornik - 25000); zbiornik = 25000; 
        if ok: ans2 = [data,wodo]; ok = False

    zbiornik -= 12000 * (1 + T>30)
print(ans1a,ans1b, ans1c)
print(*ans2)







