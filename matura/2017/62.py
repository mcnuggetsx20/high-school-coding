file = open('dane/dane.txt', 'r').read().split('\n')[:-1]
file = [i.split() for i in file]

ans = 0
for i in file:
    ans += int(i != i[::-1])
print(ans)



            temp += int( abs(int(file[i+k][j])- int(file[i][j])) > 128 or abs(int(file[i][j+k]) - int(file[i][j])) > 128)

