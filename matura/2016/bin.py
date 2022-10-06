l = 0
r = 50

while l < r - 0.01:
    wat = 1000
    sub = 4000
    per = 0.8
    tot = 0
    mn = 100000

    test = (l + r) / 2
    test = round(test, 2)

    for i in range(1, 1501):
        sub -= int(not i%2) *test * per
        wat -= int(not i%2) *test * (1-per)
        mn = min(mn, per + i%2 * 10000000)
        if i%50 ==1 and i>50:
            tot += 5000-sub-wat
            wat += 5000-sub-wat
            per = sub/(sub+wat)

    if mn <= 0.01:
        r = test
    elif mn > 0.01:
        l = test

print(test)





