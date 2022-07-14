from utils import *

druzyny = Table('dane/druzyny.txt')
sedziowie = Table('dane/sedziowie.txt')
wyniki = Table('dane/wyniki.txt')

ans = 0
tab = []

for i in wyniki:
    if i.Rodzaj_meczu == 'P':
        tab.append(i.Nr_licencji)
for i in sedziowie:
    ans += int(i.Nr_licencji not in tab)
print(ans)

