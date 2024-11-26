def showList(inputList):
    for i in inputList:
        print(i)
def AddNumToArray(output, inputSignal):
    # input each raw
    for i in range(len(output)):
        # from specific number/signal, input spesific line
        for j in inputSignal[i]:
            output[i].append(j)
    return output
#length = int(input())
#showNum = input()
# build a output list
output = [[],[],[],[],[]]
# nums coding
inputNumList=(
        ((1,1,1),(1,0,1),(1,0,1),(1,0,1),(1,1,1)),# this is 0
        ((0,0,1),(0,0,1),(0,0,1),(0,0,1),(0,0,1)), #this is 1
        ((1,1,1),(0,0,1),(1,1,1),(1,0,0),(1,1,1)), #this is 2
        ((1,1,1),(0,0,1),(1,1,1),(0,0,1),(1,1,1)), #this is 3
        ((1,0,1),(1,0,1),(1,1,1),(0,0,1),(0,0,1)), #this is 4
        ((1,1,1),(1,0,0),(1,1,1),(0,0,1),(1,1,1)), #this is 5
        ((1,1,1),(1,0,0),(1,1,1),(1,0,1),(1,1,1)), #this is 6
        ((1,1,1),(0,0,1),(0,0,1),(0,0,1),(0,0,1)), #this is 7
        ((1,1,1),(1,0,1),(1,1,1),(1,0,1),(1,1,1)), #this is 8
        ((1,1,1),(1,0,1),(1,1,1),(0,0,1),(1,1,1)), #this is 9
        )
# space coding
inputSpace=(
        [0], [0], [0], [0], [0]
        ) # this is the space
showNum = "314159265358"
length = len(showNum)
# input nums to the output list
for i in range(length):
    output = AddNumToArray(output, inputNumList[int(showNum[i])])
    if i != length - 1:
        output = AddNumToArray(output, inputSpace)
# rendering
for y in range(len(output)):
    for x in range(len(output[y])):
        if output[y][x] == 1:
            output[y][x] = "X"
        elif output[y][x] == 0:
            output[y][x] = "."
ans = []
for y in range(len(output)):
    row = ""
    for x in range(len(output[y])):
        row += output[y][x]
    ans.append(row)
# show the list
showList(ans)
