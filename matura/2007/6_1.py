with open('Dane/telefony.txt') as f:
    file = ''.join(f.readlines()).split('\n')[:-1]

tar = '504669045'

ans = 0
for i in file:
    ans += int( i == tar)

print(ans)


