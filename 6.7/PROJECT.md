TOTAL: ___ / 100



## Project Description



**Goal:** Create a Python program that analyzes a set of at least 10 images based around a theme of your choice (e.g., medical scans, satellite photos, historical archives, deep-sea research photos).

Using the new skills in units 5 and 6, you will implement a computer vision algorithm that detects a visual feature.



## "Gotta Have" Checklist



## **ESSENTIAL REQUIREMENTS**

### Project Overview - Must appear in a README.md file



> *These items belong at the very top of your `README.md`. They give the context for everything else you do.*



- [yes ] Choose a specific theme for which you will be scanning multiple images (3 pts)

- [m ] Clearly define the visual feature your program will detect and count (2 pts)

- [ m] Justify your feature detection with an explanation of how your chosen feature can be accurately identified (3 pts)



### Image Processing and Feature Extraction (Unit 5)

#### Task 1: Pixels to Data Function

- [ ] Write a function, is_target_feature, that accepts pixel data (e.g. colour channels as RGB tuple inputs) and returns a specific, useful output (e.g., returns True if the pixel matches your custom feature definition else False, or a weight) (10 pts)

#### Task 2: Pixel Iteration and List Building

- [ m] Use nested loops to iterate over all pixels **in a set of at least 10 images** and calculate your "Feature Density Score" for each image (10 pts)

- [ ] Append the filename and score to a master list, demonstrating list manipulation and the use of the append() method (5 pts)

#### Task 3: Code Profiling

- [yes ] Measure the precise time taken for the program to complete the pixel processing loops using the time module (3 pts)

- [yes ] Output this time in a human-readable report, using string formatting to ensure the output displays accurately to three decimal places (2 pts)



### Algorithms and Efficiency (Unit 6)

#### Task 4: Selection Sort

- [ ] Implement the Selection Sort algorithm function yourself (not using built-in libraries for sorting) to sort the master list based on the calculated Feature Density Score (highest to lowest) (12 pts)

- [ ] Output the top 5 results using list slicing (3 pts)

#### Task 5: Binary Search

- [ ] Implement the Binary Search algorithm function yourself to search the sorted list for a specific target score (10 pts)



### Process

- [ ] Algorithm design in English: outline the logic using English comments (pseudocode) before each major Python code block (3 pts)

- [ ] Code clarity: use descriptive variable names unless they are standard loop indices (e.g. x, y) (2 pts)

- [ ] Use of functions: structure the program using functions to organize it and reduce code duplication (2 pts)

- [ ] Testing and robustness: include a section in your