from utils import *

statek = Table("Dane_PR2/statek.txt")

mp = dict()

for i in statek:
    mp[i.towar]=0

for i in statek:
    mp[i.towar] += int(i.__dict__['ile ton']) * int(i.__dict__['Z/W'] == 'Z')

for i in sorted(mp.items(), key = lambda x:x[1], reverse=True):
    print(i)
