n, m = map(int, input().split())

def loncon(arr):
    temp,ans = 1, 1
    for k, i in enumerate(arr[:-1]):
        if i == arr[k+1]:
            temp += 1
        else:
            ans =max(ans, temp)
            temp = 1
    ans =max(ans, temp)
    return ans

tab = list()

ans = 0
N = n
while n:
    tab.append( list(map(int,input().split())) )
    n-=1

for i in range(m):
    temp = []
    for j in range(N):
        temp.append(tab[j][i])
    ans = max(ans, loncon(temp))
print(ans)

