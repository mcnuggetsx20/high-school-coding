def main():
    n = int(input())
    if n < 40:
        print('to kaczka dziennikarska')
        return

    ans = ''
    for i in range(1, n+1):
        a= input()
        try:
            ans += a[9] * (not i%40)
        except:
            continue
    print(ans)

main()
