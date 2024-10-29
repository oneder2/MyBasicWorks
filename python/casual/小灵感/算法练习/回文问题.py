import random
import math

nums = []

doubles = []
single = -1

for i in range(10):
    nums.append(random.randint(0,3))

print(nums)

for num in range(0, len(nums)):
    for i in range(0, len(nums)):
        if nums[i] == nums[num]:
            doubles.append(nums.pop(num))
            break
    if single == -1:
        single = nums.pop(num)
 
print(doubles, single)