def balancedBrackets(string):
    stack = []
    balanced = False
    bracketDic = {'(': ')', '{': '}', '[': ']'}

    if len(string):
        for bracket in string:
            print("###############")
            print(f"at '{bracket}'")
            if bracket == '(' or bracket == '[' or bracket == '{':
                stack.append(bracket)
            elif bracket == ')' or bracket == ']' or bracket == '}':
                if len(stack) == 0:
                    balanced = False
                elif len(stack) != 0 and bracket == bracketDic[stack[len(stack)-1]]:
                    x = stack.pop()
                    print(f"poping {x} and {bracket}")
                    balanced = True
                else:
                    # balanced = False
                    return False
            print(stack)
        if len(stack) != 0:
            balanced = False
    return balanced
