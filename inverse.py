# from equationsimplier import is_number
input = ['5', '4', '*', '4', 'x', '3', '*', '-', '=']
input = ['5', '4', '*', 'x', '3', '*', '=']

def stackCopy(stack):
    returnStack = []
    for i in stack:
        returnStack.append(i)
    return returnStack

def inverse(stack):
    dualOper = ['+', '-', '/', '*']
    for i in stack:
        if not i.isalnum() and dualOper.count(i) != 1 and i != '=':
            return []
    # print(stack)
    # print(stack)
    ogStack = stackCopy(stack)
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
        paraCount = 0
        var = []
        non = []
        stackCount = 0
        if len(variableStack) > 1:
            operation = variableStack.pop()
            if operation == '-':
                nonvariableStack.append('+')
            elif operation == '/':
                nonvariableStack.append('*')
            elif operation == '+':
                nonvariableStack.append('-')
            elif operation == '*':
                nonvariableStack.append('/')
            oper = 0
            while len(variableStack) != 0:
                elem = variableStack.pop()
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
                        var.insert(0, elem)
                    elif stackCount == 1:
                        non.insert(0, elem)
                else:
                    if stackCount == 0:
                        var.insert(0, elem)
                    else:
                        non.insert(0, elem)
            if var.count('x') == 0:
                temp = var
                var = non
                non = temp
            while len(non) != 0:
                nonvariableStack.insert(0, non.pop())
            returnStack = ['=']
            while len(var) != 0:
                returnStack.insert(0, var.pop())
            while len(nonvariableStack) != 0:
                returnStack.insert(0, nonvariableStack.pop())
            # print(ogStack)
            # print(returnStack)
            return returnStack
        else:
            return []
# print(input)
# print(inverse(input))