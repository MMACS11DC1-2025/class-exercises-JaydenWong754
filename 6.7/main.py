import time


t0 = time.time()

from PIL import Image

def colour(r, g, b):
    if 0 <= r < 50 and 0 <= g < 50 and 0 <= b < 50:
        return "black"

    if 200 <= r <= 255 and 200 <= g <= 255 and 200 <= b <= 255:
        return "white"
    
    if 50 <= r < 200 and 50 <= g < 200 and 50 <= b < 200:
        return "gray"

file = Image.open("6.7/6.png")
jbImage = file.load()

t1 = time.time()

blackPixels = []
whitePixels = []
grayPixels = []

width = file.width
height = file.height

for x in range(width):
    for y in range(height):
        pixel_r = jbImage[x, y][0]
        pixel_g = jbImage[x, y][1]
        pixel_b = jbImage[x, y][2]

        if colour(pixel_r, pixel_g, pixel_b) == "black":
            blackPixels.append(jbImage[x, y])

        elif colour(pixel_r, pixel_g, pixel_b) == "white":
            whitePixels.append(jbImage[x, y])

        if colour(pixel_r, pixel_g, pixel_b) == "grey":
            grayPixels.append(jbImage[x, y])


t2 = time.time()

numBlack = len(blackPixels)
numGray = len(grayPixels)
numWhite = len(whitePixels)

totalPixels = width*height

blackRatio = numBlack / totalPixels
whiteRatio = numWhite / totalPixels
grayRatio = numGray / totalPixels

blackPercent = blackRatio * 100
whitePercent = whiteRatio * 100
grayPercent = grayRatio * 100

t3 = time.time()

report = "{:.2f}% are white, {:.2f}% are gray, {:.2f}% are black".format(whitePercent, grayPercent, blackPercent)
print(report)

module_load = t1 - t0
image_open_load = t2 - t1
loop = t3-t2
entire = t3 - t0

timings = "It took {:.2f}s to import the PIL, {:.2f}s to load the image, and {:.2f}s to do the loop. All in all it took {:.2f}s.".format(module_load, image_open_load, loop, entire)
print(timings)