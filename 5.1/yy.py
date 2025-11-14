from PIL import Image
import coolcolours

image_green = Image.open("R.jpg").load()
image_beach = Image.open("beach.jpg").load()

image_output = Image.open("R.jpg")

w = image_output.width
h = image_output.length

for i in range(w):
    for j in range(h):
        r = image_green[i, j][0]
        g = image_green[i, j][1]
        b = image_green[i, j][2]

        if coolcolours.isgreen(r, g, b):
            beach_colour = image_beach[i, j]
            image_output.putpixel((i, j), beach_colour)

image_output.save("output.png", "png")