from math import gcd
#n = int(input())

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





