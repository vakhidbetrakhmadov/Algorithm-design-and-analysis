# We have a DP table, where each cell stores max amount of money that can be stolen when the thief arrives at the
# corresponding cell on the land.
# Initially only values of the cells in first column in the DP table are known. Other can be calculated as follows:
# If we define max amount of money that thief can still when he arrives at some particular cell on the land as Fij
# (where i and j start from 1), then Fij = max(money_ij + Fij-1,money_ij + Fi-1j-1,money_ij + Fi+1j-1).
# Thus we find all Fij
# Finally we just find max among Fij where j=m-1.

# Each Fij is found in constant time, we have to find n*m-n such Fij in any circumstances
# So both in the worst and the best case this algorithm time complexity is going to be O(n) = n*m-n
# That is O(n) = n*m, assuming that n=m that is O(n) = n^2

def theft(amountOfMoneyInLand):
    rows = len(amountOfMoneyInLand)
    cols = len(amountOfMoneyInLand[0])
    DPTable = [[0] * cols for i in range(rows)]
    maxMoney = 0

    for i in range(0,rows):
        DPTable[i][0] = amountOfMoneyInLand[i][0]

    for j in range(1,cols):
        for i in range(0, rows):
            fillInDPTable(i, j, DPTable, amountOfMoneyInLand)

    maxMoney = DPTableMax(cols-1, DPTable)

    return maxMoney

def fillInDPTable(row,col,DPTable,amountOfMoneyInLand):
    rows = len(amountOfMoneyInLand)
    cols = len(amountOfMoneyInLand[0])
    v1 = 0 if not isInBounds(row,col-1,rows,cols) else (amountOfMoneyInLand[row][col] + DPTable[row][col-1])
    v2 = 0 if not isInBounds(row-1,col-1,rows,cols) else (amountOfMoneyInLand[row][col] + DPTable[row-1][col-1])
    v3 = 0 if not isInBounds(row+1,col-1,rows,cols) else (amountOfMoneyInLand[row][col] + DPTable[row+1][col-1])
    DPTable[row][col] = max(v1,v2,v3)

def isInBounds(row,col,rows,cols):
    return (row >= 0 and row < rows and col >= 0 and col < cols)

def DPTableMax(col,DPTable):
    maxValue = 0
    rows = len(DPTable)
    for i in range(0,rows):
        maxValue = DPTable[i][col] if DPTable[i][col] > maxValue else maxValue
    return  maxValue


amountOfMoneyInLand = [[1,3,1,5], [2,2,4,1], [5,0,2,3], [0,6,1,2]]
res = theft(amountOfMoneyInLand)
print(res)
# Output: 16
amountOfMoneyInLand = [[10, 33, 13, 15], [22, 21, 4, 1], [5, 0, 2, 3], [0, 6, 14, 2]]
res = theft(amountOfMoneyInLand)
print(res)
# Output: 83