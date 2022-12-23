s= 25
A = [7,6,5,4,3,2,1]
B = [0] * (s+1)
n = len(A)

def tura(k):
    global n, s, A, B
    for i in range(s, A[k]-1, -1):
        print(i, A[k])
        if B[i-A[k]] and not B[i]:
            B[i] = 1
        print(B)


def main(dana):
    global n, s, A, B
    s= dana[1]
    A = dana[0]
    B = [0] * (s+1)
    n = len(A)
    B[0] =1 

    print(B)
    for k in range(1, n+1):
        tura(k-1)

    #print(B)
    return (['NIE', 'TAK'][B[-1]])


def solve()
    d = [1, 2, 3]
    ans = set()
    for s in range(1,201):
        t = (d, s)
        v = main(t)
        ans.add(v)
    return ans[0] == 'TAK' and len(ans)==1


