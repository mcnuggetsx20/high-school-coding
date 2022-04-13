file = open('dane/dane5-3.txt', 'r').read().split()
tab = [0]
for i in file:
    tab.append(int(i))
pref = [0 for i in tab]
pref.append(0)
ans = 0

for i in range(1, len(tab)):
    pref[i] = max(tab[i], tab[i]+pref[i-1])
    ans = max(ans, pref[i])
print(ans)
