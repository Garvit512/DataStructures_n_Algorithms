class MinMaxStack:
    def __init__(self):
        self.minMaxDic = {'min': [], 'max': []}
        self.stack = []

    def peek(self):
        if len(self.stack) == 0:
            return "stack is empty"
        else:
            return self.stack[len(self.stack)-1]

    def push(self, number):
        if len(self.stack) == 0 or number <= self.minMaxDic['min'][len(self.minMaxDic['min'])-1]:
            self.minMaxDic['min'].append(number)

        if len(self.stack) == 0 or number >= self.minMaxDic['max'][len(self.minMaxDic['max'])-1]:
            self.minMaxDic['max'].append(number)

        self.stack.append(number)

    def getMin(self):
        if len(self.minMaxDic['min']) != 0:
            return self.minMaxDic['min'][len(self.minMaxDic['min'])-1]
        else:
            return None

    def getMax(self):
        if len(self.minMaxDic['max']) != 0:
            return self.minMaxDic['max'][len(self.minMaxDic['max'])-1]
        else:
            return None

    def pop(self):
        if len(self.stack) == 0:
            return "stack is empty"
        else:
            res = self.stack.pop()
            if len(self.minMaxDic['min']) != 0 and res == self.minMaxDic['min'][len(self.minMaxDic['min'])-1]:
                self.minMaxDic['min'].pop()
            if len(self.minMaxDic['max']) != 0 and res == self.minMaxDic['max'][len(self.minMaxDic['max'])-1]:
                self.minMaxDic['max'].pop()
        return res

    def getStack(self):
        print("Min stack: ", self.minMaxDic['min'])
        print("Max stack: ", self.minMaxDic['max'])
        print("stack: ", self.stack)


stk = MinMaxStack()
stk.push(5)
stk.getStack()
stk.push(5)
stk.getStack()
stk.push(5)
stk.getStack()
stk.push(8)
stk.getStack()
stk.push(8)
stk.getStack()

stk.push(26)
stk.getStack()
stk.push(5)
stk.getStack()
stk.push(8)
stk.getStack()
stk.push(3)
stk.getStack()
stk.push(9)
stk.getStack()
stk.push(90)
stk.getStack()
stk.push(9)
stk.getStack()
stk.push(0)
stk.getStack()


stk.peek()
stk.getStack()
stk.getMin()
stk.getMax()

print(stk.pop())
stk.getStack()
