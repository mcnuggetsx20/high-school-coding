import matplotlib.pyplot as plt

wat = 1000
sub = 4000
per = 0.8
tot = 0
time = [i for i in range(1,1501)]
w=[]
s=[]
for i in range(1, 1501):
    sub -= int(not i%2) *20 * per
    wat -= int(not i%2) *20 * (1-per)
    if i%50 ==1 and i>50:
        tot += 5000-sub-wat
        wat += 5000-sub-wat
        per = sub/(sub+wat)
    w.append(round(wat, 2))
    s.append(sub)
plt.plot(time, w)
plt.plot(time, s)
plt.xlabel('pogchmin')
plt.show()






