"""
Write an Age in 2056 program that asks your age and outputs how old you'll be 31 years from now.

Examples:

How old are you?
> 10
In 2056, you will be 41 years old!
--
How old are you?
> 25
In 2056, you will be 56 years old!
"""


#Age bot
#print("Hi, how old are you?")

#NowAge = int(input())

#OldAge = NowAge + 31

#print("You will be " + str(OldAge) + " in 31 years.")

# Exercise 0: Factorial
# Remember that n! is defined as n * (n-1)! and 0! is 1
print("give a number")

n = int(input().strip())

def factorial(n):
        if n == 1:
            return 1
        return n * factorial(n-1)

factorial(n)

print(factorial(n))