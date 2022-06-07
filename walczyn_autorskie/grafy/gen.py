import user
from names import *
from cities import *
from random import randint

def gen(quan=0):
    def a(ind):
        a = randint(1,2)
        _user = user.user()
        if a==1:
            _user.name= names_f[randint(0, len(names_f)-1)]
            _user.lastname = lastnames_f[randint(0, len(lastnames_f)-1)]
        else:
            _user.name= names_m[randint(0, len(names_m)-1)]
            _user.lastname = lastnames_m[randint(0, len(lastnames_m)-1)]

        _user.city = cities[randint(0, len(cities)-1)]
        _user.index = ind
        return _user
    ret = []
    for i in range(quan):
        ret.append(a(i))
    return ret





