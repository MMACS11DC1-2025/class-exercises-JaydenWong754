import time

images = ["6.7/1.png", "6.7/2.png", "6.7/3.png", "6.7/4.png", "6.7/5.png", "6.7/6.png", "6.7/7.png", "6.7/8.png", "6.7/9.png", "6.7/10.png"]

t0 = time.time()

from PIL import Image

def colour(r, g, b):
    if 0 <= r < 50 and 200 <= g < 255 and 0 <= b < 50:
        return "white"

    elif 200 <= r <= 255 and 200 <= g <= 255 and 0 <= b <= 50:
        return "black"
    
    else:
        return "unknown"
    

for a in images:
    file = Image.open(a)
    jbImage = file.load()

    t1 = time.time()

    blackPixels = []
    whitePixels = []

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


    t2 = time.time()

    numDead = len(deadPixels)
    numAlive = len(alivePixels)

    totalPixels = width*height

    deadRatio = numDead / totalPixels
    aliveRatio = numAlive / totalPixels

    deadPercent = deadRatio * 100
    alivePercent = aliveRatio * 100

    t3 = time.time()

    report = "for image" + str(a) + " {:.2f}% are alive, {:.2f}% are dead".format(alivePercent, deadPercent)
    print(report)

    if deadPercent + alivePercent < 60:
        print("alive")

    else:
        print("dead")

    module_load = t1 - t0
    image_open_load = t2 - t1
    loop = t3-t2
    entire = t3 - t0

    #timings = "It took {:.2f}s to import the PIL, {:.2f}s to load the image, and {:.2f}s to do the loop. All in all it took {:.2f}s.".format(module_load, image_open_load, loop, entire)
    #print(timings)