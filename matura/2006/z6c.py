file = open('DANE/dane.txt', 'r').read().split()

c=0

for i in file:
    if i == i[::-1]:
        c+=1
print(c)




