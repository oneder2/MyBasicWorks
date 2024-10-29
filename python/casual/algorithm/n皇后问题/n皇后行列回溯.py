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

board = build_board(n)
# show_board(board)

for y in range(len(board)):
    for x in range(len(y)):
        if board