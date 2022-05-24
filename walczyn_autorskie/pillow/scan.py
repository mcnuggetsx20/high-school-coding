from exif import Image
#from math import sin, cos, acos, radians, sqr
from numpy import cos, sin, arccos, pi, radians, sqrt
from haversine import haversine
from subprocess import check_output

def link_gen(lat, lon):
    link = 'https://www.google.pl/maps/place/' + lat + ',' + lon
    return link

def solve(img, pin, radius):
    img_name = img.split('/')[-1]
    img = Image(img)

    if not img.has_exif:
        return None #img_name + ': An improper file given'

    lat = img.get("gps_latitude")
    lon = img.get("gps_longitude")

    if lat==None or lon==None:
        #print(img_name + ': No coordinate information in the given file')
        return None

    lat = lat[0] + lat[1]/60 +lat[2]/3600
    lon = lon[0] + lon[1]/60 +lon[2]/3600

    dst = haversine([lat,lon], pin)/1000

    if dst <= radius:
        return img_name + ': ' + link_gen(str(lat), str(lon))
    else:
        #print(img_name + ': was taken too far away!')
        return None
    return

def form(path):
    #path = '/home/mcnuggetsx20/Documents/programming/high-school-coding/walczyn_autorskie/pillow/' + dir_name
    files = check_output("ls -la " + path + " | awk '{print $1 " + '" "' + " $9}'", shell=True, encoding='utf-8').split('\n')[3:-1]

    for i, val in enumerate(files):
        files[i] = val.split()
        files[i][0] = files[i][0][0]
        files[i][1] = path + files[i][1]
        if files[i][0] == 'd':
            files[i][1] += '/'
    return files

def scan(dir_name,pin, radius):
    out = []
    files = form(dir_name)
    while len(files):
        i = files[0]
        if i[0] =='d':
            new = form(i[1])
            files += new
        else:
            out.append(solve(i[1], pin, radius))

        files.pop(0)
    return out

path = '/home/mcnuggetsx20/Documents/programming/high-school-coding/walczyn_autorskie/pillow/'
pin = [51.110048, 17.060480]
radius = 100

#scan(path,pin,radius)
