from search import *
from equationsimplier import *
from heuristic import *

# problemTree = problemCreator()

# for node in problemTree.Nodes:
#     print(node.data)

def sumHVisited(tree):
    sum = 0
    for i in tree.Nodes:
        sum = sum + int(not i.hVisited)
    return sum

def createHeuristics(tree):
    heuristic = Heuristics(tree)
    data = heuristics(tree)
    heuristic.addHeuristic(data)
    while sumHVisited(tree) != 0:
        data = heuristics(tree)
        heuristic.addHeuristic(data)
    return tree 

# for node in problemTree.Nodes:
#     print(node.data)
# createHeuristics(problemTree)
# print(searchTree(problemTree).data)

def printSolution(solution):
    operand = solution.pop()
    variable = ''
    answer = ''
    if operand == '=':
        variable = solution.pop()
        answer = solution.pop()
    print('sol > ' + variable + ' = ' + answer)

def workOutflow():
    problemTree = problemCreator()
    createHeuristics(problemTree)
    solution = searchTree(problemTree).data
    printSolution(solution)

workOutflow()