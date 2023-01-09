from collections import defaultdict as dd
from datetime import datetime, timedelta
#5.2

mp = {'zima' : 0.2,
      'wiosna' : 0.5,
      'lato' : 0.9,
      'jesien' : 0.4}
p = 0

koszt = 8000
season = 'zima'

n = 10
ans = dd(lambda: 0)
ans[1] = -8000

data = datetime.strptime('31.12.2022', '%d.%m.%Y' )
end = datetime.strptime('01.01.2024', '%d.%m.%Y')

while data != end:
    data += timedelta(1)
    if data == end: break

    day = data.day
    month = data.month

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
        koszt += n * 15
        ans[month] -= n * 15
        continue

    p += int(n * mp[season]) * 30
    ans[month] += int(n* mp[season]) * 30

for i in sorted(ans.items(), key = lambda x:x[0]):
    print(*i)
