from exif import Image
from math import sin, cos, acos, radians, sqrt

def l(a, b):
    a = [i for i in a]
    b = [i for i in b]
    a[0] = radians(a[0])
    a[1] = radians(a[1])
    b[0] = radians(b[0])
    b[1] = radians(b[1])
    return acos((sin(a[0]) * sin(b[0])) + (cos(a[0]) * cos(b[0]) * cos(abs(a[1]-b[1])))) * 111.1

def link_gen(lat, lon):
    link = 'https://www.google.pl/maps/place/' + lat + ',' + lon
    return link

def func(img, pin, radius):
    img = Image(img)

    lat = img.get("gps_latitude")
    lon = img.get("gps_longitude")

    lat = lat[0] + lat[1]/60 +lat[2]/3600
    lon = lon[0] + lon[1]/60 +lon[2]/3600

    dst = l((lat, lon), pin)

    if dst <= radius:
        print(dst)
        return link_gen(str(lat), str(lon))
    else:
        return None

wro = (51.110048, 17.060480)
print(func('alo.jpg', wro, 100))






