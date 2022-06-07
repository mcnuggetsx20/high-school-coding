import gen

users = gen.gen(100)
adj = [[] for i in range(100)]

users = sorted(users, key=lambda x:x.city)

for i in users:
    print(i.name, i.lastname, i.city)



