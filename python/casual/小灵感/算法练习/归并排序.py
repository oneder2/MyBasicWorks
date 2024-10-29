def merge(arr, start, mid, end):
    temp = []
    l = start
    r = mid + 1
    while l <= mid and r <= end:
        if arr[l] < arr[r]:
            temp.append(arr[l])
            l += 1
        else:
            temp.append(arr[r])
            r += 1
    temp.extend(arr[l:mid+1])
    temp.extend(arr[r:end+1])
    for i in range(start, end+1):
        arr[i] = temp[i - start]


def mergesort(arr, start, end):
    # print(arr)
    if start >= end:
        return
    mid = (start + end) // 2
    mergesort(arr, start, mid)
    mergesort(arr, mid + 1, end)
    merge(arr, start, mid, end)

arr = [9,8,7,6,5,4,3,2,1]
# arr.reverse()

mergesort(arr, 0, len(arr)-1)

print(arr)
