def binarySearch(nums, target):
    i = 0
    j = len(nums) - 1

    while i != target and j != target:
        mid = (i + j) // 2
        if nums[mid] > target:
            j = mid
        elif nums[mid] < target:
            i = mid
        else:
            return mid
    
    return mid


numList = []
for i in range(100):
    numList.append(i)
targ = 44

print(binarySearch(numList, targ))

