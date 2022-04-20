def f(a, x, m):
    ans =1 
    while x>0:
        ans = max(ans, ans * a * (x%2))
        ans %=m
        a*=a
        x//=2
    return ans

print(f(2,5,1))

