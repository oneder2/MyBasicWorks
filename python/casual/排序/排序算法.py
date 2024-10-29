import random

numlist = []
length = 10

#随意创造一个列表
for i in range(length):
    numlist.append(random.randint(0,10))

print(numlist)

for i in range(0, len(numlist)):
    key = numlist[i]
    while i > 0 & i < numlist[i-1]:
        numlist[i+1] = numlist[i]
        numlist[i] = key