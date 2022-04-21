from exif import Image
from math import sin, cos, acos, radians, sqrt

def l(a, b, p):
    a = radians(a)
    b = radians(b)
    p = radians(p)
    return acos(cos(a*p) * cos(b*p) + sin(a*p) * sin(b*p) * cos(p)) * 111.1
    

def link_gen(lat, lon):
    link = 'https://www.google.pl/maps/place/' + lat + ',' + lon
    return link

def func(img, pin, radius):
    img = Image(img)

    lat = img.get("gps_latitude")
    lon = img.get("gps_longitude")

    lat = lat[0] + lat[1]/60 +lat[2]/3600
    lon = lon[0] + lon[1]/60 +lon[2]/3600


    x = l(pin[0], lat, 90)
    y = l(pin[1], lon, 90)

    dst = sqrt(x**2 + y**2)
    if dst <= radius:
        return link_gen(str(lat), str(lon))
    else:
        return None

wro = (51.110048, 17.060480)
print(func('alo.jpg', wro, 200))






