
This repo contains my implementaions of some of the most famuous algorithms.

--- TOHtime: ---

 Consider the problem of finding required time to finish Tower of Hanoi problem with optimal number of moves recursively. The time takes to move a disk is calculated as the weight of a disk (n) multiplied by the distance between the source and destination pegs (can be 1 or 2). For example, to move disk 2 from peg 1 to peg 3 takes 2*2=4 seconds. Design and implement a Python 3 function that simulates the gameplay by printing each move to console, and at last, prints the total elapsed time for moving each disk separately.

Example output:

Input size is 3:
disk 1: SRC to DST 
disk 2: SRC to AUX 
disk 1: DST to AUX 
disk 3: SRC to DST 
disk 1: AUX to SRC 
disk 2: AUX to DST 
disk 1: SRC to DST 
Elapsed time for disk 1: 6 
Elapsed time for disk 2: 4 
Elapsed time for disk 3: 6

--- findRottenWalnut ---

Consider the problem of finding rotten walnut. You have n walnuts and the weights of all walnuts are equal except the rotten one which is lighter than the others. Your input will be a python list of positive integers which indicates the weight of all walnuts; for example: [1 1 1 1 1 0.5 1 1 1]. Your output (return value of function) will be the index of the rotten walnut. To find the rotten walnut, you will use a pair of scales. The Python function which compares two set of walnuts is:
You will assume that this function executes in constant time (O (1)).

def compareScales (leftScaleList, rightScaleList):
    result = sum(leftScaleList) - sum(rightScaleList)
    if result < 0:
        return 1
    elif result > 0:
        return -1
    else:
        return 0
        
Using this function, design a recursive algorithm that finds the index of rotten walnut
faster than linear time(O(n)) in terms of asymptotic complexity.

--- assistantship ---

You have become the head of computer engineering department. You want to assign assistantship of each course to a R.A. (Research Assistant). To do this, you must consider skills of each R.A., some are good at Algorithms while some others may be expert at Operating Systems. According to his/her skills, an assistant may do the assistantship of a course more easily than the other ones.
Your input will be a 2-dimensional Python list of integers(table) with size n x r where n is number of courses and r is number of R.A.s (assume r >= n always). Inside the table, the element at table[i][j] has the meaning of assistant number i must spend table[i][j] hours for course j per week. Design and implement a brute force algorithm in Python 3 to find the optimal solution of minimizing the total time spent for course assistantship for the whole department. If number of courses (n) is less than the number of R.A.’s (r), unoccupied R.A.’s will do the other department tasks, each of which has a cost of 6 hours per week. Your function will return 2 things: first a 1-dimensional Python list of integers with size r, list[i] will hold the number of the course that R.A. i will be its assistant and -1 if it is doing another department stuff. The second return value is a single integer denoting the minimum total time spent per week.

Example:

    #Courses 0 1 2
inputTable = [ [5, 8, 7], # R.A. 0
                      [8,12,7], #R.A.1
                      [4,8, 5] ] #R.A.2
asst, time = findOptimalAssistantship(inputTable)
print(asst)
print(time)
Output:
[1, 2, 0] #R.A. 0 is assigned to course 1 etc.
19 # Minimum total time

--- labify ---

The rector of Gebze Technical University believes that every department of the university should have access to a computer lab. Unfortunately, GTU was hit by a flood that destroyed all of its computer labs and obstructed its roads! As you are the greatest programmer of GTU, the rector wants your help to repair the roads and build some new computer labs efficiently.
GTU has n departments numbered from 1 to n. The departments are connected by m bidirectional roads. Students of a department have access to a computer lab if:
• Their department contains a computer lab.
• They can travel by roads from their department to another department containing a computer lab.
The cost of repairing any road is x liras, and the cost to build a computer lab in any city is y liras. Design an algorithm (not brute force) and implement in Python 3 to find the minimum cost of making computer labs accessible to all the students. Inputs of your function will be x (the cost to build a computer lab), y (the cost to repair a road), mapOfGtu (graph that represents GTU). The graph will be a python dictionary (a data structure in python, hash map), its keys will be integers denoting vertex number and its values will be python sets (another data structure in python) that holds other vertex numbers which are connected to the key vertex. Therefore, the graph is represented as an adjacency list.
Cost of building a lab is 2 and repairing a road is 1. There are 3 departments and 3 roads. The optimal solution is to build a lab at any of the departments (cost 2) and repair 2 roads (cost 1 x 2 = 2). Hence, the minimum total cost is 4. Solution is represented by the graph above.

Example:

mapOfGTU = {
                        1 : set([2,3]),
                        2 : set([1,3]),
                        3 : set([1,2])
                        } # graph is initialized as dictionary
minCost = findMinimumCostToLabifyGTU(2,1,mapOfGTU)
print(minCost) # Output will be 4

--- subarray_finder ---

Your middle school math teacher has given you a list of positive and negative integers and wants from you to find the subarray that has minimum sum. For example, if the input is [1, -4, -7, 5, -13, 9, 23, -1], the subarray that gives the minimum sum is [-4, -7, 5, -13]. Design and implement a divide and conquer algorithm in Python 3 that returns the subarray with minimum sum. Explain your algorithm and do worst case analysis as a comment block at the beginning of your implementation file.

