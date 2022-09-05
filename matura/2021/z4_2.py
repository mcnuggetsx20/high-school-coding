file = open('DANE_2105/instrukcje.txt', 'r').read().split('\n')[:-1]

temp = file[0].split()[0]
ans = 1
longest = 1
order = ''
for i in file[1:]:

    a = i.split()[0]
    if a == temp:
        ans += 1
    else:
        if ans > longest:
            longest = ans
            order = temp
        ans = 1
    temp = a

print(longest, order)

