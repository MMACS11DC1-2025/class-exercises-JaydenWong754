from PIL import Image
import isname

image_beach = Image.open("5.1/dog.jpg").load()

image_output = Image.open("5.1/dog.jpg")

w = image_output.width
h = image_output.height

for i in range(w):
    for j in range(h):
        r = image_beach[i, j][0]
        g = image_beach[i, j][1]
        b = image_beach[i, j][2]

        if isname.is_light((r,g,b)):
            beach_colour = (255,255,255)
            xy = (i, j)
            image_output.putpixel(xy, beach_colour)
        else:
            beach_color = (0,0,0)
            xy = (i, j)
            image_output.putpixel(xy, beach_color)
image_output.save("black.png", "png")