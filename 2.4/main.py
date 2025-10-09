score = 0
questions = ["Did you eat", "Did you study", "Did you do laundry"]

for x in questions:
    print(x)
    reply = input().strip().lower()
    
    if reply == "yes":
        score += 1
        
if score >= 2:
    print("good")
    
elif score == 1:
    print("k")

elif score == 0:
    print("im coming")