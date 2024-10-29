nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,3,6]
n = 3

for i in range(n):
    nums1.pop(m)

# 初始化指针
i = 0
j = 0

nums = []
# 指针到达极限之前循环
while not (i == m-1 and j == n-1):
    # nums1[i]较小对应值，不变
    if nums1[i] < nums2[j]:
        # nums1指针自增
        nums.append(nums1[i])
        if i < m-1:
            i += 1
    # nums2[i]指针对应值较小，将nums2[j]值
    elif nums1[i] >= nums2[j]:
        nums.append(nums2[j])
        if j < n-1:
            j += 1
else:
    if nums1[i] > nums2[j]:
        nums.append(nums2[j])
        nums.append(nums1[i])
    else:
        nums.append(nums1[i])
        nums.append(nums2[j])
        

print(nums)

