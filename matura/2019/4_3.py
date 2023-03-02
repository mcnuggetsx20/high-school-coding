file = open('Dane_PR2/dzialki.txt', 'r').read()[:-1].split('\n\n')

mp = dict()

c = 1
for i in file:
    curr = i.split('\n')
    for j in range(30):
        temp = ''
        for k in range(j+1):
            temp += curr[k][:j+1]
        if not temp.count('X'):

            if j+1 not in mp.keys(): mp[j+1] = []
            mp[j+1].append(c)
    c += 1

ind = max(list( mp.keys() ))
print(ind, mp[ind])

