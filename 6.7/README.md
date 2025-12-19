
#Grass Health Meter - By Jayden Wong

The Grass Health Meter was inspired by the New Zeland Lawn Addicts Lawn Awards, awarding participants all over the country awards and prizes for the
 brightest, greenist, and beautiful lawns. (https://www.newzealandlawnaddicts.com/new-zealand-lawn-awards/). Instead of human judges, my algorithm would have the user upload a photo of their lawn, classify each pixel as "dead" "alive" "veryalive" or "unknown" based on its RGB within a certain range, 
 detecting light/dark green or gold/brown colors. Any other pixel remaining would go into the else, being unknown.

With Human Voters alone, it is easy for unfairness and errors, for example, a absurdly terrible lawn winning for being a "joke." After Human voting for the top 10 lawns, my algorithm will give it a score / 100 based on how "alive" the grass looks, then printing the top 5 as a leaderboard.

My algorithm would also allow for users to search up lawns, finding local favorites or friends with Binary Search, searching for the file name to get it's alive score.

A challenges I faced was RGB detection, aa I could not get it to work for all images. I played around with values for all colors until it worked, but now, some images havce alot of "unknown pixels" but still with lots of accuracy.

My biggest challenge was using Binary sort to find a specific image's alive percent. Previously, I had displayed the top 5 scores using selection sort, ordering it from greatest to least, disregarding the image number. Because I believed the list was already sorted, I was puzzled for multiple classes why it was not working, semantic errors displayig unpredictable results. I even tried using the math function from the PIL to see if my isssue was rounding.

I overcame this by retracing my steps and asking peers to do a check on my code, finally realizing the selection sort was different on how I had ordered it, and I wanted to search by image, not percent. To fix it, I used selection sort inside my binary search function to re-sort the list, printing without errors.

Throught the last 2 weeks when I first started my project, I tested, comment, and worked on my code almost daily whenevere I had the chance.

To fix errors, my main strategy was looking at the DEBUG CONSOLE to fix little errors(missing brackets, colon variabkle definition) and PRINTING for the more challenging errors, finding the last good output before it went wrong, then trying to fix the code beyond that. I also like to ask peers, upperclassmen, and my Teacher for help and advice on my code. I make sure my code is organized so it is easy to read and self evaluate.

My program works fully as intended, fullfilling all of the code's requirements. It processes the image, evaluate its alive score, prints the top 5 results, and allows the user to search an image for its alive percent.

something "advanced" I tried to incorporate was weighing green pixels over 210 to have a extra weight of 1.5 percent, rewarding lawns with brighter greener grass to shine.
I added this later, so it was not previously mentioned. Lawns with brighter grass are likely more healthy, so I reward them more with a small boost

##CODE PERFORMANCE ANALYSIS
I decided to run my program 5 times to determine my approx run time

It took 0.040s to import the PIL, 0.141s to load the image, and 6.038s to do the loop. All in all it took 6.476s.
It took 0.043s to import the PIL, 0.136s to load the image, and 5.724s to do the loop. All in all it took 6.143s.
It took 0.049s to import the PIL, 0.148s to load the image, and 5.723s to do the loop. All in all it took 6.148s.
It took 0.037s to import the PIL, 0.148s to load the image, and 5.553s to do the loop. All in all it took 5.965s.
It took 0.036s to import the PIL, 0.146s to load the image, and 5.708s to do the loop. All in all it took 6.113s.

My program consistantly takes 6-6.5 seconds, down, previously from the 11 seconds I had before.

This is because putting selection sort inside binary search really messed and slowed the program. In addition, my code was full of bugs, so after optimizing, I reduced it down to 6 seconds. 

The loop takes the most amount of time, as its the main component of my code, analyzing the whole image.
This could vary by time, as it heavily depends on the image size.

Importing took the fastsest, importing the image module from the PIL, taking an average of 35-50 seconds.

#this is an example of how my code runs.

1.Iterates through each image and prints its alive, dead, and unknown stats

for image 6.7/1.png 39.32% detected alive, 24.50% detected dead, 36.18% unknown, not detetcted.
overall dead
for image 6.7/2.png 20.17% detected alive, 47.74% detected dead, 32.09% unknown, not detetcted.
overall dead
for image 6.7/3.png 39.60% detected alive, 21.30% detected dead, 39.10% unknown, not detetcted.
overall dead
for image 6.7/4.png 23.51% detected alive, 15.93% detected dead, 60.55% unknown, not detetcted.
overall dead
for image 6.7/5.png 33.16% detected alive, 18.91% detected dead, 47.93% unknown, not detetcted.
overall dead
for image 6.7/6.png 57.01% detected alive, 6.01% detected dead, 36.98% unknown, not detetcted.
overall dead
for image 6.7/7.png 60.61% detected alive, 0.11% detected dead, 39.80% unknown, not detetcted.
overall alive
for image 6.7/8.png 68.64% detected alive, 0.01% detected dead, 31.89% unknown, not detetcted.
overall alive
for image 6.7/9.png 88.56% detected alive, 1.30% detected dead, 12.33% unknown, not detetcted.
overall alive
for image 6.7/0.png 87.32% detected alive, 0.00% detected dead, 14.41% unknown, not detetcted.
overall alive

2. Prints the top 5 files/images to a leaderboard
File: 6.7/9.png, Alive Score: 88.56%
File: 6.7/0.png, Alive Score: 87.32%
File: 6.7/8.png, Alive Score: 68.64%
File: 6.7/7.png, Alive Score: 60.61%
File: 6.7/6.png, Alive Score: 57.01%

3. user interface, allows user to search through database
Do you want to search an image to get its alive score? (yes/no): yes
What number? (0-9): 0
Alive Score: 87.32%
Do you want to search an image to get its alive score? (yes/no): yes
What number? (0-9): 4
Alive Score: 23.51%
Do you want to search an image to get its alive score? (yes/no): no
Ok, goodbye!

#shows how long the program took, without the user interface
CODE PROFILING AND TIMING
It took 0.044s to import the PIL, 0.189s to load the image, and 6.711s to do the loop. All in all it took 7.213s.

Some more error handling I did was changing my 4th element single digit ID systym that was easy to error if the file path changed o the number was over a digit with splitting the file name between the / and .

it gets the image (eg 6.7/x.png), splits it by the slash, then the . so it gets whatever between the / and .


