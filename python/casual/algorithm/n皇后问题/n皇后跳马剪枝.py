# n皇后问题
from copy import deepcopy
from time import time
from math import ceil


# 初始化参数
n = 8 # 行列数
board = [] # 声明一个棋盘
all_resolve = []
all_queen_pos = []
max_queens = 0
jump_aim = ((2,1),(-2,1), (2,-1), (-2,-1), (1,2), (-1,2), (1,-2), (-1,-2))


def build_board(length):
    """初始化棋盘"""
    board = []
    for y in range(length):
        board.append([])
        for x in range(length):
            board[y].append(-1)
    return board

def show_board(board):
    """打印棋盘"""
    for i in board:
        print(i)
    print("\n")

def get_empty_list(board):
    """获取一个棋盘中的空位，以(y, x)元组形式储存在列表，并返回该列表"""
    empty_list_output = []
    # show_board(board)
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == -1:
                empty_list_output.append(deepcopy((y, x)))
    return empty_list_output

def get_horse_empty_list(board, y, x):
    """获取一个坐标下可跳马移动的空位，以(y, x)元组形式储存在列表，并返回该列表"""
    empty_horse_list_output = []
    # show_board(board)
    for alt in jump_aim:
        yt, xt = y + alt[0], x + alt[1]
        if xt < 0 or xt >= n or yt < 0 or yt >= n:
            continue
        if board[yt][xt] == -1:
            empty_horse_list_output.append((yt, xt))
    return empty_horse_list_output

def queen_range_update(y, x, board):
    """更新给定皇后的射程范围"""
    # 横着
    for i in range(n):
        # print(y, x, i)
        if board[y][i] == -1:
            board[y][i] = 0
    
    # 竖着
    for i in range(n):
        if board[i][x] == -1:
            board[i][x] = 0
    
    y0, x0 = y, x
    # 向左上
    while y0 > 0 and x0 > 0:
        y0 -= 1
        x0 -= 1
        if board[y0][x0] == -1:
            board[y0][x0] = 0
    
    y0, x0 = y, x
    # 向右上
    while y0 > 0 and x0 < n-1:
        y0 -= 1
        x0 += 1
        if board[y0][x0] == -1:
            board[y0][x0] = 0
    
    y0, x0 = y, x
    # 向左下
    while y0 < n-1 and x0 > 0:
        y0 += 1
        x0 -= 1
        if board[y0][x0] == -1:
            board[y0][x0] = 0
    
    y0, x0 = y, x
    # 向右下
    while y0 < n-1 and x0 < n-1:
        y0 += 1
        x0 += 1
        if board[y0][x0] == -1:
            board[y0][x0] = 0

    return board

def n_queen(table, num = 0):
    global all_queen_pos
    global all_resolve
    global max_queens

    """主递归"""
    # 获取空位
    empty_list = get_empty_list(table)

    if len(empty_list) == 0:
        """终止检测，无空时返回"""
        if num > max_queens:
            max_queens = num
            all_resolve.append(table)

        return

    # 还有空，继续逼近
    empty_list = []
    if len(all_queen_pos) == 0 :
        """没有皇后，八分之一棋盘剪枝"""
        for y in range(ceil(len(table) / 2)):
            for x in range(y, ceil(len(table[0]) / 2)):
                empty_list.append((y, x))

    elif len(all_queen_pos) != 0:
        """已有皇后"""
        for yq, xq in all_queen_pos:
            """将皇后遍历查找跳马位点，获取空位"""
            empty_list = empty_list + get_horse_empty_list(table, yq, xq)

        if len(empty_list) == 0:
            """如果没有可跳马位点，获取空位"""
            empty_list = deepcopy(get_empty_list(table))

    # 保存棋盘状态
    checktable = deepcopy(table)
    for empty in empty_list:
        """遍历空位"""
        if table[empty[0]][empty[1]] == -1:
            table[empty[0]][empty[1]] = num + 1 # 更新新皇后位置
            table = deepcopy(queen_range_update(empty[0], empty[1], table)) # 更新可放置位置
            all_queen_pos.append((empty[0], empty[1]))
            n_queen(table, num + 1) # 递归新棋盘
            all_queen_pos.pop()
            table = deepcopy(checktable) # 恢复原有状态


board = build_board(n)

begin = time()
n_queen(board)
print(time() - begin)

# print(len(all_resolve))
for i in all_resolve:
    show_board(i)
# show_board(all_resolve[0])

print("最多皇后数：", max_queens)