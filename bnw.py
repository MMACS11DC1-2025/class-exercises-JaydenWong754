from PIL import Image
import isname
def binarize(input_filename, output_prefix):
    output_filename = "output_prefix" + "output.png"
    myimage = Image.open(input_filename).load()
    outputimage = Image.open(input_filename)

    w = outputimage.width
    h = outputimage.height

    for i in range(w):
        for j in range(h):
            if isname.is_light((r,g,b)):
                outputimage
                image_output.putpixel(xy, beach_colour)
            else:
                beach_color = (0,0,0)
                xy = (i, j)
                image_output.putpixel(xy, beach_color)
    image_output.save("black.png", "png")