Example:

inpArr = [1, -4, -7, 5, -13, 9, 23, -1]
msa = min_subarray_finder(inpArr)
print(msa)
#Output: [-4, -7, 5, -13]
print(sum(msa))
#Output: -19

--- lcp ---

Your high school English teacher has given you a list of words (strings). Your mission is to find the longest common postfix of given words. Here is an example:
Your input: [“bash”, “trash”, “backslash”,” flash”]
Your output: “ash”
Your input: [“absorptivity”, “circularity”, “electricity”,” importunity”, “humanity”]
Your output: “ity”
Design and implement a divide and conquer algorithm to accomplish this task. Explain your algorithm and do worst case analysis as a comment block at the beginning of your implementation file.

Example:

inpStrings = ["absorptivity", "circularity”, "electricity", "importunity", "humanity"]
lcp = longest_common_postfix(inpStrings)
print(lcp)
#Output: ity

--- find_kth_book_1 ---

As you are a new computer engineering student, you want to have books for classes. You have friend that knows a friend that knows another friend who has n of the books you want, and he/she lent them to you in an alphabetically (a to z) sorted form. But you needed m more books and you bought them from a bookstore again in an alphabetically (a to z) sorted form. You don’t merge and sort them (m and n) alphabetically because the lent books must not be mixed with your own books. Assuming they are merged and sorted, you want to find the k th (starting from 1) book. Design and implement a decrease and conquer algorithm in Python 3 to accomplish this task in O (log n + log m) time (assume that comparing two strings is constant time). Explain your algorithm as a comment block at the beginning of your implementation file.

Example:

m = ["algotihm", "programminglanguages", "systemsprogramming"] n = ["computergraphics", "cprogramming", "oop"]
book = find_kth_book_1(m,n,4)
print(book)
#Output: programminglanguages
book = find_kth_book_1(m,n,6)
print(book)
#Output: systemsprogramming

--- quickSortsComp ---

In quicksort, both Lomuto’s and Hoare’s partition schemes can be used. Implement quick sort in Python 3 using both and compare the partition schemes. What are their advantages and disadvantages? Answer this question as a comment block at the
beginning of your implementation file.

Example:

arr = [15,4,68,24,75,16,42]
qsh = quickSortHoare(arr)
print(qsh)
#Output: [4, 15, 16, 24, 42, 68, 75]
qsl = quickSortLomuto(arr)
print(qsl)
#Output: [4, 15, 16, 24, 42, 68, 75]

--- maximum_cost ---

There are two unsigned integer lists X and Y with the same number of elements (N). The following relation exists among their ith elements:
𝟏≤𝑿𝒊 ≤𝒀𝒊
The cost (S) of a list X is defined as:
    𝑁
𝑆 = ∑ |𝑿𝒊 − 𝑿𝒊−𝟏|
    𝑖=2
Given a list Y, design and implement a dynamic programming algorithm in Python 3 that returns the maximum possible cost of list X.
Explain your algorithm and do worst case analysis as a comment block at the beginning of your implementation file.

Example:

Y = [14,1,14,1,14]
cost = find_maximum_cost(Y)
print(cost)
#Output: 52
Y = [1,9,11,7,3]
cost = find_maximum_cost(Y)
print(cost)
#Output: 28
Y = [50,28,1,1,13,7]
cost = find_maximum_cost(Y)
print(cost)
#Output: 78

--- theft ---

A large amount of money was given to you and to protect, you split and buried it in a land with n*m cells (dimension is n row m column). Each cell in the land contains a positive integer which is the number of Turkish liras buried. A thief has learned your secret and going to steal maximum amount of money before the cops arrive. Initially the thief is at first column but can be at any row. He can move only 1 cell right, right-up or right-down from a given cell. When the thief arrives a new cell, he steals the money.
Design and implement a dynamic programming algorithm in Python 3 to find out maximum amount of money he can steal when he reaches to the end (last column). Explain your algorithm and do worst case analysis as a comment block at the beginning of your implementation file.

Example:

amountOfMoneyInLand= [[1,3,1,5], [2,2,4,1], [5,0,2,3], [0,6,1,2]]
res = theft(amountOfMoneyInLand)
print(res)
#Output: 16
amountOfMoneyInLand= [[10,33,13,15], [22,21,4,1], [5,0,2,3], [0,6,14,2]]
res = theft(amountOfMoneyInLand)
print(res)
#Output: 83

--- decentNumber ---

A Decent Number having N digits has the following properties:
1. Its digits can only be 3's and/or 5's.
2. The number of 3's it contains is divisible by 5.
3. The number of 5's it contains is divisible by 3.
4. If there is more than one such number, we pick the largest one.
Design and implement a greedy algorithm to find the decent number having N digits. If there is not any decent number with N digits, return -1. Explain your algorithm and your greedy choice as a comment block at the beginning of your implementation file.

Example:

dn = decentNumber(1)
print(dn)
#Output: -1
dn = decentNumber(3)
print(dn)
#Output: 555
dn = decentNumber(5)
print(dn)
#Output: 33333
dn = decentNumber(11)
print(dn)
#Output: 55555533333
