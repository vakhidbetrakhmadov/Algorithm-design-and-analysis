mapOfGTU1 = {1 : [2,3],
            2 : [1,3],
            3 : [1,2]}

mapOfGTU2 = {1 : [2,3],
            2 : [1,3,4],
            3 : [1,2,4],
            4 : [3,2],
            5 : [6],
            6 : [5]}

otherMap = {0 : [1,3,4],
            1 : [0,3,4],
            2 : [0,5,6],
            3 : [0,1,4],
            4 : [0,1,3],
            5 : [2,6],
            6 : [2,5]}

def depthFirstSearch(graph):
    nodes = graph.keys()
    visited = dict.fromkeys(nodes, False)
    parent = dict.fromkeys(nodes, -1)
    for node in nodes:
        if not visited[node]:
            depthFirstSearchHelper(node, graph, visited, parent)
    return parent

def depthFirstSearchHelper(current, graph, visited, parent):
    visited[current] = True
    adjacentNodes = graph[current]
    for nextNode in adjacentNodes:
        if not visited[nextNode]:
            parent[nextNode] = current
            depthFirstSearchHelper(nextNode, graph, visited, parent)

def findMinimumCostToLabifyGTU(labCost, roadCost, map):
    departments = map.keys()
    numberOfDepartments = len(departments)
    returnValue = 0
    if labCost < roadCost:
        returnValue = labCost * numberOfDepartments
    else:
        newMap = depthFirstSearch(map)
        for department in newMap:
            if newMap[department] == -1:
                returnValue += labCost
            else:
                returnValue += roadCost
    return returnValue


minCost1 = findMinimumCostToLabifyGTU(2,1,mapOfGTU1)
print (minCost1)
minCost2 = findMinimumCostToLabifyGTU(5,2,mapOfGTU2)
print (minCost2)