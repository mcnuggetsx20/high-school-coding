file = open('dane/dane.txt', 'r').read().split('\n')[:-1]
file = [[i.split()[0]] + i.split() + [i.split()[-1]] for i in file]
file = [file[0]] + file + [file[-1]]

ans = 0
tab = [-1, 1]
for i in range(1, len(file) - 1):
    for j in range(1, len(file[i]) -1):
        temp = 0
        for k in tab:
            temp += int( abs(int(file[i+k][j])- int(file[i][j])) > 128 or abs(int(file[i][j+k]) - int(file[i][j])) > 128)
        ans += int(temp > 0)

print(ans)

