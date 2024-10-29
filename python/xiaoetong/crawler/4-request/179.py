nums = [3,30,34,5,9]
stringNums = []

# 字符串化
for num in nums:
    stringNums.append(str(num))

# 找出最长的字符长度
longestLength = 0
for i in stringNums:
    if len(i)>longestLength:
        longestLength = len(i)

# 补零数表初始化
zeroNums = []
for i in range(len(nums)):
    zeroNums.append(0)

stringNums.sort(reverse=True)

print(stringNums)

# 补零
for i in range(len(stringNums)):
    while len(stringNums[i]) < longestLength:
        stringNums[i] += "0"
        zeroNums[i] += 1

# 
for i in range(len(stringNums)):
    stringNums[i] = stringNums[i][0:len(stringNums[i]) - zeroNums[i]]

altimate = ""

for i in stringNums:
    altimate = altimate + i

print(zeroNums)
print(stringNums)
print(longestLength)
print(altimate)
