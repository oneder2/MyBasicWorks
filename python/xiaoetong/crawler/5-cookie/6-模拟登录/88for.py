nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,3,6]
n = 3

for i in range(n):
    nums1.pop(m)

for i in range(len(nums1)):
    midindex = 0
    for j in range(midindex, len(nums2)):
        if nums1[i] > nums2[j]:
            