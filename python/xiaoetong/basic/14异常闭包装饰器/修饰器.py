# 给已有的函数增加额外的功能，本质就是闭包
# several traits:
# 1. Original code
# 2. Original arranging way
# 3. Extra functions


import time

def get_time(a):
    def inner():
        # 开始计时
        start = time.time()
        # 程序
        a()
        # 结束计时
        end = time.time()
        print(f"一共花费了：{end - start}")
    return inner

# 从1输出到100000
@get_time
def print_num():
    # 用循环遍历输出
    for i in range(1, 10000 + 1):
        print(i)

print_num()

# 调用函数
# fn = get_time(print_num)
# fn()