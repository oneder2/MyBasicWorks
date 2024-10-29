# 新解
import time
import copy


# 初始化
n = 10
x0, y0 = 0, 0
xn, yn = n-1, n-1
max_steps = n ** 2

table = []
all_resolve = []
choices = [[2, 1], [-2, 1], [2, -1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]

# 构建棋盘
def build_board(n):
    board = []
    for i in range(n):
        board.append([])
        for j in range(n):
            board[i].append(-1)
    return board


def show_table(table):
    """输出棋盘"""
    for row in table:
        print(row)
    print("\n")


def jump_horse(x = x0, y = y0, step = 0):
    """主递归"""
    global max_steps
    global all_resolve
    # show_table(table)

    # 检测是否超出步数
    if step > max_steps:
        return

    # 检测是否超出范围
    if x < 0 or x >= n or y < 0 or y >= n:
        return

    # 检测终止
    if x == xn and y == yn:
        if step < max_steps:
            max_steps = step
            all_resolve = []
        all_resolve.append(copy.deepcopy(table))
        # print("[——ok——]")
        return

    # 进行下一步
    for delta in choices:
        if table[y][x] == -1:
            table[y][x] = step + 1
            jump_horse(x + delta[0], y + delta[1], step + 1)
            table[y][x] = -1
    return



table = build_board(n)
# show_table(table)


# begin = time.time()
jump_horse()
# end = time.time() - begin

# for i in all_resolve:
#     show_table(i)

print("运行完毕")
# print("耗时：", end)

print("最优解个数：", len(all_resolve))
print("最优解所需要步数：", max_steps)
