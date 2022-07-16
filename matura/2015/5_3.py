from utils import *

mandaty = Table('dane/mandaty.txt')
wykroczenia = Table('dane/wykroczenia.txt')
kierowcy = Table('dane/kierowcy.txt')

ans = []
for i in wykroczenia:
    name = i.nazwa.lower()
    if 'naruszenie zakazu' in name:
        ans.append(i.nazwa)

ans.sort()
for i in ans:
    print(i)

