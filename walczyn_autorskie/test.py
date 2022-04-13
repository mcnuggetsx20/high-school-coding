from PIL import Image

krecik = '/home/mcnuggetsx20/Pictures/krecik.png'
mrdk = '/home/mcnuggetsx20/Pictures/mordka.png'
out = '/home/mcnuggetsx20/Pictures/krecik2.png'
name = '/home/mcnuggetsx20/Pictures/decoded.png'

img = Image.open(krecik)
#mordka = Image.open(mrdk)
img2 = Image.open(out)

px = img.load()
px2 = img2.load()

print(px[0,0])
print(px2[0,0])


