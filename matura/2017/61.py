file = open('dane/dane.txt', 'r').read().split()
file = [int(i) for i in file]
print(max(file))
print(min(file))
