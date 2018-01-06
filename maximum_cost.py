# If the max sum for the i-th element is Fi (i starts from 1), we then have two such sums,
# Fi_one, when i-th element is 1, and Fi_self when i-th element is itself.
# Therefore we have a 2*n DP table (where n is len(Y), that stores Fi_one and Fi_self for each element of the array Y.
# Initially only the first column of the DP table is known, and both entries in it are zeros,
# that is F0_one = 0, F0_self = 0.
# In order to find F1_one we need to consider two cases, when previous element is one and when it is itself.
# So F1_one = max(abs(1-1) + F0_one
# , abs(1-Y[0]) + F0_self)
# The same thing applies for the F1_self
# And F1_self then is max(abs(Y[1]-1) + F0_one, abs(Y[1] - Y[0]) + F0_self)
# This formulas are generalize for i below in the code (i starts from 1)
# Finally when we finish we just need to choose max between Fi_one and Fi_self

# Each Fi is found in constant time, we have to find 2*(len(Y)-1) such Fi in any circumstances
# So both in the worst and the best case this algorithm time complexity is going to be O(n) = 2*(n-1)
# That is O(n) = n

def find_maximum_cost(Y):
    length = len(Y)
    DPTable = [[0] * length for i in range(2)]

    for i in range(1, length):
        Fi_one = max(DPTable[0][i-1], abs(1-Y[i-1])+DPTable[1][i-1])
        Fi_self = max(abs(Y[i]-1)+DPTable[0][i-1], abs(Y[i]-Y[i-1])+DPTable[1][i-1])
        DPTable[0][i] = Fi_one
        DPTable[1][i] = Fi_self

    return max(DPTable[0][length-1], DPTable[1][length-1])


Y = [14,1,14,1,14]
cost = find_maximum_cost(Y)
print(cost)
# Output: 52

Y = [1,9,11,7,3]
cost = find_maximum_cost(Y)
print(cost)
#Output: 28

Y = [50,28,1,1,13,7]
cost = find_maximum_cost(Y)
print(cost)
#Output: 78

Y = [80,22,45,11,67,67,74,91,4,35,34,65,80,21,95,1,52,25,31,2,53]
cost = find_maximum_cost(Y)
print(cost)
#Output: 1107

Y = [79, 6,40, 68, 68, 16, 40, 63, 93,49, 91]
cost = find_maximum_cost(Y)
print(cost)
#Output: 642