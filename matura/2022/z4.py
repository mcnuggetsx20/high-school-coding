file = open('dane/liczby.txt').read().split()
test = open('dane/przyklad.txt').read().split()
file = list(map(int, file))

#4.1
ans = []
for i in file:
    i = str(i)
    if i[0] == i[-1]: ans.append(i)
print(len(ans), ans[0])

#4.2
def fact(n):
    tab = []; k = 2
    while n!=1:
        while n%k ==0: n//=k; tab.append(k)
        k += 1
    return tab

from collections import defaultdict as dd
ans1= dd(lambda: 0)
ans2= dd(lambda: 0)
for i in file:
    temp = fact(i)
    ans1[i] = len(temp); ans2[i] = len(set(temp))

print(max(ans1.items(), key=lambda x:x[1]))
print(max(ans2.items(), key=lambda x:x[1]))

#4.3
print()
def sil(n):
    ans =1
    for i in range(2, n+1): ans *= i
    return ans

file = list(set(file))
file.sort()
t,p = [],[]

for i in range(len(file)):
    for j in range(i+1, len(file)):
        if file[j]%file[i]: continue

        for k in range(j+1, len(file)):
            if file[k]%file[j]: continue
            t.append((file[i], file[j], file[k]))

            for l in range(k+1, len(file)):
                if file[l]%file[k]: continue


                for m in range(l+1, len(file)):
                    if file[m]%file[l]: continue
                    p.append((file[i], file[j], file[k], file[l], file[m]))
print(len(t), len(p))
for i in t: print(i)
#nagradzanie jebanej sraki kurwa








