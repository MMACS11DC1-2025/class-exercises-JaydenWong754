#import time module
import time

#start timing program
t0 = time.time()

#import the image module from library
from PIL import Image

#list of image file paths (10)
images = ["6.7/1.png", "6.7/2.png", "6.7/3.png", "6.7/4.png", "6.7/5.png", "6.7/6.png", "6.7/7.png", "6.7/8.png", "6.7/9.png", "6.7/0.png"]

#list to store tuples
imageresults = []

#import pil time
t1 = time.time()

'''
classifies a pixel as dead, alive, or unknown based on its rgb color
brighter greens are alive,
yellows / browns are dead,
any other pixel not ALIVE or DEAD will be classified as unknown
'''
#TEST ERROR - Took me a very long time to fix the rgb values, just playing around until my liking
def is_target_feature(r, g, b):
    #check if pixel is "dead", if it is will return dead
    if 150 <= r <= 230 and 120 <= g <= 200 and 0 <= b <= 100:
        return "dead"
    #check if pixel is "alive", if it is will return alive
    elif 0 <= r <= 200 and 80 <= g <= 255 and 0 <= b <= 120:
        return "alive"
    #check if pixel is "unknown", if it is will return unknown
    else:
        return "unknown"

#variables to measure time performance to optimize time
#total time spent opening images
image_open_time_cumulative = 0
#total time spent processing pixels
loop_time_cumulative = 0

#MAIN loop, processes the images in list
for a in images:
    #measure how long opening each image takes
    t_start_image = time.time() 
    file = Image.open(a)
    jbImage = file.load() #load the data
    t_after_image_open = time.time() 

    #store each pixel based on how it was classified (dead alive or unknown)
    deadPixels = []
    alivePixels = []
    unknownPixels = []

    #width + height to know how big the image is to iterate through all the pixels
    width = file.width
    height = file.height

    #measures how long pixel loop takes
    t_start_loop = time.time() 

    #loop thru every pixel in image
    for x in range(width):
        for y in range(height):
            pixel_r = jbImage[x, y][0]
            pixel_g = jbImage[x, y][1]
            pixel_b = jbImage[x, y][2]

            #classify pixel using func created earlier
            pixel_colour = is_target_feature(pixel_r, pixel_g, pixel_b)

            #ads pixel to list its classified as, whatever it returned
            if pixel_colour == "dead":
                deadPixels.append((pixel_r, pixel_g, pixel_b))

            elif pixel_colour == "alive":
                alivePixels.append((pixel_r, pixel_g, pixel_b))

            else:
                unknownPixels.append((pixel_r, pixel_g, pixel_b))

    t_end_loop = time.time() 
    
    #test error - used to dissplay as 0, now fixed
    #add time to total
    image_open_time_cumulative += (t_after_image_open - t_start_image)
    loop_time_cumulative += (t_end_loop - t_start_loop)

    #count the pixels
    numDead = len(deadPixels)
    numAlive = len(alivePixels)
    numUnknown = len(unknownPixels)

    #find the area
    totalPixels = width*height

    #find the ratio of alive to dead to unknown
    deadRatio = numDead / totalPixels
    aliveRatio = numAlive / totalPixels
    unknownRatio = numUnknown / totalPixels

    #multiply by 100 to get the percent
    deadPercent = deadRatio * 100
    alivePercent = aliveRatio * 100
    unknownPercent = unknownRatio * 100

    #store resulkts
    #test error - had to add "a" or second element to help with binary search
    imageresults.append((alivePercent, a))

    #print the summary for detection
    report = "for image" + str(a) + " {:.2f}% detected alive, {:.2f}% detected dead, {:.2f}% unknown, not detetcted.".format(alivePercent, deadPercent, unknownPercent)
    print(report)

    #decides if the grass is alive or dead
    if alivePercent > 60:
        print("overall alive")

    else:
        print("overall dead")

#record time after the main processing loop finish
t2 = time.time()

#sel sort algorithm to sort it by alivePercent from most alive to least alive
for i in range(len(imageresults)):
    largest_score = imageresults[i][0]
    largest_index = i
    
    #find largest index of unsorted side of list (from i+1 to end)
    for j in range(i + 1, len(imageresults)):
        #comapare alive percent
        if imageresults[j][0] > largest_score: 
            largest_score = imageresults[j][0]
            largest_index = j
    
    #swap the largest element found with the element at the current position 'i'
    imageresults[largest_index], imageresults[i] = imageresults[i], imageresults[largest_index]

print(imageresults)

#TEST ERROR - Confused with ARRAYs, tried doing :4 (0, 1, 2, 3, 4)
#print top 5 results
for y in imageresults[:5]:
    print("File: " + str(y[1]) + ", Alive Score: " + "{:.2f}".format(y[0]) + "%") 

#record time after sorting
t3 = time.time()

#calculate the times
module_load = t1 - t0
image_open_load = image_open_time_cumulative
loop = loop_time_cumulative
entire = t3 - t0

#format + print time summary
timings = "It took {:.3f}s to import the PIL, {:.3f}s to load the image, and {:.3f}s to do the loop. All in all it took {:.3f}s.".format(module_load, image_open_load, loop, entire)


print(timings)

#TEST ERROR - I had my elif and else swapped with defining the new midpoint
#work in progress, commentys later
def search(list_of_lists, query):
    for i in range(len(list_of_lists)):
        smallest_id = int(list_of_lists[i][1][4])
        smallest_index = i
        
        for j in range(i + 1, len(list_of_lists)):
            current_id_in_loop = int(list_of_lists[j][1][4])
            
            if current_id_in_loop < smallest_id: 
                smallest_id = current_id_in_loop
                smallest_index = j
        
        list_of_lists[smallest_index], list_of_lists[i] = list_of_lists[i], list_of_lists[smallest_index]

    search_start_index = 0
    search_end_index = len(list_of_lists) - 1

    while search_start_index <= search_end_index:
        midpoint = (search_start_index + search_end_index) // 2
        
        midpoint_id = int(list_of_lists[midpoint][1][4])

        if midpoint_id == query:
            return list_of_lists[midpoint][0]

        elif midpoint_id < query:
            search_start_index = midpoint + 1 
        else:
            search_end_index = midpoint - 1

    return -1

print(f"Alive Score for Image 2: {search(imageresults, 2)}%")