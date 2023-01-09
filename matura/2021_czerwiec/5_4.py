from collections import defaultdict as dd
from datetime import datetime, timedelta
k = 8000
p = 0

data = datetime.strptime('31.12.2022', '%d.%m.%Y' )
end = datetime.strptime('01.01.2025', '%d.%m.%Y')

season = 'zima'
n = 10

ok = False

mp = {'zima' : 0.2,
      'wiosna' : 0.5,
      'lato' : 0.9,
      'jesien' : 0.4}

#5.1
while data != end:
    data += timedelta(1)
    if data == end: break

    day = data.day
    month = data.month

    if day == 1 and (p-k) >= 3 *800:
        n+=3
        k += 3*800

    if day == 21 and month == 12:
        season = 'zima'

    elif day == 21 and month == 3:
        season = 'wiosna'

    elif day == 21 and month  == 6:
        season = 'lato'

    elif day == 23 and month == 9:
        season = 'jesien'

    if data.weekday() == 5: continue

    if data.weekday() == 6:
        k += n * 15
        continue

    p += int(n * mp[season]) * 30

print(p, k)



    

