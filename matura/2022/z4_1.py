file = open('Dane_2205/liczby.txt', 'r').read().split()
ans = 0
for i in reversed(file):
    if i[0]==i[-1]:
        ans += 1
        mn = i
print(ans, mn)
