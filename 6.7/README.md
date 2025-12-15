
- [ ] Testing and robustness: include a section in your README describing testing done to ensure each of the tasks works as intended (1 pt)
- [ ] Performance analysis: include a section in your README describing your code profiling: give an example of the report and discuss what parts of the program take the longest
- [ ] Challenges faced: include a section in your README describing at least one challenge faced and how you overcame it (2 pts)




### Creativity and Originality
- [ ] The chosen theme and visual feature are unique, interesting, and insightful (2 pts)
- [ ] Feature detection uses a more advanced process, such as pre-processing the image, using multiple pixels, or using statistical approaches to detect features (4 points)
- [ ] Captured feature involves a real-world use-case. References a real paper, report, or dataset supporting decisions for detecting feature (4 points)

## **SUBMISSION REQUIREMENTS**

### **Files to Include:**
1. `main.py` - Your complete Python program
1. `README.md` - Documentation file with all required content.
1. Images - The set of at least 10 images that your program will analyze
1. (Optional): - Other Python modules you write that you import for use in `main.py`

### **Required Documentation Content Summary:**
- Project overview, including your chosen image theme
- Explanation of your visual feature and how it will be identified
- Discussion of the testing and validation done to verify your program works as intended
- Discussion of your code profiling
- Discussion of challenges faced while working on this project

Grass Health Meter - By Jayden Wong

The Grass Health Meter was inspired by the New Zeland Lawn Addicts Lawn Awards, awarding participants all over the country awards and prizes for the
 brightest, greenist, and beautiful lawns. (https://www.newzealandlawnaddicts.com/new-zealand-lawn-awards/). Instead of human judges, my algorithm
  would have the user upload a photo of their lawn, classify each pixel as "dead" "alive" or "unknown" based on its RGB within a certain range, 
 detecting light/dark green or gold/brown colors. Any other pixel remaining would go into the else, being unknown.

With Human Voters alone, it is easy for unfairness and errors, for example, a absurdly terrible lawn winning for being a "joke." After Human voting for the top 10 lawns, my algorithm will give it a score / 100 based on how "alive" the grass looks, then printing the top 5 as a leaderboard.

My algorithm would also allow for users to search up lawns, finding local favorites or friends with Binary Search, searching for the file name to get it's alive score or place on the leaderboard.

One of the biggest challenges I faced was RGB