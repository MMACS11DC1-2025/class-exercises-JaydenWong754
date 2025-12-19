import time

t0 = time.time()

from PIL import Image

images = ["6.7/1.png", "6.7/2.png", "6.7/3.png", "6.7/4.png", "6.7/5.png", "6.7/6.png", "6.7/7.png", "6.7/8.png", "6.7/9.png", "6.7/10.png"]

imageresults = []

t1 = time.time()

def colour(r, g, b):
    if 150 <= r <= 230 and 120 <= g <= 200 and 0 <= b <= 100:
        return "dead"
    elif 0 <= r <= 200 and 80 <= g <= 255 and 0 <= b <= 120:
        return "alive"
    else:
        return "unknown"
   
image_open_time_cumulative = 0
loop_time_cumulative = 0

for a in images:
    t_start_image = time.time() 
    file = Image.open(a)
    jbImage = file.load()
    t_after_image_open = time.time() 

    deadPixels = []
    alivePixels = []
    unknownPixels = []

    width = file.width
    height = file.height

    t_start_loop = time.time() 
    for x in range(width):
        for y in range(height):
            pixel_r = jbImage[x, y][0]
            pixel_g = jbImage[x, y][1]
            pixel_b = jbImage[x, y][2]

            pixel_colour = colour(pixel_r, pixel_g, pixel_b)

            if pixel_colour == "dead":
                deadPixels.append((pixel_r, pixel_g, pixel_b))

            elif pixel_colour == "alive":
                alivePixels.append((pixel_r, pixel_g, pixel_b))

            else:
                unknownPixels.append((pixel_r, pixel_g, pixel_b))
    t_end_loop = time.time() 

    image_open_time_cumulative += (t_after_image_open - t_start_image)
    loop_time_cumulative += (t_end_loop - t_start_loop)


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

t2 = time.time()

for i in range(len(imageresults)):
    smallest_score = imageresults[i][0]
    smallest_index = i
    for j in range(i + 1, len(imageresults)):
        if imageresults[j][0] < smallest_score:
            smallest_score = imageresults[j][0]
            smallest_index = j
   
    imageresults[smallest_index], imageresults[i] = imageresults[i],imageresults[smallest_index]

for y in imageresults[:6]:
    print(y[1])


t3 = time.time()

module_load = t1 - t0
image_open_load = image_open_time_cumulative
loop = loop_time_cumulative
entire = t3 - t0

timings = "It took {:.3f}s to import the PIL, {:.3f}s to load the image, and {:.3f}s to do the loop. All in all it took {:.3f}s.".format(module_load, image_open_load, loop, entire)

print(timings)