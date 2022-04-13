def f(x):
    return x

def integral(a, b, n=1000):
    area = 0
    width = (b-a)/n
    x = a
    while x < b:
        area += f(x)*width
        x+=width
    return area

print(integral(0, 100))
