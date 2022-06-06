import datetime
file = open('Dane_2205/soki.txt', 'r').read().split('\n')[:-1]

temp = file[0].split('\t')
file = file[1:]
for i, j in enumerate(file):
    a = file[i].split('\t')
    file[i]= dict(zip(temp, a))

def solve(inc):
    bottles = 30000
    prev = datetime.datetime.strptime(file[0]['data'], '%d.%m.%Y')
    watch = True
    zam = 0
    but = 0

    for i in file:
        data = datetime.datetime.strptime(i['data'], '%d.%m.%Y')
        tyg = data.weekday() + 1
        delta = datetime.timedelta(1)
        if data - prev == delta:
            bottles += inc * int(tyg in range(1, 6))
            bottles += 5000 * int(tyg in range(6, 8))

        wlk = int(i['wielkosc_zamowienia'])
        if bottles < wlk:
            return False
            if watch:
                print('Pierwsze zamówienie: ', data, i['nr_zamowienia'])
                watch =False
            zam += 1
            but += wlk
        bottles -= wlk * int(wlk <= bottles)
        prev= data
    return True
for i in range(12000, 1000000000000000000):
    if solve(i):
        print(i)
        break




