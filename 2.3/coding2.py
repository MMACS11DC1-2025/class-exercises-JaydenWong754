"""
Write an Olympic Judging program that outputs the average scores from 5 different judges. 

Each score is out of 10 points maximum. Half points are allowed (e.g. 7.5)

The program should take 5 inputs and output the final average score.

Example:

Judge 1: 5.5
Judge 2: 10
Judge 3: 7
Judge 4: 8.5
Judge 5: 9
Your Olympic score is 8.0
"""

#judgebot
totalscore = 0

avgscore = 0
for x in range(5):
    print("hi pls judge the person out of ten in numbers eg 1 2 3")
    score = float(input())
    totalscore += score

avgscore += totalscore / 5


print("ur score is" + str(avgscore) )



