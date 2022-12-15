n = int(input())

tab = []
for i in range(n):
    a = int(input().strip(), 2)
    tab.append((a, i+1))
tab.sort()

print(tab[0][1], tab[-1][1])
