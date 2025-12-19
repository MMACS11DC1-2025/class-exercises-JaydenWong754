import time

t0 = time.time()

from PIL import Image

def colour(r, g, b):

    if 0 <= r < 50 and 0 <= g < 50 and 0 <= b < 50:
        return "black"

    if r > 200 and g < 60 and b < 60:
        return "red"

    if r > 200 and g > 100 and g < 180 and b < 50:
        return "orange"
        
    if r > 200 and g > 200 and b < 50:
        return "yellow"

    if g > 200 and r < 60 and b < 60:
        return "green"

    if b > 200 and r < 60 and g < 150: 
        return "blue"
        
    if r > 150 and b > 200 and g < 40: 
        return "purple"
    
file = Image.open("5.5/rain.png")
jbImage = file.load()

t1 = time.time()

yellowPixels = []
redPixels = []
greenPixels = []
bluePixels = []
pinkPixels = []
blackPixels = []
orangePixels = []
purplePixels = []

width = file.width
height = file.height

for x in range(width):
    for y in range(height):
        pixel_r = jbImage[x, y][0]
        pixel_g = jbImage[x, y][1]
        pixel_b = jbImage[x, y][2]

        if colour(pixel_r, pixel_g, pixel_b) == "yellow":
            yellowPixels.append(jbImage[x, y])
        
        elif colour(pixel_r, pixel_g, pixel_b) == "red":
            redPixels.append(jbImage[x, y])

        elif colour(pixel_r, pixel_g, pixel_b) == "green":
            greenPixels.append(jbImage[x, y])

        elif colour(pixel_r, pixel_g, pixel_b) == "blue":
            bluePixels.append(jbImage[x, y])

        elif colour(pixel_r, pixel_g, pixel_b) == "pink":
            pinkPixels.append(jbImage[x, y])

        elif colour(pixel_r, pixel_g, pixel_b) == "black":
            blackPixels.append(jbImage[x, y])

        elif colour(pixel_r, pixel_g, pixel_b) == "orange":
            orangePixels.append(jbImage[x, y])

        elif colour(pixel_r, pixel_g, pixel_b) == "purple":
            purplePixels.append(jbImage[x, y])

t2 = time.time()
numYellow = len(yellowPixels)
numRed = len(redPixels)
numGreen = len(greenPixels)
numPink = len(pinkPixels)
numBlack = len(blackPixels)
numOrange = len(orangePixels)
numBlue = len(bluePixels)
numPurple = len(purplePixels)

totalPixels = width*height
yellowRatio = numYellow / totalPixels
redRatio = numRed / totalPixels
greenRatio = numGreen / totalPixels
pinkRatio = numPink / totalPixels
blackRatio = numBlack / totalPixels
orangeRatio = numOrange / totalPixels
blueRatio = numBlue / totalPixels
purpleRatio = numPurple / totalPixels

yellowPercent = yellowRatio * 100
redPercent = redRatio * 100
greenPercent = greenRatio * 100
bluePercent = blueRatio * 100
pinkPercent = pinkRatio * 100
blackPercent = blackRatio * 100
orangePercent = orangeRatio * 100
purplePercent = purpleRatio * 100

t3 = time.time()

report = "{:.2f}% of the jellybeans are yellow, {:.2f}% are red, {:.2f}% are blue, {:.2f}% are green, {:.2f}% are orange, {:.2f}% are black, {:.2f}% are purple".format(yellowPercent, redPercent, bluePercent, greenPercent, orangePercent, blackPercent, purplePercent)
print(report)

module_load = t1 - t0
image_open_load = t2 - t1
loop = t3-t2
entire = t3 - t0

timings = "It took {:.2f}s to import the PIL, {:.2f}s to load the image, and {:.2f}s to do the loop. All in all it took {:.2f}s.".format(module_load, image_open_load, loop, entire)
print(timings)