from PIL import Image

def encode(source, encoder, out):
    img = Image.open(source)
    mordka = Image.open(encoder)

    px = img.load()
    px_mordka = mordka.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r=px[i,j][0]
            r+= (1 - 2 * int(r > 0)) * int(max(px_mordka[i,j][:-1]) < 10)
            img.putpixel((i,j), (r) + px[i,j][1:])

    img.save(out)
    mordka.close()
    img.close()


def decode(source, encoded, out_name):
    wzo = Image.open(source)
    enc = Image.open(encoded)
    out = Image.new(mode="RGB", size = wzo.size, color = (255,255,255))

    px = wzo.load()
    px_enc = enc.load()

    for i in range(wzo.size[0]):
        for j in range(wzo.size[1]):
            r,g,b = px[i,j]
            r1,g1,b1 = px_enc[i,j]

            if r != r1:
                out.putpixel((i, j), (abs(r1-r),g1,b1))
    out.save(out_name)
    out.show()

krecik = 'krecik.png'
mordka = 'mordka.png'
out = 'krecik2.png'
name = 'decoded.png'

encode(krecik, mordka, out)
decode(krecik, out, name)
