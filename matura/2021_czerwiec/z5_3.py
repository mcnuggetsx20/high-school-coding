def main(k):
    from collections import defaultdict as dd
    from datetime import datetime, timedelta
#5.3

    mp = {'zima' : 0.2,
          'wiosna' : 0.5,
          'lato' : 0.9,
          'jesien' : 0.4}
    p = 0

    koszt = 8000
    season = 'zima'

    n = 10

    data = datetime.strptime('31.12.2022', '%d.%m.%Y' )
    end = datetime.strptime('01.01.2025', '%d.%m.%Y')

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
            continue

        p += int(n * mp[season]) * k

    return p - koszt

tab = [False]*3
for i in range(100):
    v = main(i)
    if v >= 100000 and not tab[0]:
        print(i, v)
        tab[0] = True
    if v >= 125000 and not tab[1]:
        print(i, v)
        tab[1] = True
    if v >= 150000 and not tab[2]:
        print(i, v)
        tab[2] = True

