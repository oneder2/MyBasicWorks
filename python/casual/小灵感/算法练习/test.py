length = 10000000
nums = []
primaries = []

nums = [i for i in range(0,length + 1)]

index = 2
while index < length:
    if nums[index] != None:
        for i in range(index*2, length + 1, index):
            nums[i] = None
    index += 1

print(list(filter(lambda x: x != None, nums)))