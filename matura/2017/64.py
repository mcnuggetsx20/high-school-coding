file = open('dane/dane.txt', 'r').read().split('\n')[:-1]
file = [i.split() for i in file]

ans = 0
for i in range(320):
    st = set()
    temp = 0
    for j in file:
        st.add(j[i])
        if len(st) > 1:
            break
        temp += 1
    ans = max(ans, temp)

print(ans)


