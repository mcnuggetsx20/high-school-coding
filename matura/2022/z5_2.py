import datetime
file = open('Dane_2205/soki.txt', 'r').read().split('\n')[:-1]

temp = file[0].split('\t')
file = file[1:]
for i, j in enumerate(file):
    a = file[i].split('\t')
    file[i]= dict(zip(temp, a))

tab = []
watch = False
c = 0
ans = 0
prev = ''
_first = ''
first= ''
last = ''
for i in file:
    if i['magazyn'] =='Ogrodzieniec': tab.append(datetime.datetime.strptime(i['data'], '%d.%m.%Y'))

prev = tab[0]
for i in tab:
    print(i)
for i in tab[1:]:
    cond = i - prev == datetime.timedelta(1)
    if cond:
        c+= 1
        if not watch:
            c+=1
            watch = True
            _first = prev
    else:
        watch = False
        if ans < c:
            ans = c
            first = _first
            last = prev
        c= 0
    prev = i
print(ans, first, last)

