s =  "abb"

maxRepeat = 1 # 最大的重复字符对
repeatIndex = 0 # 发现最大重复字符对对应的索引值
finalBias = 0 # 最大的重复字符对有多少个重复的字符

# 遍历字符串
for i in range(len(s)):
    repeat = 1 # 记录有几对重复的字符对
    bias = 0 # 记录连续的重复字符对

    # 发现左边的字符与当前索引对应字符值相等
    for y in range(i-1, -1, -1):
        if i - y - bias + 1 <= 0:
            break

        if s[i] == s[y]:
            bias += 1
            repeat += 1
        else:
            break

    # 遍历字符串两侧
    for x in range(1, len(s) - 1):
        # 边界检测
        if i - x - bias + 1 <= 0 or i + x >= len(s):
            break

        # 发现一致字符对就增加重复量
        if s[i + x] == s[i - x - bias]:
            repeat += 1
        # 存在不一致字符，直接退出
        else:
            break

    # 更新最大数对
    if maxRepeat < repeat:
        maxRepeat = repeat
        repeatIndex = i
        finalBias = bias

# 此时分为三种情况：
# 1. 该字符串正好是一个回文字符串，可以直接输出（回文中心在中间）
# 2. 回文中心在左侧
# 3. 回文中心在右侧

# 先看第一种（中间，正好回文）：
mid = False
if finalBias % 2 == 0:
    if s[repeatIndex:] == s[:repeatIndex + 1][::-1]:
        mid = True
else:
    if s[repeatIndex:] == s[:repeatIndex][::-1]:
        mid = True

if mid:
    print(s)
    exit()

print(maxRepeat)
print(repeatIndex)
print(finalBias)

# 再看第二种（中心在左侧）：
print(s[repeatIndex + maxRepeat - finalBias:])
print(s[repeatIndex + maxRepeat - finalBias:][::-1] + s)

