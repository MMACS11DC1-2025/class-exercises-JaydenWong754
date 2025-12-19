"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
#Jayden Wong
#10/1/25
#Similarity Bot
#Gets 2 users input and turns them into lists
#look at the similarities between items in the lists
#then turns it into a percent and shows it to the user
#ask if they wanna see difference\
#then show it 

#Jayden Wong
#10/18/25 (corrections)
#CORRECTION - i provided test cases 
""" Test case #1, user follows all instructions

Hello, Whats your full name!
Jayden Wong
Who would you like to compare yourself to? enter their full name
Jeremy Wong
You both answered '8' for: What is your favourite digit?
You both answered 'Football' for: Whats your favourite sport to watch?
Youre 25.0 percent alike
nah bro stay away.. very different
do u wanna know ur differences (reply with yes or yeah)
yes
OK :)
You said 'Dog' but they said 'Cat' for: What is your favourite pet among these options?
You said 'French' but they said 'Math' for: Whats your favourite subject?
You said 'Badminton' but they said 'Football' for: Whats your favourite sport to play?
You said 'Hip-hop' but they said 'K-Pop' for: What genre of music do you enjoy most?
You said 'Thriller/Mystery' but they said 'Adventure' for: What is your favourite movie genre?
You said 'Chipotle' but they said 'Bubble Waffle' for: Whats the best fast food nearby?

Test case 2 user does not follow instructions (will say error)

Hello, Whats your full name!
Jayden
Who would you like to compare yourself to? enter their full name
kdanjdkdja;ldj
Sorry one or both of ur names cannot be found or u didnt enter their full name. include space between first and last

Test case 3 user follows instructions, but doesnt know want to know differences

Hello, Whats your full name!
Evan Chan
Who would you like to compare yourself to? enter their full name
Serene Lee
You both answered 'Cat' for: What is your favourite pet among these options?
You both answered 'Math' for: Whats your favourite subject?
You both answered 'Badminton' for: Whats your favourite sport to play?
Youre 37.5 percent alike
nah bro stay away.. very different
do u wanna know ur differences (reply with yes or yeah)
no
k not nice

Test case 4 user enters nothing
Hello, Whats your full name!

Who would you like to compare yourself to? enter their full name

Sorry one or both of ur names cannot be found or u didnt enter their full name. include space between first and last
"""
#Jayden Wong
#10/1/25
#define variables
userline = ""

userline2 = ""

questions = ["What is your favourite digit?", "What is your favourite pet among these options?" , "Whats your favourite subject?" ,"Whats your favourite sport to play?", "Whats your favourite sport to watch?", "What genre of music do you enjoy most?", "What is your favourite movie genre?", "Whats the best fast food nearby?" ]

#open file
file = open("2.4/responses.csv")

#reads all lines in file
#TEST ERROR: i accidentally made readlines read and i had a semantic error
all_lines = file.readlines()

#user inputs and display
print("Hello, Whats your full name!")  

reply = input().lower().strip()

#checks user input
for line in all_lines:
    if reply in line.lower():
        userline = line

print("Who would you like to compare yourself to? enter their full name")

reply2 = input().lower().strip()

for line2 in all_lines:
    if reply2 in line2.lower():
        userline2 = line2

#see if that code is empty 
if userline == "" or userline2 == "":
    print("Sorry one or both of ur names cannot be found or u didnt enter their full name. include space between first and last")
    exit()

#splits the list with commas
userline = userline.strip().split(",")

userline2 = userline2.strip().split(",")

#CORRECTION - checks to see if the lines second item in  the list (1) is equal to the reply (stripped and lowered.) previouusly
#I had it only first name, but it caused issues, so more specific
if userline[1].lower() != reply or userline2[1].lower() != reply2:
    print("Sorry one or both of ur names cannot be found or u didnt enter their full name. include space between first and last")
    exit()


#CORRECTION - I wanted to make the interface better for the advance criteria so i channged how i did it to reference what questions
# were asked from responses.crv , before, i used list comprehensions and i found it easier just to redo it.
total = 0

for x in range(len(questions)):
    if userline[x + 2] == userline2[x + 2]:
        print("You both answered '" + userline[x + 2] + "' for: " + questions[x])
        total = total + 1

# percent alike
percent = total / len(questions) * 100

print("Youre " + str(percent) + " percent alike")

#looks at the data and sees the result to give a comment
if percent == 100:
    print("Wow can u read minds")

elif percent >= 60:
    print("twins!")

elif percent >= 50:
    print("could be best friends!")

elif percent >= 40:
    print("umm maybe a friend")

else:
    print("nah bro stay away.. very different")

#user input and display
print("do u wanna know ur differences (reply with yes or yeah)")

reply3 = input().lower().strip()

#if they wanna see it
if reply3 == "yes" or  reply3 == "yeah":

    print("OK :)")

#CORRECTION - I wanted to make the interface better for the advance criteria so i channged how i did it to reference what questions
# were asked from responses.crv , before, i used list comprehensions and i found it easier just to redo it.
    for x in range(len(questions)):
        if userline[x + 2] != userline2[x + 2]:
            print("You said '" + userline[x + 2] + "' but they said '" + userline2[x + 2] + "' for: " + questions[x])
else:
    print("k not nice")