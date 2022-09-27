file = open('dane/dane.txt', 'r').read().split('\n')[:-1]
file = [i.split() for i in file]

st = set()
ans = 0
for i in range(320):
    st.clear()
    temp = 0
    for j in file:
        st.add(j[i])
        if len(st)>1:
            st.clear()
            st.add(j[i])
            ans = max(ans, temp)
            temp = 0
        temp+=1
    ans = max(ans, temp)
print(ans)


