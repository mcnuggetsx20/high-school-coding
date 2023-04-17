file = open('dane/woda.txt').read().split('\n')[:-1]
keys = ['data', 'woda']
file = [dict(zip(keys, i.split('\t'))) for i in file]
from collections import defaultdict as dd

#5.1
ans = dd(lambda: 0)
for i in file:
    rok= i['data'].split('-')[0]
    woda = int(i['woda'])
    ans[rok] += woda
ans = max(ans, key=ans.get)
print('5.1\n', ans)

#5.2
from datetime import datetime
ans = []
temp = []
for i in file:
    woda = int(i['woda'])
    if woda >= 10000: temp.append(i)
    else:
        if len(temp) > len(ans): ans= temp.copy()
        temp=[]
print('\n5.2\n', ans[0]['data'], ans[-1]['data'])

#5.3
ans = dd(lambda: 0)
for i in file:
    rok= i['data'].split('-')[0]
    m= i['data'].split('-')[1]
    woda = int(i['woda'])

    if rok != '2008': continue
    ans[m] += woda
a = list(ans.keys()); a.sort()
print('\n5.3')
for i in a: print(i, '\t', ans[i])

#5.4 (o zgrozo symulacja)
W = 5 *(10**5)
from math import ceil
ansa=[]
ansb=0
ansc=0
WC = W

for i in file:
    data= i['data']

    #po polnocy
    pomiar = W
    pomiarc = WC
    nadmiar = max(0, pomiar-10**6)
    W -= nadmiar

    if nadmiar: ansa.append(data)
    ansb += (pomiar >= 800000)
    ansc = max(ansc,WC)


    #8:00
    W -= ceil(0.02*pomiar)
    WC -= ceil(0.02*pomiarc)

    #koniec dnia
    W += int(i['woda'])
    WC += int(i['woda'])
    #print(data, pomiar)

print('\n5.4')
print(ansa[0])
print(ansb)
print(ansc)






    




