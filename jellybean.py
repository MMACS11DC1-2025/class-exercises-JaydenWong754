from PIL import Image

def colour(r, g, b):
    if r > 150 and g > 150 and b < 150:
        
        return "yellow"
    
    else:
        return "go away"

file = Image.open("jellybean.png")
jbImage = file.load()

yellowPixels = []

width = file.width
height = file.height

for x in range(width):
    for y in range(height):
        pixel_r = jbImage[x, y][0]
        pixel_g = jbImage[x, y][1]
        pixel_b = jbImage[x, y][2]

        if colour(pixel_r, pixel_g, pixel_b) == "yellow":
            yellowPixels.append(jbImage[x, y])

numYellow = len(yellowPixels)

totalPixels = width*height
yellowRatio = numYellow / totalPixels

yellowPercent = yellowRatio * 100
report = "{:.2f}% of the jellybeans are yellow".format(yellowPercent)
print(report)