from utils import *

druzyny = Table('dane/druzyny.txt')
sedziowie = Table('dane/sedziowie.txt')
wyniki = Table('dane/wyniki.txt')

mp = dict()

for i in druzyny:
    mp[i.Id_druzyny] = 0

for i in wyniki:
    mp[i.Id_druzyny] += int(i.Bramki_zdobyte) - int(i.Bramki_stracone)

for i in mp:
    if not mp[i]:
        print(druzyny.find([i])[0].Nazwa)

