file = open('Dane_2205/liczby.txt', 'r').read().split()
file = [int(i) for i in file]
file.sort()


def fact(n):
    ans = 1
    for i in range(n):
        ans *= i
    return ans

def newt(n, k):
    res = fact(n) / ( fact(k) * fact(n-k) )
    return res

for i in range(len(file)):
    a = file[i]
    temp = []
    for j in range(i+1, len(file)):
        if not (file[j]%file[i]):
            print(file[i], file[j])
            temp.append(file[j])
    c = 0
    last =a 
    for j in temp:
        if j % last:
            continue
        c+=1
ans5 =0
ans3 =0












