#绝对值
def abs(num):
    if num < 0:
        num = - num
    return num

#正数检测
def posi(num):
    if num > 0:
        return True
    else:
        return False

#整数检测
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