#Q2
score = 0
questions = ["Did you eat?", "Did you study?", "Did you do laundry?", "Did you call grandma?"]

for x in questions:
    print(x)
    if input().strip().lower() == "yes" :
        score += 1

#1 equal sign means updating, 2 equal signs mean comparing
if score == 3 or score == 4:
    print("good")
    
elif score == 1 or score == 2:
    print("ok")
    
elif score == 0:
    print("im coming over")

else:
    print("i didnt hear u")

#Q1
print("Hi person 1")
print("give 3 hobby")
scoree = 0
hob1 = input().strip().lower()

hob1 = hob1.split()

print("Hi person 2")
print("give 3 hobby")

hob2 = input().strip().lower()

hob2 = hob2.split()

result = [item for item in hob1 if item in hob2]

print("you have " + str(result) + " in common")

for item in result:
    scoree+= 1
print(str(scoree) + " things in common")