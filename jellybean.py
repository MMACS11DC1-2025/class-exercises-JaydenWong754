import time

t0 = time.time()

from PIL import Image

def colour(r, g, b):
    if 0 <= r < 50 and 0 <= g < 50 and 0 <= b < 50:
        return "black"

    # 2. Check Red
    if r >= 219 and g > 182 and 0 <= b:
        return "red"

    # 3. Check Green
    if r < 86 and g <= 154 and b < 58:
        return "green"

    # 4. Check Blue
    if r < 200 and 0 <= g < 200 and 230 < b <= 255:
        return "blue"

    # 5. Check Pink (now checked AFTER black)
    if r <= 194 and g <= 86 and b <= 141:
        return "pink"
    
    # 6. Check Yellow
    if r <= 255 and g <= 255 and b < 25:
        return "yellow"
        
    # 7. Check Orange
    if r <= 239 and g < 131 and 0 < b:
        return "orange"
    

file = Image.open("jellybean.png")
jbImage = file.load()

t1 = time.time()

yellowPixels = []
redPixels = []
greenPixels = []
bluePixels = []
pinkPixels = []
blackPixels = []
orangePixels = []

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

t2 = time.time()
numYellow = len(yellowPixels)
numRed = len(redPixels)
numGreen = len(greenPixels)
numPink = len(pinkPixels)
numBlack = len(blackPixels)
numOrange = len(orangePixels)
numBlue = len(bluePixels)

totalPixels = width*height
yellowRatio = numYellow / totalPixels
redRatio = numRed / totalPixels
greenRatio = numGreen / totalPixels
pinkRatio = numPink / totalPixels
blackRatio = numBlack / totalPixels
orangeRatio = numOrange / totalPixels
blueRatio = numBlue / totalPixels

yellowPercent = yellowRatio * 100
redPercent = redRatio * 100
greenPercent = greenRatio * 100
bluePercent = blueRatio * 100
pinkPercent = pinkRatio * 100
blackPercent = blackRatio * 100
orangePercent = orangeRatio * 100

t3 = time.time()

report = "{:.2f}% of the jellybeans are yellow, {:.2f}% are red, {:.2f}% are blue, {:.2f}% are green, {:.2f}% are orange, {:.2f}% are black".format(yellowPercent, redPercent, bluePercent, greenPercent, orangePercent, blackPercent)
print(report)

module_load = t1 - t0
image_open_load = t2 - t1
loop = t3-t2
entire = t3 - t0

timings = "It took {:.2f}s to import the PIL, {:.2f}s to load the image, and {:.2f}s to do the loop. All in all it took {:.2f}s.".format(module_load, image_open_load, loop, entire)
print(timings)