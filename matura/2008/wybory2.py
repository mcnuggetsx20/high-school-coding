file = open('dane/dane.txt', 'r').read().split('\n')[:-1]


ans = dict()
ans = {i: 0 for i in range(1, 21)}
c = 1

def solve(line):
    global ans, c
    line = line.split()[:-1]
    for i in range(len(line)):
        ans[c] += int(line[i])

for i in file:
    solve(i)
    c+=1

print('max:', max(ans, key = ans.get))
print('min:', min(ans, key = ans.get))


        
