import time


#冒泡排序
def bubblesort(arr):
    """冒泡排序bubble sorting"""
    n = len(arr)
    for a in range(n):
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

#选择排序
def selectsort(arr):
    """选择排序select sorting"""
    n = len(arr)
    for a in range(n):
        minIndex = a
        for i in range(a, n):
            if arr[i] < arr[minIndex]:
                minIndex = i
        arr[a], arr[minIndex] = arr[minIndex], arr[a]
    return arr

#原理未知的选择排序
def selectsort_1(arr):
    """选择排序select sorting"""
    n = len(arr)
    for c in range(n):
        for b in range(n):
            for a in range(b, -1, -1):
                if arr[b] < arr[a]:
                    arr[b], arr[a] = arr[a], arr[b]
        # print(arr)
    return arr

#插入排序
def insertsort(arr):
    """插入排序insert sorting"""
    n = len(arr)
    for i in range(1, n):
        x = arr[i]
        j = i - 1
        while j >= 0:
            if x <= arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            else:
                break
        arr[j+1] = x
    return arr

#归并排序
def merge(a, begin, mid, end):
    """合并数组"""
    temp = []
    l, r = begin, mid + 1
    while l <= mid and r <= end:
        if a[l] <= a[r]:
            temp.append(a[l])
            l += 1
        else:
            temp.append(a[r])
            r += 1
    temp.extend(a[l:mid+1])
    temp.extend(a[r:end+1])
    for i in range(begin, end+1):
        a[i] = temp[i - begin]
    # print(arr)
    # return a

def mergesort(arr, begin, end):
    """归并排序merge sorting"""
    if begin == end:
        return 
    mid = (begin + end) // 2
    mergesort(arr, begin, mid)
    mergesort(arr, mid + 1, end)
    merge(arr, begin, mid, end)
    
#快速排序
def quicksortpivot(a, begin, end):
    """找到基准数"""
    pivot = begin
    j = begin + 1
    for i in range(begin, end + 1):
        if a[i] < a[pivot]:
            a[i], a[j] = a[j], a[i]
            j += 1
    a[pivot], a[j-1] = a[j-1], a[pivot]
    pivot = j - 1
    return pivot

def quicksort(a, begin, end):
    """快速排序quick sorting"""
    if begin >= end:
        return
    pivot = quicksortpivot(a, begin, end)
    quicksort(a, begin, pivot - 1)
    quicksort(a, pivot + 1, end)

#堆排序
def heapify(heap, begin, end):
    """堆化"""
    son = begin * 2 + 1
    while son <= end:
        if son + 1 <= end and heap[son + 1] > heap[son]:
            son += 1
        if heap[son] > heap[begin]:
            heap[begin], heap[son] = heap[son], heap[begin]
            begin, son = son, son * 2 + 1
        else:
            break

def heapsort(a):
    """堆排序heap sorting"""
    l = len(a)
    for i in range(l // 2, -1, -1):
        heapify(a, i, l - 1)
    for i in range(l - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, 0, i - 1)
    # return a


#简易测试数组
arr = [5, 9, 4, 8, 7, 6, 3, 1, 0, 2]

# #复杂测试数组
# arr= []
# for i in range(1000, -1, -1):
#     arr.append(i)

# 1000个元素倒序转正序耗时一览：
# 气泡：0.44
# 选择：0.12
# 插入：0.22
# 归并：0.02
# 快速：
# 堆：0.01
# python3自带sort()函数：0.0 （小于0.001）

timestart = time.time()

heapsort(arr)
# arr.sort()

timeend = time.time()

# print(arr)
spend = str(timeend - timestart)
print("程序运行耗时：" + spend)