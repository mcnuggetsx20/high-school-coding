n = int(input())

def ok(word):
    word = [ord(i) for i in word]
    return max(word) - min(word) <= 10

ans = []
while n:
    a = input()
    if ok(a):
        ans.append(a)
    n-=1
print(*ans, sep='\n')

