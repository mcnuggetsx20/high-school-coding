from datetime import datetime, timedelta
from math import ceil
file = open('dane/pogoda.txt','r').read().split('\n')[1:-1]
file = [ i.split('\t') for i in file]

data = datetime.strptime('31.03.2015', '%d.%m.%Y')
mx = 25000
zbiornik = mx
prev = mx
z1 = True

ans = dict(zip( [i for i in range(4, 10)], [0]*6))

a4 = 0
b4 = 0
c4 = 0

for i in file:
    data += timedelta(days=1)
    T = int(i[0])
    opady = float(i[1].replace(',', '.'))

    #print(zbiornik)

    zbiornik = min(mx, zbiornik + (700*opady))
    if not opady: zbiornik = max(0, zbiornik - ceil(0.0003 * (T**1.5) * prev))

    a4 += T <=15
    c4 += T>15 and opady > 0.6

    if T > 15 and opady <= 0.6:
        b4 += 1
        w = 12000
        if T > 30: w*=2

        if zbiornik -w < 0:
            if z1: z1=False; print(data, mx-zbiornik) 
            m = data.month
            ans[m] += (mx-zbiornik)
            zbiornik = mx

        zbiornik = max(0, zbiornik - w)

    prev = zbiornik

print()
for i in ans:
    print(i, ceil(ans[i]/1000) * 11.74)

print()
print(a4, b4, c4)


