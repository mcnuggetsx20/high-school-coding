from utils import *

statek = Table("Dane_PR2/statek.txt")

prev = statek[0].data

a = statek[0].__dict__['Z/W'] == 'W'
b = int(statek[0].__dict__['cena za tone w talarach'])
c = int(statek[0].__dict__['ile ton'])

tal = 5 * 10**5 + b*c * (int(a) - int(not a))
des = '2018-12-18'

odp1 = 0

for i in statek[1:]:
    now = i.data

    if prev == des and now != des:
        odp1 = tal
        break

    a = i.__dict__['Z/W'] == 'W'
    b = int(i.__dict__['cena za tone w talarach'])
    c = int(i.__dict__['ile ton'])
    tal += b*c * (int(a) - int(not a))
    prev = now

if(prev == des):
    odp1=tal

ans = tal
mxd = ''

a = statek[0].__dict__['Z/W'] == 'W'
b = int(statek[0].__dict__['cena za tone w talarach'])
c = int(statek[0].__dict__['ile ton'])
tal = 5 * 10**5 + b*c * (int(a) - int(not a))
prev = statek[0].data

for i in statek[1:]:
    now = i.data
    if(prev != now):
        if ans < tal:
            ans = tal
            mxd = prev

    a = i.__dict__['Z/W'] == 'W'
    b = int(i.__dict__['cena za tone w talarach'])
    c = int(i.__dict__['ile ton'])
    tal += b*c * (int(a) - int(not a))
    prev = now

if ans < tal:
    ans = tal
    mxd = prev
odp2 = ans

#############################
ans = 0
tal = 0

for i in statek:
    now = i.data
    #if now != prev:
    #    mx = max(ans, mx)

    a = i.__dict__['Z/W'] == 'W'
    b = int(i.__dict__['cena za tone w talarach'])
    c = int(i.__dict__['ile ton'])
    tal += b*c * (int(a) - int(not a))
    if tal < 0:
        ans += -tal
        tal =0

odp3 = ans

print("Stan kasy z dnia 18.12.2018: ", odp1)
print("Maksymalny stan kasy: ", odp2)
print("Dzien maksymalnego stanu kasy: ", mxd)
print("Minimum talarów: ", odp3)




