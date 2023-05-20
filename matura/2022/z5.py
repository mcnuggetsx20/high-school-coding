file = open('dane/soki.txt').read().split('\n')[:-1]
file = [ dict(zip(file[0].split('\t'), i.split('\t'))) for i in file[1:]]

#5.1
from collections import defaultdict as dd
ans = dd(lambda: 0)
for i in file: ans[ i['magazyn']] += 1
for i in sorted(ans): print(i, ans[i])
print()

#5.2
from datetime import datetime
mp = dd(lambda: [])
for i in file: mp[i['data']].append(i)
ans = []
temp = []
for i in mp:
    ok = False
    for j in mp[i]:
        if j['magazyn'] == 'Ogrodzieniec': ok = True; break
        else: continue
    if ok: temp.append(i)
    else: ans = max(ans, temp, key=lambda k: len(k)).copy(); temp =[]

ans = max(ans, temp, key=lambda k: len(k)).copy()
print(len(ans))
print(ans[0], '\t', ans[-1])
print()

#5.3
def solve(K):
    global mp
    N = 30000
    filia = []
    ans4b = 0
    for i in mp:
        data = datetime.strptime(i, '%d.%m.%Y')
        if data.weekday() in [5,6]: N += 5000
        else: N += K

        for j in mp[i]:
            q = int(j['wielkosc_zamowienia'])
            if q > N: filia.append((i, j['nr_zamowienia'])); ans4b += q
            else: N -= q
            #print(N, q, data.weekday())
    try: res = filia[0]
    except: res = None
    return res, len(filia), ans4b
print(solve(5000))
l = 12000
r = 20000
while r > l+1:
    m = (l+r)//2
    if solve(m)[0] == None: r = m
    else: l = m
print(r)






