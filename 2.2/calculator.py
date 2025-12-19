"""
Machines are good at crunching numbers - faster and more accurately than most 
humans! Create a small program that calculates something useful to you 
(making you smile is useful). It should take user input, at use at least one of the 
number operators we saw in class: + / * . You may modify one of your previous 
exercises to include calculations, if you wish.

Remember to design your algorithm in English first, then translate it to Python 
code. Test as you go!
"""
#prints info
print("calculator")
print("enter a number eg 1 2 3 4 5")

#defines input
number1 = input()

#prints info
print("enter another number eg 1 2 3 4 5")

#defines input
number2 = input()

#ask user what operator
print("times or plus")

#defines input
operator = input().lower().strip()

#does multiplication
if operator == "times":
    ans = int(number1) * int(number2)
    print(ans)

#does addition
elif operator == "plus":
    ans = int(number1) + int(number2)
    print(ans)

#if somehow doesnt work
else:
    print("idk try again")