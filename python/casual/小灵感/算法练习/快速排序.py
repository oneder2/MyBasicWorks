def pivotquicksort(a, start, end):
    pivot = start
    j = pivot + 1
    for i in range(j, end+1):
        if a[i] < a[pivot]:
            a[j], a[i] = a[i], a[j]
            j += 1
    a[pivot], a[j-1] = a[j-1], a[pivot]
    pivot = j-1
    return pivot

def quicksort(a, start, end):
    if start >= end:
        return
    pivot = pivotquicksort(a, start, end)
    quicksort(a, start, pivot - 1)
    quicksort(a, pivot + 1, end)

arr = [100]
for i in range(100, -1, -1):
    arr.append(i)

quicksort(arr, 0, len(arr) - 1)

print(arr)
