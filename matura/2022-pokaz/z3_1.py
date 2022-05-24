def f_pow(a, x, m):
    ans = 1
    while x>0:
        if x%2:
            ans*=a
        a*=a
        x//=2

    return ans

print(f_pow(2, 5, 1))


