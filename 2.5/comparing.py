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

#define variables
userline = ""
userline2 = ""

#open file
file = open("2.4/responses.csv")

#reads all lines in file
#TEST ERROR: i accidentally made readlines read and i had a semantic error
all_lines = file.readlines()

#user inputs and display
print("Hello, Whats your first name!")

reply = input().lower().strip()

#finds input
for line in all_lines:
    if reply in line.lower():
        print("Heres your info.")
        print(line)
        userline = line

#user input and display
print("Who would you like to compare yourself to?")

reply2 = input().lower().strip()

#finds input of other person
#TEST GOOD:Finally worked, before it printed userline variable twice?
for line2 in all_lines:
    if reply2 in line2.lower():
        print("Heres their info.")
        print(line2)
        userline2 = line2

#see if that code is valid 
if userline == "" or userline2 == "":
    print("Sorry one of ur names cannot be found")
    exit()

#splits the list with commas
userline = userline.split(",")

userline2 = userline2.split(",")

#TEST ERROR: i didnt know if i should use list(userline) etc but it ran without and i checked the variable type and it was list

#TEST ERROR: i didnt have [2:] so it kept doing weird stuff with favorite numbers and id
#finds similarities
result = [item for item in userline[2:] if item in userline2[2:]]

#how much items in list
total = len(result)

#TEST ERROR: I need to x 100 because it returns a decimal
#finds percent alike results
#handle error
if len(userline) == 0:
    percent = 0
else:
    percent = total / len(userline) * 100

#TEST ERROR: forgot to turn it to string woops
#TEST GOOD: Finally worked after fixing my code
#user display
print("You have " + str(result) + " in common and are " + str(percent) + " percent alike")

#looks at the data and sees the result to give a comment
if percent >= 50:
    print("Wow yall twins fr")

elif percent >= 40:
    print("could be best friends!")

elif percent >= 30:
    print("umm maybe a friend")

else:
    print("nah bro stay away")

#user input and display
print("do u wanna know ur differences (reply with yes or yeah)")

reply3 = input().lower().strip()

#if they wanna see it
if reply3 == "yes" or  reply3 == "yeah":

    print("OK :)")

    #looks for items not seen in eachothers list
    result2 = [item for item in userline[2:] if item not in userline2[2:]]
    result3 = [item for item in userline2[2:] if item not in userline[2:]]
    
    #user display
    print("you input:" + str(result2) + "while they input: " + str(result3))
    
else:
    #user input and display
    print("k not nice")
