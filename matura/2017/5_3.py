from utils import *

druzyny = Table('dane/druzyny.txt')
sedziowie = Table('dane/sedziowie.txt')
wyniki = Table('dane/wyniki.txt')

ans = [0,0,0]

for i in wyniki:
    if i.Gdzie == 'W':
        score = int(i.Bramki_zdobyte) - int(i.Bramki_stracone)
        ind = int(score < 0) + 2 * int(score > 0)
        ans[ind] += 1
print('Wygrane:' , ans[2])
print('Przegrane:' , ans[1])
print('Zremisowane:' , ans[0])


