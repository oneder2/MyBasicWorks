import time
import math

rlim = 10000000 # 搜索范围

primaries = []


def tough(output, n):
    for a in range(2, n): # 遍历范围

        if a % 2 == 0: # 是偶数直接跳过
            if a == 2:
                output.append(a)
            continue

        mark = True # 除数标记

        for b in range(3, a//2, 2): # 遍历比a小的奇数
            if a % b == 0: # a能被b整除
                mark = False # 标记
                break # 不是质数，跳出循环

        if mark:
            output.append(a)

def func_get_prime(n):
    return list(filter(lambda x: not [x%i for i in range(2, int(math.sqrt(x))+1) if x%i ==0], range(2,n+1)))


begin = time.time()

print (func_get_prime(rlim))

print(time.time() - begin)

# print(len(primaries))

