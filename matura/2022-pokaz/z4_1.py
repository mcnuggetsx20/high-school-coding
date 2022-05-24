file = open('Dane_2203/brenna.txt', 'r').read().split('\n')[1:-1]

for i in range(len(file)):
    file[i] = file[i].split()
    file[i][2] = float(file[i][2].replace(',', '.'))
    file[i][3] = float(file[i][3].replace(',', '.'))
file.append(['','','',''])

mx = 0
mn = 100000000

mp = dict()

for i in range(len(file)-1):
    if file[i][0] == file[i+1][0]:
        mx = max(file[i][2], mx)
        mn = min(file[i][2], mn)
    else:
        mp[abs(mx - mn)] = file[i][0] 
        mx = 0
        mn = 10000000

print(max(mp.keys()), mp[max(mp.keys())])


