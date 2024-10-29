# n皇后问题
from copy import deepcopy
from time import time


# 初始化参数
n = 6 # 行列数
board = [] # 声明一个棋盘
all_queens_pos = [] # 所有皇后的位置
max_queens = 0


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
    """主递归"""
    # global all_resolve
    global max_queens

    # 有无空位
    empty_list = get_empty_list(table)

    if len(empty_list) == 0: # 无空位
        if num > max_queens:
            max_queens = num
            # all_resolve = []
            # all_resolve.append(table)
        # elif num == max_queens:
        #     all_resolve.append(table)
        return

    else: # 有空位
        checktable = deepcopy(table)
        for empty in empty_list:
            table[empty[0]][empty[1]] = num + 1
            table = queen_range_update(empty[0], empty[1], deepcopy(table))
            # show_board(table)
            n_queen(deepcopy(table), num + 1)
            table = deepcopy(checktable)

    return
        
board = build_board(n)

begin = time()
n_queen(board)
print(time() - begin)

# print(len(all_resolve))
# for i in all_resolve:
#     show_board(i)
# show_board(all_resolve[0])

print("最多皇后数：", max_queens)