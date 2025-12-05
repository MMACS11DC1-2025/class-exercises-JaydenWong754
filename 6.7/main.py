import time

images = ["6.7/1.png", "6.7/2.png", "6.7/3.png", "6.7/4.png", "6.7/5.png", "6.7/6.png", "6.7/7.png", "6.7/8.png", "6.7/9.png", "6.7/10.png"]

imageresults = []

t0 = time.time()

from PIL import Image

def colour(r, g, b):
    if 150 <= r <= 230 and 120 <= g <= 200 and 0 <= b <= 100:
        return "dead"
    elif 0 <= r <= 200 and 80 <= g <= 255 and 0 <= b <= 120:
        return "alive"
    else:
        return "unknown"
    

for a in images:
    file = Image.open(a)
    jbImage = file.load()

    t1 = time.time()

    deadPixels = []
    alivePixels = []
    unknownPixels = []

    width = file.width
    height = file.height

    for x in range(width):
        for y in range(height):
            pixel_r = jbImage[x, y][0]
            pixel_g = jbImage[x, y][1]
            pixel_b = jbImage[x, y][2]

            if colour(pixel_r, pixel_g, pixel_b) == "dead":
                deadPixels.append(jbImage[x, y])

            elif colour(pixel_r, pixel_g, pixel_b) == "alive":
                alivePixels.append(jbImage[x, y])

            else:
                unknownPixels.append(jbImage[x, y])


    numDead = len(deadPixels)
    numAlive = len(alivePixels)
    numUnknown = len(unknownPixels)

    totalPixels = width*height

    deadRatio = numDead / totalPixels
    aliveRatio = numAlive / totalPixels
    unknownRatio = numUnknown / totalPixels

    deadPercent = deadRatio * 100
    alivePercent = aliveRatio * 100
    unknownPercent = unknownRatio * 100

    imageresults.append((alivePercent, a))

    
    report = "for image" + str(a) + " {:.2f}% detected alive, {:.2f}% detected dead, {:.2f}% unknown, not detetcted.".format(alivePercent, deadPercent, unknownPercent)
    print(report)

    if alivePercent > 60:
        print("overall alive")

    else:
        print("overall dead")

for i in range(len(imageresults)):
    smallest_score = imageresults[i][0]
    smallest_index = i
    for j in range(i + 1, len(imageresults)):
        if imageresults[j] < smallest_score:
            smallest_score = imageresults[j]
            smallest_index = j
    
    imageresults[smallest_index], imageresults[i] = imageresults[i],imageresults[smallest_index]



t2 = time.time()

print(imageresults)

t3 = time.time()

'''
module_load = t1 - t0
image_open_load = t2 - t1
loop = t3-t2
entire = t3 - t0
'''
#timings = "It took {:.3f}s to import the PIL, {:.3f}s to load the image, and {:.3f}s to do the loop. All in all it took {:.3f}s.".format(module_load, image_open_load, loop, entire)

#print(timings)