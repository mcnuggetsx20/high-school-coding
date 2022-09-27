file = open("dane/dane.txt", 'r').read().split('\n')[:-1]
file = [list(map(int, i.split())) for i in file]
ans = 0

tab = [False for i in range(320)]
tab = [tab for i in file]

for x in range(len(file)):
    for y in range (len(file[x])):
        temp = 0
        try:
            print(x, y)
            temp += abs(file[x][y] - file[x][y+1]) > 128
        except:
            pass
        try:
            temp += abs(file[x][y] - file[x + 1][y]) > 128
        except:
            pass
        temp += temp > 0
        ans += temp

print(ans)
