
# Returns value: index of the rotten walnut
def findRottenWalnut(listOfNuts):
    lenListOfNuts = len(listOfNuts)
    if lenListOfNuts < 2:
        return -1
    return findRottenWalnutHelper(listOfNuts, 0, lenListOfNuts - 1)

def findRottenWalnutHelper(listOfNuts, low, high):
    if low == high:
        return low

    mid = (high + 1 + low) // 2         # calculate middle index
    even = ((high - low + 1) % 2) == 0  # check if the sublist size if even
    comparison = compareScales(listOfNuts[low : mid if even else mid + 1], listOfNuts[mid : high + 1])

    if comparison == 0:
        return -1 if (even or (not even and listOfNuts[mid] == listOfNuts[mid - 1])) else mid
    elif comparison == 1:
        return findRottenWalnutHelper(listOfNuts, low, mid - 1 if even else mid)
    else: # compareResult == -1
        return findRottenWalnutHelper(listOfNuts, mid, high)


def compareScales (leftScaleList, rightScaleList):
    result = sum(leftScaleList) - sum(rightScaleList)
    if result < 0:
        return 1
    elif result > 0:
        return -1
    else:
        return 0

print 'Rotten walnut is found at index: {0}'.format(findRottenWalnut([1,0.5,1,1]))
