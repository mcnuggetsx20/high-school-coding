import datetime

day = datetime.datetime(2022, 4, 1)

grass=10000
temp = 10000

while str(day)!='2022-10-31 00:00:00':
    grass -= 15 * 30
    grass+=600
    grass -= (3*grass)//100
    day+=datetime.timedelta(days=1)
    if grass > temp:
        print(day)



