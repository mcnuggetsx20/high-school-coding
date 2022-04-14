file = open('Dane_PR/liczby.txt', 'r').read().split()
ans = 0
mx = 0 
_sum=0
c=0
for i in file:
    ans += int(i[-1]=='0')
    mx = max(mx, int(i, 2))
    _sum += int(i, 2) * int(len(i)==9)
    c+=int(len(i)==9)
print('a)\t', ans)
print('b)\t', mx, bin(mx).replace('0b', ''))
print('c)\t', c, bin(_sum).replace('0b',''))
