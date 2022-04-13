wat = 1000
sub = 4000
per = 0.8
tot = 0
test = 28.04
for i in range(1, 1501):
    sub -= int(not i%2) *test * per
    wat -= int(not i%2) *test * (1-per)
    if i%50 ==1 and i>50:
        tot += 5000-sub-wat
        wat += 5000-sub-wat
        per = sub/(sub+wat)
    if i==1500:
        print(i, per*100, round(tot,4))








