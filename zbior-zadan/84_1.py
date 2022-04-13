file = open('dane/84/lpg.txt', 'r').read().split('\n')

day = 3
pb95=45
lpg=30

pb_refuel=0
lpg_refuel=0

for i in range(0,len(file)):
    temp = file[i].split()
    file[i]=temp

for i in range(1,len(file)):
    day%=7
    if lpg > 15:
        lpg-=(9*int(file[i][1]))/100
    else:
        lpg-=(9*int(file[i][1]))/200
        pb95-=(6*int(file[i][1]))/200

    lpg=round(lpg, 2)
    pb95=round(pb95, 2)

    if day==4:
        if pb95 < 40:
            pb_refuel+=1
            pb95=45
    if lpg < 5:
        lpg_refuel+=1
        lpg=30
    day+=1
print(lpg_refuel, pb_refuel)


