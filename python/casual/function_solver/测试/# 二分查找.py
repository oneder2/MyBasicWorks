import time
# 二分查找
target = 0.6
upb, downb = 100, 0

while downb + 1 != upb: #二分查找
    mid = (upb + downb) // 2
    if target > mid:
        downb = mid
    else:
        upb = mid
    if mid == target:
        break

if target == downb or target == upb:
    print("这个数是整数")
else:
    print("这个数不是整数")
