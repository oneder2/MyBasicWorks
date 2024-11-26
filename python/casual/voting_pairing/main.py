# 男生与女生数量设置
boynum = int(input("男生个数："))
girlnum = int(input("女生个数："))


# 创造权重储二维表
weight = []

for g in range(girlnum):
    weight.append([])
    for b in range(boynum):
        weight[g].append(0)

# print(weight)

# 创造Ann全排列表
pair = []

for b in range(boynum):
    pair.append([])

# for g in range(girlnum):




for a in range(len(pair), 0, -1):
    mark = False
    for b in range(len[a]):
        if b in pair[a][b+1:]:
            mark = True
            break
        elif b == len(a) - 1:
            break
    if mark:
        del pair[a]

for order in range(len(pair)):
    for index in range(len(index)):
        added = added + weight[index][pair[order][index]]
    weight.append(added)

for mid in range
