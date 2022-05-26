file = open('Dane_2205/soki.txt', 'r').read().split('\n')[:-1]

temp = file[0].split('\t')
file = file[1:]
for i, j in enumerate(file):
    a = file[i].split('\t')
    file[i]= dict(zip(temp, a))

ans = dict()
for i in file:
    curr = i['magazyn']
    if curr not in ans:
        ans[curr] = 0
    ans[curr] += 1

for i in ans:
    print(i, ans[i])
