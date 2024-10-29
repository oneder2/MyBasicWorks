# 找出跳马的所有解
# 初始化棋盘格
n = 4
x0, y0 = 0, 0
xt, yt = 3, 3
table = []
resolve = []

for y in range(n):
    table.append([])
    for x in range(n):
        table[y].append(0)

table[x0][x0] = 2


def printlist(List):
    for i in List:
        print(i)


def check(yn, xn, newy, newx):
    """检测该步是否可行"""
    global table
    tempy = yn + newy
    tempx = xn + newx
    if tempy < 0 or tempy >= n or tempx < 0 or tempx >= n or abs(newx) == abs(newy):
        return
    else:
        if table[tempy][tempx] == 0:
            """更新棋盘状态"""
            checkmap = []
            for y in table:
                checkmap.append(list.copy(y))
            table[yn][xn] = 1
            table[tempy][tempx] = 2
            jump_horse(tempy, tempx)
            table = list.copy(checkmap)
        return


def jump_horse(y = 0, x = 0):
    """主递归"""
    global count
    global table

    # 终止检测
    if table[yt][xt] == 2:
        print("[—ok—]")
        printlist(table)
        print("\n")
        resolve.append(table)
        if not (table in resolve):
            count += 1
        return

    # 可行性检测
    for xi in [-2, -1, 1, 2]:
        for yi in [-2, -1, 1, 2]:
            check(y, x, yi, xi)
    return


# mark = False
jump_horse()

print(len(resolve))
