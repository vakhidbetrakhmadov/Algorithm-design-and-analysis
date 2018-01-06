def find_kth_book_1(m, n, k):
    return findKthBook(m, 0, len(m)-1, n, 0, len(n)-1, k-1)

# We first find middle indexes in both arrays, mid1 and mid2.
# We then compare their sum (mid1+mid2) with k in order to figure out with which part (left or right)
# of both of the arrays to continue.
# If k is less or equal the sum of middle indexes(k <= mid1+mid2), then the k-th element is either in:
# 1) array1[low1..mid1-1] or array2[low2..high2] If array1[mid1] > array2[mid2]
# (we discard mid-element and all elements after it for array1,
# because they wouldn't be in the range if the arrays were merged and sorted)
# 2) array1[low1..high1] or array2[low2..mid2-1] If array1[mid1] <= array2[mid2]
# (we discard mid-element and all elements after it for array2,
# because they wouldn't be in the range if the arrays were merged and sorted)
# If k is more then the sum of middle indexes, then the k-th element is is either in:
# 1) array1[low1..high1] or array2[mid2+1..high2] If array1[mid1] > array2[mid2] (we discard mid-element for array2 and
# all the elements before mid-element, because they wouldn't be in the range if the arrays were merged and sorted),
# and we decrease k by the number of elements left on the left side of array2 because,
# if the the array have been merged and sorted, they would occupy positions before k-th element
# 2) array1[mid1+1..high1] or array2[low2..high2] If array1[mid1] <= array2[mid2](we discard mid-element for array1 and
# all the elements before mid-element, because they wouldn't be in the range if the arrays were merged and sorted),
# and we decrease k by the number of elements left on the left side of array1 because,
# if the the arrays have been merged and sorted, they would occupy positions before k-th element
# Finally if one of the array is empty, that is low? > high?, then the k-th element is array[k] of the non-empty array

def findKthBook(books1, low1, high1, books2, low2, high2, k):
    if low1 > high1:
        return books2[low2 + k]
    elif low2 > high2:
        return books1[low1 + k]

    mid1 = (high1 - low1 + 1) // 2
    mid2 = (high2 - low2 + 1) // 2

    if k <= mid1 + mid2:
        if (books1[low1 + mid1] > books2[low2 + mid2]):
            return findKthBook(books1,low1,low1+mid1-1,books2,low2,high2,k)
        else:
            return findKthBook(books1,low1,high2,books2,low2,low2+mid2-1,k)
    else: # k > mid1 + mid2
        if books1[low1 + mid1] > books2[low2 + mid2]:
            return findKthBook(books1, low1, high1, books2, low2+mid2+1, high2, k-mid2-1)
        else:
            return findKthBook(books1, low1+mid1+1, high1, books2, low2, high2, k-mid1-1)


m = ['algotihm', 'programminglanguages', 'systemsprogramming']
n = ['computergraphics', 'cprogramming','oop']

print(find_kth_book_1(m,n,1))
print(find_kth_book_1(m,n,2))
print(find_kth_book_1(m,n,3))
print(find_kth_book_1(m,n,4))
print(find_kth_book_1(m,n,5))
print(find_kth_book_1(m,n,6))

m = [1,3,5,7,9]
n = [2,4,6,8,10]

for i in range(1,11):
    print(find_kth_book_1(m, n, i))