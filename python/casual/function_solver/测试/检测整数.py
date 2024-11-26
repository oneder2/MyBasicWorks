import time

#绝对值
def abs(num):
    if num < 0:
        num = - num
    return num


#二分法整数检测（较复杂，但是精度无限）
def integraty(num):
    num = abs(num)
    upb, downb = 10, 0
    if num == 0: #边界检测
        return True
    while num > upb: #确立大致上下界
        upb *= 10
    while downb + 1 != upb: #二分查找
        
        mid = (upb + downb) // 2
        if num > mid:
            downb = mid
        else:
            upb = mid
        if mid == num:
            break

    if num == downb or num == upb:
        return True
    else:
        return False

#较为通用的整数检测（较简单，但是精度有限）
def general(num):
    num = float(num)
    bond = 10**-8
    differ = abs(num - int(num))
    if differ <= 10**-8:
        return True
    else:
        return False

starttime = time.time()
print(integraty(100000100000000000.1))
endtime = time.time()
spending = endtime - starttime
print(spending)

starttime = time.time()
print(general(100000100000000000.1))
endtime = time.time()
spending = endtime - starttime
print(spending)