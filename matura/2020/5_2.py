import datetime
from utils import *

statek = Table("Dane_PR2/statek.txt")

ans = 0
prev = datetime.datetime.strptime(statek[0].data, '%Y-%m-%d')

for i in statek[1:]:
    now = datetime.datetime.strptime(i.data, '%Y-%m-%d')
    ans += int( now - prev > datetime.timedelta(21) )
    prev = now

print(ans)



