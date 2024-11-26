# first line input
comnum = int(input())
# second line input
scoreList = input().split(" ")
# int the str nums
for i in range(0, len(scoreList)):
    scoreList[i] = int(scoreList[i])

maxScore = 0
minScore = 10
sumUp = 0
for i in scoreList:
    sumUp += i
    if maxScore < i:
        maxScore = i
    if minScore > i:
        minScore = i

sumUp = sumUp - minScore - maxScore
print(round( sumUp / (comnum-2), 2))
