#!/usr/bin/python
import eqparser 
from createNode import Node, Tree, Heuristics
from inverse import inverse

def stackCopy(stack):
    returnStack = []
    for i in stack:
        returnStack.append(i)
    return returnStack

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
# def solver(string, starti, endi):
#     oper = ''
#     operFlag = False
#     para1 = ''
#     para1Flag = False
#     para2 = ''
#     para2Flag = False
#     for i in string[starti:endi]:
#         if i != ' ' and operFlag == False and para1Flag == False and para2Flag == False:
#             oper = oper + i
#         elif i != ' ' and operFlag == True and para1Flag == False and para2Flag == False:
#             para1 = para1 + i
#         elif i != ' ' and operFlag == True and para1Flag == True and para2Flag == False:
#             para2 = para2 + i
#         elif i == ' ':
#             if operFlag == False and para1Flag == False and para2Flag == False:
#                 operFlag = True
#             elif operFlag == True and para1Flag == False and para2Flag == False:
#                 para1Flag = True
#             elif operFlag == True and para1Flag == True and para2Flag == True:
#                 para2Flag ==True
#             elif string.index(i) == endi - 1:
#                 para2Flag == True
            
#             if para2Flag == True:
#                 break
#     print(oper)
#     print(para1)
#     print(para2)
#     output = 0
#     returnString = ''
#     intFlag = False
#     outputString = ''
#     stringFlag = False
#     for i in range(4):
#         returnString = ''
#         if para1.isdigit() and para2.isdigit():
#             if i == 0:
#                 output = int(para1) + int(para2)
#                 returnString = returnString + string[:starti-1] + str(output) + string[endi+1:]
#                 print(returnString)
#             elif i == 1:
#                 output = int(para1) * int(para2)
#                 returnString = returnString + string[:starti-1] + str(output) + string[endi+1:]
#                 print(returnString)
#             elif i == 2:
#                 output = int(para1) - int(para2)
#                 returnString = returnString + string[:starti-1] + str(output) + string[endi+1:]
#                 print(returnString)
#             elif i == 3:
#                 output = int(para1) / int(para2)
#                 returnString = returnString + string[:starti-1] + str(output) + string[endi+1:]
#                 print(returnString)

        





# input = repr(p)
# solver(input, 4, 9)
def stacker(string):
    stack = []
    entity = ''
    openOper = 0
    for i in string:
        if i == '(':
            openOper = openOper + 1
        elif i == ')':
            openOper = openOper - 1
            if entity != '':
                stack.insert(0, entity)
            entity = ''
        elif i != ' ':
            entity = entity + i
        elif i == ' ':
            if entity != '':
                stack.insert(0, entity)
            entity = '' 
    return stack

# stack = stacker(input)
# print(stack)



def createProblem(string):
    stack = stacker(string)
    rootNode = Node(stack)
    problemTree = Tree(rootNode)
    return problemTree


def dualOperator(para1, para2):
    output = []
    for i in range(4):
        if i == 0:
            output.append(float(para1) + float(para2))
        elif i == 1:
            output.append(float(para1) * float(para2))
        elif i == 2:
            output.append(float(para1) - float(para2))
        elif i == 3:
            if para2 != 0:
                output.append(float(para1) / float(para2))
            else:
                output.append('INF')
    return output

def dualOperator2(para1, para2):
    output = []
    for i in range(4):
        if i == 0:
            output.append('(' + para1 + ')' + '+' + '(' + para2 + ')')
        elif i == 1:
            output.append('(' + para1 + ')' + '*' + '(' + para2 + ')')
        elif i == 2:
            output.append('(' + para1 + ')' +  '-' + '(' + para2 + ')')
        elif i == 3:
            output.append('(' + para1 + ')' +  '/' + '(' + para2 + ')')
    return output

def nodeCreator(problemTree, currNode, stack, outputs, unused):
    oStack = stackCopy(stack)
    for i in outputs:
        stack.append(str(i))
        for j in unused:
            stack.append(j)
        nodeStack = stackCopy(stack)
        child = Node(nodeStack)
        problemTree.addNode(currNode, child)
        stack = stackCopy(oStack)



def solver2(tree):
    node = Node([])
    # print(len(tree.Nodes))
    for i in tree.Nodes:
        if i.visited == False:
            node = i
            i.changeVisited()
            break
    if node.data == []:
        print("All Nodes Created")
        return Node([])
    if len(node.data) == 3:
        operator = node.data.pop()
        if operator == '=':
            node.data.append(operator)
            # print("Final Equality")
            return Node([])
        else:
            node.data.append(operator)
    if len(node.data) == 1:
        print("Single Inequality")
        return Node([])
    dualOper = ['+', '-', '/', '*']
    equator = ['=']
    index = 0
    comperator = ['==', '!-', '>', '<', '>=', '<=']
    inverseStack = stackCopy(node.data)
    newNodeStack = inverse(inverseStack)
    if newNodeStack != []:
        tree.addNode(node, Node(newNodeStack))
    stack = stackCopy(node.data)
    
    elem1 = stack.pop()
    elem2 = stack.pop()
    elem3 = stack.pop()
    unused = []
    # if equator.count(elem1) != 1:
    #     return Node([])
    # elif equator.count(elem1) == 1 and dualOper.count(elem3):
    #     unused.insert(0, elem1)
    #     unused.insert(0, elem2)
    #     elem1 = elem3
    #     elem2 = stack.pop()
    #     elem3 = stack.pop()
    # else:
    
    # print(newNodeStack)
    
    while dualOper.count(elem1) != 1 or dualOper.count(elem2) != 0 or dualOper.count(elem3) != 0:     
        if dualOper.count(elem2) == 1:
            unused.insert(0, elem1)
            elem1 = elem2
            elem2 = elem3
            elem3 = stack.pop()
        elif dualOper.count(elem3) == 1:
            unused.insert(0, elem1)
            unused.insert(0, elem2)
            elem1 = elem3
            elem2 = stack.pop()
            elem3 = stack.pop()
    if is_number(elem2) and is_number(elem3):
        outputs = dualOperator(elem2, elem3)
        nodeCreator(tree, node, stack, outputs, unused)
    else:
        outputs = dualOperator2(elem2, elem3)
        nodeCreator(tree, node, stack, outputs, unused)
    return node
def sumVisited(tree):
    sum = 0
    for i in tree.Nodes:
        sum = sum + int(not i.visited)
    return sum

 

# input = '(= (* (* x 5) 5) 10)'
# input = '(= (- (* 3 x) 4) (* 4 5))'
# input = repr(p)
# input = '(= 3 4)'
# input = ''


def iterator(input):
    problemTree = createProblem(input)
    solver2(problemTree)
    while sumVisited(problemTree) != 0:
        solver2(problemTree)
    return problemTree 

# tree = iterator(input)
# for node in tree.Nodes:
#     print(node.data)
# print(sumVisited(tree))

def problemCreator():
    try:
        s = input('eq > ')   # use input() on Python 3
    except EOFError:
        print
    p = eqparser.parse(s)
    print("This is parsed as: " + repr(p))
    print("In infix form: " + str(p))

    # stackSolver = []
    # print(type(repr(p)))
    inp = repr(p)
    tree = iterator(inp)
    return tree