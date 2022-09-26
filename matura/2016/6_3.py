file = open('dane/dane_6_3.txt', 'r').read().split('\n')[:-1]

for i in file:
    a = i.split()
    st = set()
    for j in range(len(a[0])):
        diff = (ord(a[1][j]) - ord(a[0][j]) + 26)%26
        st.add(diff)
        if len(st) > 1:
            print(a[0])
            break

