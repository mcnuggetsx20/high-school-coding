import datetime

day = datetime.datetime(2022, 4, 1)

grass=10000
temp = 0

while str(day)!='2022-10-31 00:00:00':
    if str(day)=='2022-04-10 00:00:00':
        temp -=grass
    grass -= 15 * 30
    grass+=600
    if str(day)=='2022-04-09 00:00:00':
        temp = grass
    grass -= (3*grass)//100
    day+=datetime.timedelta(days=1)
print(temp)



