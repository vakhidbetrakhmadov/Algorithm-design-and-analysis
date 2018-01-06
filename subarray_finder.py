
# So the basic idea here is that we divide the array into two on each level of recursion,
# we find the min sub-array sum and its indexes in the left part (recursively), we find min sub-array and its indexes
# in the right side (recursively), and we find min sub-array and its indexes in the left and right parts such that it
# contains the mid point of the array (crossing sub-array). This last step is pretty much simple, we just start from
# the mid-point and move to the left and to the right keeping track of our min-left-sum and min-right-sum, each time
# when either min-left-sum or min-right-sum becomes less we update our left and right indexes of min crossing sub-array.
# This is done in linear time ( O(n) ).
# At the end we just compare the result from the left part, right part and crossing part and chose the least one.

# The best and the worst cases for this algorithm are the same.
# Recurrence relation for this algorithm can be expressed as T(n) = 2T(n/2) + O(n)
# According to the Master theorem:
# a = 2, b = 2, f(n) = n
# n^(logb(a)) = n^(log2(2)) = n^1 = Teta(n)
# f(n) <=> Teta(n^(logb(a))), f(n) <=> Teta(n), second rule

# So T(n) = Teta(n log(n))


INT_MAX = 99999999

def minCrossingSum(array,low,mid,high):
    leftSum = INT_MAX
    rightSum = INT_MAX

    sum = 0
    subLow = mid
    for i in range(mid,low,-1):
        sum += array[i]
        if sum < leftSum:
            leftSum = sum
            subLow = i

    sum = 0
    subHigh = mid+1
    for i in range(mid+1,high):
        sum += array[i]
        if sum < rightSum:
            rightSum = sum
            subHigh = i

    return leftSum + rightSum, subLow, subHigh

def minSubArraySumHelper(array,low,high):
    if low == high:
        return array[high],low,high

    mid = (low + high) // 2

    min1, subLow1, subHigh1 = minSubArraySumHelper(array,low,mid)
    min2, subLow2, subHigh2 = minSubArraySumHelper(array,mid+1,high)
    min3, subLow3, subHigh3 = minCrossingSum(array,low,mid,high)

    minValue = min(min1, min2,min3)

    if minValue == min1:
        return minValue, subLow1, subHigh1
    elif minValue == min2:
        return minValue, subLow2, subHigh2

    return minValue, subLow3, subHigh3

def min_subarray_finder(array):
    minValue, subLow, subHigh = minSubArraySumHelper(array,0,len(array)-1)
    return array[subLow:subHigh+1]

array = [1, -4, -7, 5, -13, 9, 23, -1]
result = min_subarray_finder(array)
print(result)