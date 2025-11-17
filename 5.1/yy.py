from PIL import Image
import xx
image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()

image_output = Image.open("5.1/kid-green.jpg")

w = image_output.width
h = image_output.height

for i in range(w):
    for j in range(h):
        r = image_green[i, j][0]
        g = image_green[i, j][1]
        b = image_green[i, j][2]

        if xx.isgreen(r,g,b):
            beach_colour = image_beach[i, j]
            xy = (i, j)
            image_output.putpixel(xy, beach_colour)

image_output.save("output.png", "png")