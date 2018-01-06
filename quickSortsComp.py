# Lomuto partition is generally easier to understand and implement, rather then Hoare partition.
# Number of comparisons are the same, n - 1 for both, but Lomuto algorithm tends to do much more swaps then Hoare
# partition. So Hoare partition algorithm in general gives better performance.

def quickSortHoare(arr):
    quickSort(arr, 0, len(arr)-1,hoarePartition)

def quickSortLomuto(arr):
    quickSort(arr, 0, len(arr)-1,lomutoPartition)

def hoarePartition(arr,low,high):
    swaps = 0
    pivotValue = arr[low]
    right = low - 1
    left = high + 1
    while right < left:
        right += 1
        while arr[right] < pivotValue: right += 1

        left -= 1
        while arr[left] > pivotValue: left -= 1

        if right < left:
            swap(arr,left,right)
            swaps += 1

    swap(arr,low,left)

    return left

def lomutoPartition(arr,low,high):
    swaps = 0
    pivotValue = arr[low]
    s = low
    for i in range(low,high+1):
        if arr[i] < pivotValue:
            s += 1
            swap(arr,s,i)
            swaps += 1

    swap(arr,low,s)

    return s

def quickSort(arr,low,high,partionFunction):
    if low < high:
        pivot = partionFunction(arr,low,high)
        quickSort(arr,low,pivot-1,partionFunction)
        quickSort(arr,pivot+1,high,partionFunction)

def swap(arr,left,right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp

arr = [15,4,68,24,75,16,42]
quickSortHoare(arr)
print(arr)
#Output: [4, 15, 16, 24, 42, 68, 75]

arr = [15,4,68,24,75,16,42]
quickSortLomuto(arr)
print(arr)
#Output: [4, 15, 16, 24, 42, 68, 75]

arr = [0,0,0,0,0,0,0,0,0]
quickSortHoare(arr)
print(arr)

arr = [0,0,0,0,0,0,0,0,0]
quickSortLomuto(arr)
print(arr)
