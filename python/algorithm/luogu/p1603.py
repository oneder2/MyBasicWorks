words = input().split(" ")
alpha = {
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9,
        "ten":10,
        "eleven":11,
        "twelve":12,
        "thirteen":13,
        "fourteen":14,
        "fifteen":15,
        "sixteen":16,
        "seventeen":17,
        "eighteen":18,
        "nineteen":19,
        "twenty":20,
        "a":1,
        "both":2,
        "another":1,
        "first":1,
        "second":2,
        "third":3
        }
numWords = []
for word in words:
    if word in alpha:
        numWords.append((alpha[word] ** 2) % 100)
numWords.sort()
strWords = []
for i in numWords:
    strvalue = str(i)
    if i < 10:
        strvalue = "0" + strvalue
    strWords.append(strvalue)
strNewWord = "".join(strWords)
if strNewWord == "":
    code = 0
else:
    code = int(strNewWord)
print(code)
