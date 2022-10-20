file = open('dane/dane.txt', 'r').read().split('\n')[:-1]

ans = dict()
ans = {chr(i): 0 for i in range(65, 71)}
curr = {chr(i): 0 for i in range(65, 71)}

def f(v, s):
    return v/(s+1)

def solve(line):
    global ans, q, curr
    line = line.split()[:-1]
    for i in range(q):
        for j in range(len(line)):
            curr[chr(j + 65)] = f(int(line[j]), ans[chr(j+65)])
        mx = max(curr, key=curr.get)
        ans[mx] += 1
        curr = {chr(i): 0 for i in range(65, 71)}

q = int(file[5].split()[-1])

solve(file[5])

for i in ans:
    print(i, ans[i])



        

