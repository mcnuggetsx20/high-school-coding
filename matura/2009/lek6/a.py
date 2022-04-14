lek = open('Dane/lekarze.txt', 'r').read().split('\n')[1:-1]
wiz = open('Dane/wizyty.txt', 'r').read().split('\n')[1:-1]

ans = dict()
ans2 = dict()
for i in range(0, 73):
    ans.update({i : 0})

for i in wiz:
    a = i.split('\t')
    ans[int(a[0])]+=1

for i in lek:
    a = i.split('\t')
    ans2.update({a[1] + ' ' +  a[2] : ans[int(a[0])]})

for i in sorted(ans2.items(), reverse=True, key=lambda x: x[1]):
    print(i)
