'''
def biggest(list):
    bignum = list[0]
    for x in list:
        if x > bignum:
            bignum = x
    return bignum

list = [1, 2, 3, 4]

print(biggest(list))
'''
'''
titles = []
count = 1
counter = 0
print("how many books")
amt = input()
finalcount = 0

for x in range(int(amt)):
    print("title " + str(count) + " ?")
    title = input().strip().lower()
    titles += title
    count += 1

booktitle = True

while booktitle == True:
    print("max title length?")
    maxwords = int(input())

    if maxwords == " ":
        booktitle = False
    
    else:
        for y in titles:
            y.split()
            for z in y.split():
                counter += 1
                if counter < maxwords:
                    finalcount += 1
    print("theres " + str(finalcount) + " book with under " + str(maxwords) + " words")
'''

name = []
vowel = []
print("give a name")
name = input().split()
newname = name
for x in name:
    if x in "aeiou":
        vowel += x
        for
        

"for i in range(len(vowel)):"
    "if x in "":"
        "x = vowel[-1 - i]"


'''
import random
words = random.choice(["lose", "cats", "fart"])
chars = len(words)
x = True
while x == True:
    print("guess a letter")
    guess = input().strip().lower()
    for y in range(chars):
        if guess == words[y]:
            print(str(guess) + "is the " +str(y + 1) + "letter out of " + str(chars) )

    if guess == words:
        print("u got it! it was " + words)
        x = False
'''