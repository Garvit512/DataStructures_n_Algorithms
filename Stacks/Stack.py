"""
Created on Sat Oct 19 22:47:43 2019

@author: garvit
"""


class Stack:

    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)
        print("push in STACK: {}".format(data))

    def pop(self):
        print("pop from STACK: {}".format(self.items.pop()))

    def peak(self):
        if len(self.items) == 0:
            print("Stack is Empty")
        else:
            print("peak of STACK: ", self.items[len(self.items) - 1])

    def size(self):
        print("size of STACK: ", len(self.items))

    def isEmpty(self):

        if self.items == []:
            print("Stack is Empty")
        else:
            print("Stack is not Empty")

    def printStack(self):
        print("Stack: ", self.items)


stk = Stack()

stk.push(10)
stk.push(20)
stk.push(30)
stk.push(40)

stk.pop()
stk.size()
stk.isEmpty()
stk.peak()
stk.printStack()






