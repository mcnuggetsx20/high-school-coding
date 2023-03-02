file = open('Dane_PR2/dzialki.txt', 'r').read().split('\n\n')
tab = []

for i in file:
    tab.append(i.split())

c=0
for i in tab:
    t = 0
    for j in i:
        for k in j:
            t += int(k=='*')
    c += int(t/900 >= 0.7)
print(c)

