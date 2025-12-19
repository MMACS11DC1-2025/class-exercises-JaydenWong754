- [ ] Performance analysis: include a section in your README describing your code profiling: give an example of the report and discuss what parts of the program take the longest
- Discussion of your code profiling

Grass Health Meter - By Jayden Wong

The Grass Health Meter was inspired by the New Zeland Lawn Addicts Lawn Awards, awarding participants all over the country awards and prizes for the
 brightest, greenist, and beautiful lawns. (https://www.newzealandlawnaddicts.com/new-zealand-lawn-awards/). Instead of human judges, my algorithm
  would have the user upload a photo of their lawn, classify each pixel as "dead" "alive" or "unknown" based on its RGB within a certain range, 
 detecting light/dark green or gold/brown colors. Any other pixel remaining would go into the else, being unknown.

With Human Voters alone, it is easy for unfairness and errors, for example, a absurdly terrible lawn winning for being a "joke." After Human voting for the top 10 lawns, my algorithm will give it a score / 100 based on how "alive" the grass looks, then printing the top 5 as a leaderboard.

My algorithm would also allow for users to search up lawns, finding local favorites or friends with Binary Search, searching for the file name to get it's alive score or place on the leaderboard.

A challenges I faced was RGB detection, aa I could not get it to work for all images. I played around with values for all colors until it worked, but now, some images havce alot of "unknown pixels" but still with lots of accuracy.

My biggest challenge was using Binary sort to find a specific image's alive percent. Previously, I had displayed the top 5 scores using selection sort, ordering it from greatest to least, disregarding the image number. Because I believed the list was already sorted, I was puzzled for multiple classes why it was not working, semantic errors displayig unpredictable results. I even tried using the math function from the PIL to see if my isssue was rounding.

I overcame this by retracing my steps and asking peers to do a check on my code, finally realizing the selection sort was different on how I had ordered it, and I wanted to search by image, not percent. To fix it, I used selection sort inside my binary search function to re-sort the list, printing without errors.

Throught the last 2 weeks when I first started my project, I tested, comment, and worked on my code almost daily whenevere I had the chance.

To fix errors, my main strategy was looking at the DEBUG CONSOLE to fix little errors(missing brackets, colon variabkle definition) and PRINTING for the more challenging errors, finding the last good output before it went wrong, then trying to fix the code beyond that. I also like to ask peers, upperclassmen, and my Teacher for help and advice on my code. I make sure my code is organized so it is easy to read and self evaluate.

My program works fully as intended, fullfilling all of the code's requirements. It processes the image, evaluate its alive score, prints the top 5 results, and allows the user to search an image for its alive percent.

something "advanced" I tried to incorporate was weighing green pixels over 210 to have a extra weight of 1.5 percent, rewarding lawns with brighter greener grass to shine.
I added this later, so it was not previously mentioned. Lawns with brighter grass are likely more healthy, so I reward them more with a small boost

CODE PERFORMANCE ANALYSIS
I decided to run my program 5 times to determine my approx run time

It took 0.040s to import the PIL, 0.141s to load the image, and 6.038s to do the loop. All in all it took 6.476s.
It took 0.043s to import the PIL, 0.136s to load the image, and 5.724s to do the loop. All in all it took 6.143s.
It took 0.049s to import the PIL, 0.148s to load the image, and 5.723s to do the loop. All in all it took 6.148s.
It took 0.037s to import the PIL, 0.148s to load the image, and 5.553s to do the loop. All in all it took 5.965s.
It took 0.036s to import the PIL, 0.146s to load the image, and 5.708s to do the loop. All in all it took 6.113s.

My program consistantly takes 6 seconds, down, previously from the 11 seconds I had before.

This is because putting selection sort inside binary search really messed and slowed the program. In addition, my code was full of bugs, so after optimizing, I reduced it down to 6 seconds. 

The loop takes the most amount of time, as