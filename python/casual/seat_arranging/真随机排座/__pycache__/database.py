from restore import variables

from random import randint

def get(target, zone): # 确定坐标
    for y in range ( len (zone) ) :
        for x in range( len (zone[y]) ):
            if zone[y][x] == target:
                return (x, y)

def left(putin):
    return (putin[0] - 1, putin[1])

def right(putin):
    return (putin[0] + 1, putin[1])

def up(putin):
    return (putin[0], putin[1] - 1)

def down(putin):
    return (putin[0], putin[1] + 1)

def swap(index_a, index_b, field, way):
    if way == 1:
        index_m = up(index_a)
    elif way == 2:
        index_m = down(index_a)
    elif way == 3:
        index_m = left(index_a)
    elif way == 4:
        index_m = right(index_a)
    Mid = field[index_m[1]][index_m[0]]
    field[index_m[1]][index_m[0]] = field[index_b[1]][index_b[0]]
    field[index_b[1]][index_b[0]] = Mid
    return field

def pack(arrangement, empty):
    N = variables.element_1
    Z = variables.element_2

    index_n = get(N,arrangement)
    index_z = get(Z, arrangement)

    #不必进一步操作，命运使然
    if left(index_n) == index_z or right(index_n) == index_z or up(index_n) == index_z or down(index_n) == index_z:
        pass

    #需要人定胜天
    else:
        plot = randint(1, 4)#1上2下3左4右

        Cheat = False

        while not Cheat:
            if plot == 1:#排在上面
                if index_n[1] - 1 >= 0 and arrangement[index_n[1] - 1][index_n[0]] != empty:
                    swap(index_n, index_z, arrangement, 1)
                    Cheat = True
                else:
                    plot += 1
            
            if plot == 2:#排在下面
                if index_n[1] + 1 < len(arrangement) and arrangement[index_n[1] + 1][index_n[0]] != empty:
                    swap(index_n, index_z, arrangement, 2)
                    Cheat = True
                else:
                    plot += 1
            
            if plot == 3:#排在左面
                if index_n[0] - 1 >= 0 and arrangement[index_n[1]][index_n[0] - 1] != empty:
                    swap(index_n, index_z, arrangement, 3)
                    Cheat = True
                else:
                    plot += 1
            
            if plot == 4:#排在右面
                if index_n[0] + 1 < len(arrangement[0]) and arrangement[index_n[1]][index_n[0] + 1] != empty:
                    swap(index_n, index_z, arrangement, 4)
                    Cheat = True
                else:
                    plot = 1
    
    return(arrangement)