def showList(inputList):
    for i in inputList:
        print(" ".join(i))

size = int(input())

# build the magic square, init all to 0
mg = []
for i in range(size):
    mg.append([])
    for j in range(size):
        mg[i].append(0)

# first row mid value is 1
cursor = [0, size//2]
mg[0][size//2] = 1
current = 2

# expand magic square
for i in range(size ** 2 - 1):
    #print(cursor)
    #showList(mg)
    y = cursor[0]
    x = cursor[1]
    if cursor[0] == 0 and cursor[1] != size - 1:
        cursor = [size - 1, x + 1]
    elif cursor[0] != 0 and cursor[1] == size - 1:
        cursor = [y - 1, 0]
    elif cursor[0] == 0 and cursor[1] == size - 1:
        cursor = [y + 1, x]
    elif cursor[0] != 0 and cursor[1] != size - 1:
        #print(mg[y - 1][x + 1])
        if mg[y - 1][x + 1] == 0:
            cursor = [y - 1, x + 1]
        else:
            cursor = [y + 1, x]
    
    mg[cursor[0]][cursor[1]] = current
    current += 1

# build 2d array from int to str
for y in range(len(mg)):
    for x in range(len(mg[y])):
        mg[y][x] = str(mg[y][x])

showList(mg)

