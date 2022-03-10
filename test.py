from equationsimplier import stackCopy
input = ['5', '4', '*', '4', 'x', '3', '*', '-', '=']
input = ['5', '4', '*', 'x', '3', '*', '=']

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
print(varStack(input))

def change_Stack(node_data, child_data):
    node_copy = stackCopy(node_data)
    child_copy = stackCopy(child_data)
    