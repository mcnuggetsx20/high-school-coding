file = open('dane/84/lpg.txt', 'r').read().split('\n')

day = 3
pb95=45
lpg=30

for i in range(0,len(file)):
    temp = file[i].split()
    file[i]=temp

for i in range(1,len(file)):
    day%=7
    #print(pb95, lpg, day)

    if lpg < 5.25:
        print(file[i][0])

    if lpg > 15:
        lpg-=round((9*int(file[i][1]))/100, 2)
    else:
        lpg-=round((9*int(file[i][1]))/200, 2)
        pb95-=round((6*int(file[i][1]))/200, 2)

    lpg=round(lpg, 2)
    pb95=round(pb95, 2)



    if day==4:
        if pb95 < 40:
            pb95=45
    if lpg < 5:
        lpg=30

    day+=1

