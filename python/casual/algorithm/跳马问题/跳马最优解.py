# 找出给定起始与终止点的跳马最优解——深度查找改
# 初始化棋盘格
n = 8
maxsteps = n**2 - 1

x0, y0 = 0, 0
xt, yt = n-1, n-1

table = []
all_best_resolve = []

for y in range(n):
    table.append([])
    for x in range(n):
        table[y].append(0)

table[x0][x0] = 2


def printlist(List):
    for i in List:
        print(i)
    print("\n")



def check_abalable(yn, xn, newy, newx, steps):
    """检测该步是否可行"""
    global table
    global all_best_resolve
    global maxsteps

    tempy = yn + newy
    tempx = xn + newx
    
    if tempy < 0 or tempy >= n or tempx < 0 or tempx >= n:
        return
    
    if abs(newx) == abs(newy):
        return
    
    if table[tempy][tempx] == 0:
        """更新棋盘状态"""
        checkmap = []
        for y in table:
            checkmap.append(list.copy(y))

        if maxsteps > steps:
            steps += 1
        else:
            return

        table[yn][xn] = steps
        table[tempy][tempx] = steps + 1
        jump_horse(tempy, tempx, steps)
        table = list.copy(checkmap)
    return


def jump_horse(y = 0, x = 0, steps = 0):
    """主递归"""
    global maxsteps
    global all_best_resolve

    # 终止检测
    if table[yt][xt] == steps + 1:

        # print("[—ok—]")
        # printlist(table)
        
        if maxsteps > steps:
            maxsteps = steps
            all_best_resolve = []
        
        all_best_resolve.append(table)
        return

    # 可行性检测
    for xi in [-2, -1, 1, 2]:
        for yi in [-2, -1, 1, 2]:
            check_abalable(y, x, yi, xi, steps)
    return


jump_horse()

for best_resolve in all_best_resolve:
    printlist(best_resolve)

if len(all_best_resolve) == 0:
    maxsteps = 0

print("最优解个数：", len(all_best_resolve))
print("最大步数：", maxsteps)