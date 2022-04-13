file = open('DANE/dane.txt', 'r').read().split()

a=['A', 'C', 'E']
c=0

for i in file:
    if i[-1] in a:
        c+=1
print(c)



