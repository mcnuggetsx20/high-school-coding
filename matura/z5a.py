import datetime
data = datetime.datetime(2015, 9, 15)
tab = ['Sat', 'Sun']

wood = 550
pora=0
while data != datetime.datetime(2017, 1, 1):
    pora=0
    if wood < 100:
        print(pora, data)
        break
    if data.strftime('%a') == 'Fri' and wood <100:
        wood+=300

    elif data.strftime('%a') in tab and wood >= 26:
        wood-=26


    pora =1
    wood -= 26 * int(wood >=26)
    if wood < 100:
        print(pora, data)
        break
    data += datetime.timedelta(days=1)

