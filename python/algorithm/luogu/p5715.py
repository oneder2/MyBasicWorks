strlist = input().split(" ")
numlist = [int(i) for i in strlist]

for j in range(len(numlist)):
    minindex = j
    for i in range(j, len(numlist)):
        if numlist[i] < numlist[minindex]:
            minindex = i
    numlist[minindex], numlist[j] = numlist[j], numlist[minindex]

ans = ""
for i in range(len(numlist)):
    ans += str(numlist[i])
    if i != len(numlist)-1:
        ans += " "

print(ans)
