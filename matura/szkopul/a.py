from math import gcd
def check(arr):
    ans, temp = 1, 1

    for k, i in enumerate(arr[:-1]):
        if gcd(i) == gcd(arr[k+1]):
            temp += 1
        else:
            ans = max(ans, temp)
            temp = 1
    ans = max(ans, temp)
    return ans

tab = [3,7,4,6,10,2,5]
print(check(tab))


