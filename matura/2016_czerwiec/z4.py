sep = ';'
file = open('dane/ubezpieczenia.txt', 'r').read().split('\n')[:-1]
file = [ dict(zip(file[0].split(sep), i.split(sep))) for i in file[1:]]

from collections import defaultdict as dd
ans = dd(lambda:0)
for i in file:
    month= i['Data_urodz'].split('-')[1]
    ans[month] += 1
for i in sorted(ans.items(),key=lambda x:x[0]): print(*i)

#4.2
print()
ans = dd(lambda:0)
for i in file:
    if i['Imie'][-1] != 'a': continue
    m = i['Miejsce_zamieszkania']
    ans[m] += 1
for i in sorted(ans.items(),key=lambda x:x[0]): print(*i)

#4.3
print()
ans = dd(lambda:0)
tab = ['kobiety', 'mezczyzni']
for i in file:
    p = i['Imie'][-1] != 'a'
    kw = 25000 + p*5000
    age = 2016 - int(i['Data_urodz'].split('-')[0])

    if age <= 30: skl = 0.1
    elif age <= 45: skl = 0.15
    else: skl = 0.12
    skl *= 0.01

    p = tab[p]
    ans[p] += kw * skl + 49*(age>60)
for i in ans: print(i, round(ans[i],2))

#4.4
print()
ans = dd(lambda:0)
for i in file:
    age = 2016 - int(i['Data_urodz'].split('-')[0])

    age -= 20
    age //=10
    ans[age] += 1
for i in sorted(ans.items(),key=lambda x:x[0]): print(*i)


    






