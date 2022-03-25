file = open('Dane_2203/szachy.txt', 'r').read().split('\n\n')[:-1]

for i in range(len(file)):
    file[i] = file[i].split()

white = 0
black = 0

def solve(tar):
    global white, black
    temp = ''.join(tar.split('.'))
    white += int(temp.count('Wk') + temp.count('kW') >= 1)
    black += int(temp.count('Kw') + temp.count('wK') >= 1)

for i in file:
    for j in range(8):
        temp = ''
        for k in i:
            temp += k[j]
        solve(temp)

    for j in i:
        solve(j)

print(white, black)


