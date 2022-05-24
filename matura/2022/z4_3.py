file = open('Dane_2205/liczby.txt', 'r').read().split()
file = [int(i) for i in file]
file.sort()

vis = []
ans3 = 0
ans5 =0 

def dfs(ind):
    global mp, vis

    if not len(mp[ind]): return [[1], [ind]]

    if ind in vis: return [[0], [None]]
    vis.append(ind)

    reses =[]
    anses =[ind]

    #print(ind, 1)
    for i in mp[ind]:
        #print(i)
        #print(i, 2)
        a = int(i not in vis)
        curr = dfs(i)
        for j in curr[0]:
            reses.append(j + a)
        for j in curr[1]:
            anses.append(j)

    return [reses, anses]

def fact(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

def newt(n, k):
    if n==k: return 1
    elif n<k: return 0
    return fact(n) / ( fact(k) * fact(n-k) )

mp = dict()

for i in range(len(file)):
    a = file[i]
    mp[a] = []

    for j in range(i+1, len(file)):

        if not (file[j]%file[i]):

            mp[a].append(file[j])
            #print(file[i], file[j])

detailed = []
for i in mp.keys():
    a = dfs(i)
    #print(i, a)
    ans3 += newt(a[0][0], 3)
    ans5 += newt(a[0][0], 5)
    b = a[1][:a[0][0]]
    for j in range(len(b)):
        for k in range(j+1, len(b)):
            for p in range(k+1, len(b)):
                detailed.append([b[j],b[k],b[p]])
        

print(int(ans3), ans5)
for i in detailed:
    print(i)

