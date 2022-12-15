n, m = map(int, input().split())

def loncon(arr):
    ans, temp = 1, 1
    a = ['E', 'W']

    if 'E' not in arr and 'W' not in arr:
        return 0

    for k,i in enumerate(arr[:-1]):
        if i in a and arr[k+1] in a:
            temp += 1
        else:
            ans = max(ans, temp)
            temp = 1
    ans = max(ans, temp)
    return ans

from collections import defaultdict
mp = defaultdict(lambda: 0)

for j in range(m):
    a = input()
    mp[j] = loncon(a)

ans = sorted(mp.items(), key = lambda x: x[1], reverse=True)
for i in ans:
    if i[1] == ans[0][1]:
        print(i[0] + 1, end = ' ')
print()
print(ans[0][1])

