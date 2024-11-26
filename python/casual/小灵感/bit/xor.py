def has_duplicates(data):
    xor_result = 0
    print(xor_result)
    for num in data:
        xor_result ^= num  # 对每个元素进行异或运算
        print(xor_result)

    # 如果结果为 0，说明有重复元素
    return xor_result == 0

# 示例
data1 = [1, 2, 3, 4, 5]  # 没有重复
data2 = [1, 2, 3, 4, 5, 2]  # 有重复

print(has_duplicates(data1))  # 输出: False
print(has_duplicates(data2))  # 输出: True

