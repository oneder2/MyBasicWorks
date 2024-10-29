nums = [1,2,3,4]
# Initialize params
maxNum = 0
maxLength = 0

# Find biggest number and index
currentLength = 0
for i in range(0, len(nums)):
    # break currentLength
    if maxNum > nums[i]:
        currentLength = 0

    # update maxNum
    elif maxNum < nums[i]:
        maxNum = nums[i]
        maxLength = 1 
        currentLength = 1 # reset
    
    # longer the length
    else:
        currentLength += 1
    
    if maxLength < currentLength:
        maxLength = currentLength

print(maxLength)