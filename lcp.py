# We recursively divide our array into two parts and find longest postfix in the left and right parts.
# We then find longest postfix of the longest postfixes of the left and right parts.

# We are going to have n - 1 comparisons in total.
# Comparison is accomplished in the following way: We select the smallest word out of two, and we compare it to the
# postfix of the lager word moving to the end of the smaller word until we find a match. In the best case this function
# time complexity is O(1). In the worst case this function complexity is m = min(length(word1),length(word2)) O(m).

# So in total, in the best case we will have O(n) time complexity, and O(n*m) in the worst case.

def longestCommonPostfixTwo(string1,string2):

    postfix = ''
    string1Len = len(string1)
    string2Len = len(string2)

    if string2 < string1:
        temp = string1
        string1 = string2
        string2 = temp
        string1Len = len(string1)
        string2Len = len(string2)

    for i in range(0,string1Len):
        if(string1[i:string1Len] == string2[string2Len - string1Len + i : string2Len]):
            postfix = string1[i:string1Len]
            break

    return postfix

def longestCommonPostfixHelper(list,low,high):

    if (high - low) == 1:
        return longestCommonPostfixTwo(list[low],list[high])
    elif high == low:
        return list[low]

    mid = (low + high) // 2

    postfixLeft = longestCommonPostfixHelper(list,low,mid)
    postfixRight = longestCommonPostfixHelper(list,mid+1,high)
    return longestCommonPostfixTwo(postfixLeft,postfixRight)

def longest_common_postfix(list):
    return longestCommonPostfixHelper(list,0,len(list)-1)

list1 = ['absorptivity', 'circularity', 'electricity', 'importunity', 'humanity']
list2 = ['bash', 'trash', 'backslash','flash']
list3 = ['absorptivity', 'circularity', 'electricity', 'importunity', 'humanity']
print(longest_common_postfix(list1))
print(longest_common_postfix(list2))
print(longest_common_postfix(list3))