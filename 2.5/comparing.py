"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
score = 0
userline = ""
userline2 = ""

file = open("2.4/responses.csv")

print("Hello, Whats your Name!")

reply = input().lower().strip()

for line in file:
    if reply in line.lower():
        print("Heres your info.")
        print(line)
        userline = line

print("Who would you like to compare yourself to?")

reply2 = input().lower().strip()

for line2 in file:
    if reply2 in line2.lower():
        print("Heres their info.")
        print(line2)
        userline2 = line2

userline = userline.split(",")

userline2 = userline2.split(",")

userline = list(userline)

userline2 = list(userline2)

print(userline)
print(userline2)