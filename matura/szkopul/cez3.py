n = int(input())

tab = [chr(i) for i in range(65, 91)] * 2

while n:
    a, b = input().split()
    check = set()
    for i, j in zip(a, b):
        ind2 = ord(j) - 65
        for k in range(ind2, len(tab)):
            if tab[k] == i:
                check.add(k - ind2)
                break

    if len(check) > 1:
        print(a)
    n-=1

