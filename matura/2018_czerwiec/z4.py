def parse(name):
    tab = open(f'dane/{name}.txt', 'r').read().split('\n')[:-1]
    tab = [ list(map(int, i.split())) for i in tab]
    globals()[name] = tab

parse('dane1')
parse('dane2')

#4.1
ans = 0
for i,v in enumerate(dane1):
    ans += dane1[i][-1] == dane2[i][-1]
print(ans)

#4.2
print()

ans = 0
for i,v in enumerate(dane1):
    v = [i%2 for i in v]
    k = [i%2 for i in dane2[i]]
    ans += v.count(1) == k.count(1) == v.count(0) == k.count(0) == 5

print(ans)

#4.3
print()

c = 0
ans = []
for i,v in enumerate(dane1):
    v = set(v)
    k = set(dane2[i])

    if v == k:
        ans.append(i+1)
        c += 1
print(c, 'pary ciągów\nnumery wierszy:')
print(*ans)

#4.4
print()
for i,v in enumerate(dane1):
    k = dane2[i]

    v += k
    v.sort()
    print(*v)






