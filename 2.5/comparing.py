"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
userline = ""
userline2 = ""

file = open("2.4/responses.csv")

all_lines = file.read()

print("Hello, Whats your Name!")

reply = input().lower().strip()

for line in all_lines:
    if reply in line.lower():
        print("Heres your info.")
        print(line)
        userline = line

print("Who would you like to compare yourself to?")

reply2 = input().lower().strip()

for line2 in all_lines:
    if reply2 in line2.lower():
        print("Heres their info.")
        print(line2)
        userline2 = line2

userline = userline.split(",")

userline2 = userline2.split(",")

userline = list(userline)

result = [item for item in userline if item in userline2]

total = len(result)

percent = total / len(userline) * 100 

print("You have " + str(result) + " in common and are " + str(percent) + " percent alike")

print("Do you wanna see who your most likely to be friends with")

reply3 = input().lower().strip()

if reply3 == "yes" or "yeah":
    print("ok!")

else:
    print("umm k")

data = all_lines.split("/n")

for x in data:
    items = x.split(",")

result2 = [items for item in userline if item in x]

total2 = len(result2)

if total2 > 0.5:
    print("ur similar with" + str(total2))
    
else:
    print("error")