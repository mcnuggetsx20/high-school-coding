#66.3
file = open('dane/66/trojki.txt', 'r').read().split('\n')[:-1]
file = [[int(i) for i in i.split()] for i in file]

def check(a, b):
    a = sorted(a)
    b = sorted(b)
    c1 = a[0] * a[0] + a[1] * a[1] == a[2] * a[2]
    c2 = b[0] * b[0] + b[1] * b[1] == b[2] * b[2]
    return c1 and c2

for i in range( len(file) -1 ):
    if check(file[i], file[i+1]):
        print(file[i])
        print(file[i+1], end = '\n\n')

    


