eggs = 0
money = 0
chicken = 200
odp1 = []
odp2 = 0
real = 0
Real = False

for i in range(1, 181):
    gain = 0

    if not i%30:
        temp = int(0.2*chicken)
        money -= 18 * temp
        chicken += temp
        gain -= 18 * temp
    if chicken == 200 and i!=1 and len(odp1)== 0: odp1.append(str(i) + 'poludnie') 

    eggs += chicken * bool(i%7)
    money += chicken * bool(i%7) * 0.9
    gain += chicken * bool(i%7) * 0.9
    eggs -= eggs * bool(i%7)

    odp2 += 0.2 * 1.9 * chicken
    gain -= 0.2 * 1.9 * chicken

    chicken -= 2 * (i%2)
    if chicken == 200 and i!=1 and len(odp1)== 0: odp1.append(str(i) + ' wieczorem') 

    real += gain
    if not Real and real > 1500:
        Real = True
        odp3 = i

print(odp1)
print(odp2)
print(odp3)



