file = open('Dane_PR2/pary.txt', 'r').read().split()

era = [True for i in range(111)]
for i in range(2, 111):
    for j in range(2, 111//i):
        era[i*j] = False;

def solve(query):
    global era, file
    for i in range(2, len(era)):
        for j in range(2, len(era)):
            if era[i] and era[j] and i + j == int(query):
                print(query, i, j)
                return

for q in range(0, len(file), 2):
    ok = False
    if not int(file[q])%2:
        solve(file[q])





