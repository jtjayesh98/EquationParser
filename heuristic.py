from inspect import stack
from re import L
from createNode import Node, Tree, Heuristics
from equationsimplier import stackCopy

def find_operation(stack):
    dualOper = ['+', '-', '/', '*']
    elem1 = stack.pop()
    elem2 = stack.pop()
    elem3 = stack.pop()
    unused = []
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
    return elem1

def compareStack(nodeData, childData):
    return 0

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def find_operations(node_data):
    dualOper = ['+', '-', '/', '*']
    operator = node_data.pop()
    if dualOper.count(operator) == 1:
        para1 = node_data.pop()
        para2 = node_data.pop()
        operations = [operator, para1, para2]
        return operations

def varStack(stack):
    operator = stack.pop()
    stackCount = 0
    paraCount = 0
    LHSStack = []
    RHSStack = []
    oper = 0
    dualOper = ['+', '-', '/', '*']
    if operator == '=':
        while len(stack) != 0:
            elem = stack.pop()
            if dualOper.count(elem) == 1:
                oper = oper + 1
            else:
                paraCount = paraCount + 1
                if paraCount == 2:
                    oper = oper - 1
                    if oper != 0:
                        paraCount = paraCount - 1
                    else:
                        paraCount = 0
            if oper == 0:
                if stackCount == 0:
                    stackCount = stackCount+ 1
                    LHSStack.insert(0, elem)
                elif stackCount == 1:
                    RHSStack.insert(0, elem)
            else:
                if stackCount == 0:
                    LHSStack.insert(0, elem)
                else:
                    RHSStack.insert(0, elem)
        # print(LHSStack)
        # print(RHSStack)
        if len(LHSStack)==0 or len(RHSStack) == 0:
            return []
        variableStack = []
        nonvariableStack = []
        if LHSStack.count('x') > 0 :
            if RHSStack.count('x') > 0:
                LHSStack = LHSStack
                RHSStack = RHSStack
                print("Perform action to get all variable on one side")
            else:
                variableStack = LHSStack
                nonvariableStack = RHSStack
        else:
            variableStack = RHSStack
            nonvariableStack = LHSStack
    return variableStack

def find_change(node_data, child_data):
    node_copy = stackCopy(node_data)
    # print(node_copy)
    child_copy = stackCopy(child_data)
    # print(child_copy)
    if len(node_data) == len(child_data):
        return compareStack(node_data, child_data)
    else:
        for i in range(min(len(node_data), len(child_data))):
            node_elem = node_copy.pop()
            child_elem = child_copy.pop()
            if node_elem != child_elem:
                node_copy.append(node_elem)
                node_operations = find_operations(node_copy)
                return [node_operations, child_elem]

def change_Stack(node_data, child_data):
    node_copy = stackCopy(node_data)
    child_copy = stackCopy(child_data)
    nodeVar = varStack(node_copy)
    childVar = varStack(child_copy)
    return (len(nodeVar) - len(childVar))*10
    

def heuristics(tree):
    node = Node([])
    dualOper = ['+', '-', '/', '*']
    for i in tree.Nodes:
        if i.hVisited == False:
            node = i
            i.changeHVisited()
            break
    if node.data == []:
        return
    stack_heuristic = create_heuristics(node.children_list)
    if node.children_list == []:
        return
    for i in node.children_list:
        if len(i.data) != len(node.data):
            stack_heuristic[node.children_list.index(i)] = stack_heuristic[node.children_list.index(i)] + calculator(i.data)
            operations, result = find_change(node.data, i.data)
            if is_number(operations[1]) and is_number(operations[2]):
                if operations[0] == '+':
                    if float(result) == float(operations[1]) + float(operations[2]):
                        stack_heuristic[node.children_list.index(i)] = stack_heuristic[node.children_list.index(i)] + 10
                    else:
                        stack_heuristic[node.children_list.index(i)] = stack_heuristic[node.children_list.index(i)] - 1
                elif operations[0] == '-':
                    if float(result) == float(operations[1]) - float(operations[2]):
                        stack_heuristic[node.children_list.index(i)] = stack_heuristic[node.children_list.index(i)] + 10
                    else:
                        stack_heuristic[node.children_list.index(i)] = stack_heuristic[node.children_list.index(i)] - 1
                elif operations[0] == '*':
                    if float(result) == float(operations[1]) * float(operations[2]):
                        stack_heuristic[node.children_list.index(i)] = stack_heuristic[node.children_list.index(i)] + 10
                    else:
                        stack_heuristic[node.children_list.index(i)] = stack_heuristic[node.children_list.index(i)] - 1
                elif operations[0] == '/':
                    if float(result) == float(operations[1]) / float(operations[2]):
                        stack_heuristic[node.children_list.index(i)] = stack_heuristic[node.children_list.index(i)] + 10
                    else:
                        stack_heuristic[node.children_list.index(i)] = stack_heuristic[node.children_list.index(i)] - 1
            else:
                operand = ''
                for j in result:
                    if dualOper.count(j) == 1:
                        operand = j
                # print(operand)
                if operations[0] == '+':
                    if operand == '+':
                        stack_heuristic[node.children_list.index(i)] = stack_heuristic[node.children_list.index(i)] + 5
                    else:
                        stack_heuristic[node.children_list.index(i)] = stack_heuristic[node.children_list.index(i)] - 1
                elif operations[0] == '-':
                    if operand == '-':
                        stack_heuristic[node.children_list.index(i)] = stack_heuristic[node.children_list.index(i)] + 5
                    else:
                        stack_heuristic[node.children_list.index(i)] = stack_heuristic[node.children_list.index(i)] - 1
                elif operations[0] == '*':
                    if operand == '*':
                        stack_heuristic[node.children_list.index(i)] = stack_heuristic[node.children_list.index(i)] + 5
                    else:
                        stack_heuristic[node.children_list.index(i)] = stack_heuristic[node.children_list.index(i)] - 1
                elif operations[0] == '/':
                    if operand == '/':
                        stack_heuristic[node.children_list.index(i)] = stack_heuristic[node.children_list.index(i)] + 5
                    else:
                        stack_heuristic[node.children_list.index(i)] = stack_heuristic[node.children_list.index(i)] - 1
        else:
            stack_heuristic[node.children_list.index(i)] = stack_heuristic[node.children_list.index(i)] + change_Stack(node.data, i.data)
    # print(stack_heuristic)
    returnVal = [node, stack_heuristic]
    return returnVal

def create_heuristics(node_list):
    returnVal = []
    for i in node_list:
        returnVal.append(0)
    return returnVal

def calculator(stack):
    if len(stack) == 3:
        copyStack = stackCopy(stack)
        operator = copyStack.pop()
        if operator == '=':
            return 10
    else:
        return 0