wat = 1000
sub = 4000
per = 0.8
for i in range(1, 192):
    sub -= int(not i%2) *20 * per
    wat -= int(not i%2) *20 * (1-per)
    if i%50 ==1 and i>50:
        wat += 5000-sub-wat
        per = sub/(sub+wat)
    print(i, sub+wat, per, sub, wat)






