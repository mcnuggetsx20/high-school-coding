import datetime


grass=10000
temp = 10000
test = 30
stop=False

while not stop:
    day = datetime.datetime(2022, 4, 1)
    grass=10000
    while str(day)!='2022-10-31 00:00:00':
        grass -= 15 * test
        if str(day)=='2022-04-12 00:00:00' and grass <= 0:
            print(test)
            stop=True
            break
        grass+=600
        grass -= (3*grass)//100
        day+=datetime.timedelta(days=1)
        temp=grass
    test+=1




