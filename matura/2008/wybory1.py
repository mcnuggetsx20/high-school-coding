file = open('dane/dane.txt', 'r').read().split('\n')[:-1]

ans = dict()
ans = {chr(i): 0 for i in range(65, 71)}

def solve(line):
    global ans
    line = line.split()[:-1]
    for i in range(len(line)):
        ans[chr(i + 65)] += int(line[i])

for i in file:
    solve(i)

for i in ans:
    print(i, ans[i])



        
