from exif import Image

img = Image('meta.py')
print(img.has_exif)

lat = img.get("gps_latitude")
lon = img.get("gps_longitude")

