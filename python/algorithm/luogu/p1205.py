# print list
def ShowList(inputList):
    for i in inputList:
        print(i)

# turn list, 1~3
def TurnList(inputList, opcode):
    level = len(inputList)
    output = BuildTwodList(level)
    for j in range(level):
        for i in range(level):
            if opcode == 1:
                output[j][i] = inputList[i][-j]
            elif opcode == 2:
                output[j][i] = inputList[-j][-i]
            elif opcode == 3:
                output[j][i] = inputList[-i][j]
            elif opcode == 4:
                output[j][i] = inputList[j][-i]
    return output

# build a 2d list
def BuildTwodList(level):
    output = []
    for j in range(level):
        output.append([])
        for i in range(level):
            output[j].append("")
    return output


size = int(input())

square = []
for i in range(size):
    square.append(input())

#target = []
#for i in range(size):
#    target.appen(input())


ShowList(square)
#ShowList(TurnList(square, 1))
#ShowList(TurnList(square, 2))
ShowList(TurnList(square, 3))
#ShowList(TurnList(square, 4))
