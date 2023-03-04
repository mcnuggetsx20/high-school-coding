drewno = 550
delta = 300
c = 0
brak = 0

from datetime import datetime, timedelta
start = datetime.strptime('15.09.2015', '%d.%m.%Y')
end = datetime.strptime('1.04.2016', '%d.%m.%Y')

first = False
ans1 = ''
ans2a = 0
ans2b = [0,0] #drewno, gaz
ans3 = []

while start != end:
    day= start.weekday()
    if day in [5, 6]:
        if drewno >= 26: drewno -= 26
        else: c += abs(drewno - 26)

        if drewno < 100 and not first: first = True; ans1 = 'rano ' + datetime.strftime(start, '%d.%m.%Y')

    if day == 4 and drewno < 100: drewno += delta; ans2a += 1; brak = max(brak, c); c= 0

    if drewno >= 26: drewno -= 26; ans2b[0] += 1;
    else: ans2b[1] += 1; c+= abs(drewno-26)

    ans3.append(drewno)

    if drewno < 100 and not first: first = True; ans1 = 'wieczorem ' + datetime.strftime(start, '%d.%m.%Y')

    start += timedelta(1)

print(ans1)
print(ans2a, ans2b)
print(ans3)
print(300 + brak) #to jest zle z jakiegos powodu
