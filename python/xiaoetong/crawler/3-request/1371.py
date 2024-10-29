s = "leetcodeisgreat"

# 元音
vowels = ["a", "e", "i", "o", "u"]

# 所有的元音对段落长度
pairs = []
pairsLength = []

# 将一段元音对区间表达并存储到列表中
for l in range(0, len(s)):
    if s[l] in vowels:
        for r in range(l+1, len(s)):
            if s[r] == s[l]:
                pairs.append((l, r))
                break

# 创建储存区间长度的length表
for i in pairs:
    pairsLength.append(i[1] - i[0] + 1)

# 按照区间长度从长到短排序
for i in range(len(pairsLength)):
    maxNumIndex = i
    for a in range(i, len(pairsLength)):
        if pairsLength[a] > pairsLength[maxNumIndex]:
            maxNumIndex = a
    pairsLength[i], pairsLength[maxNumIndex] = pairsLength[maxNumIndex], pairsLength[i]
    pairs[i], pairs[maxNumIndex] = pairs[maxNumIndex], pairs[i]


for up in range(len(pairs)):
    upLength = pairs[up][1] - pairs[up][0] + 1
    # 遍历列表，查看检测是否满足条件
    flag = True
    for off in range(up, len(pairs)):
        # 若子字符串不包含于父字符串，子字符串左右边界与父字符串左右边界之差之积小于零
        if (pairs[up][0] - pairs[off][0]) * (pairs[up][0] - pairs[off][1]) < 0 or (pairs[up][1] - pairs[off][0]) * (pairs[up][1] - pairs[off][1]) < 0:
            flag = False
            break
        # 其余情况正常
    if flag:
        print(upLength)
        break


    # 最终检测是否满足


print(pairs)
print(pairsLength)

