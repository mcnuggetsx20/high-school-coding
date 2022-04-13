file1 = open('plik1.txt', 'r').read().split('\n')[1:-1]
file2 = open('plik2.txt', 'r').read().split('\n')[1:-1]

srt = dict()
for i in file1:
    a = i.split('\t')
    srt.update({float(a[0]) : float(a[1])})

ans = [i for i in sorted(srt.items(),reverse=True, key=lambda x: x[1])][0:5]
notes = dict()

for i in ans:
    notes.update({i[0] : [10000000000, '']})
for i in ans:
    for j in file2:
        a = j.split('\t')
        for k in range(1, len(a)-2):
            if abs(i[0] - float(a[k])) < float(notes[i[0]][0]):
                notes[i[0]][0] = abs(i[0] - float(a[k]))
                notes[i[0]][1] = a[0]
for i in notes.keys():
    print(notes[i][1])
