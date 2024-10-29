s = "eleetminicoworoep"

# 元音
vowels = ["a", "e", "i", "o", "u"]

# 所有的元音对段落长度
pairs = []

lenPairs = len(pairs)

# 将一段元音对区间表达并存储到列表中
for l in range(0, len(s)):
    if s[l] in vowels:
        for r in range(l+1, len(s)):
            if s[r] == s[l]:
                pairs.append([l, r])
                break

# 如果元音对列表长度为0或1，则直接返回字符串长度
if lenPairs == 0 or lenPairs == 1:
    print(lenPairs)

print(pairs)

# 除去存在重叠区间的元音对
for up in range(len(pairs)):
    for off in range(up, len(pairs)):
        if (pairs[up][0] - pairs[off][0]) * (pairs[up][0] - pairs[off][1]) < 0 or (pairs[up][1] - pairs[off][0]) * (pairs[up][1] - pairs[off][1]) < 0:
            pairs.pop(up)
            pairs.pop(off - 1)
            break

print(pairs)

# 将辅音计入进元音字符串中
for pair in pairs:
    l, r = pair[0], pair[1]
    while l-1 > 0 and not s[l-1] in vowels:
        l -= 1
    while r+1 < len(s) and not s[r+1] in vowels:
        r += 1
    pair[0], pair[1] = l, r

# 比较长度
pairLength = []
for pair in pairs:
    pairLength.append(pair[1] - pair[0] + 1)

# 输出最大值
print(max(pairLength))
