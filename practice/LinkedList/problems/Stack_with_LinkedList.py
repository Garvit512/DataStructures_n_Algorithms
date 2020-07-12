#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 21:56:10 2020

@author: garvit
"""

class Node:

    # initilizing a node on singly linked list
    def __init__(self):
        self.data = None
        self.next = None

    # setting data in node
    def setData(self,data):
        self.data = data

    # getting data from node
    def getData(self):
        return self.data

    # setting next in node
    def setNext(self,next):
        self.next = next

    # getting next from node
    def getNext(self):
        return self.next

    # hasNext
    def hasNext(self):
        if self.getNext() is not None:
            return False
        else:
            return True


class Stack_LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def push(self,data):
        self.length+=1
        ittr = self.head
        newNode = Node()
        newNode.setData(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            print(f"{newNode.getData()} PUSHED in Stack")
            # print("Head location: ",self.head)
            # print('Node location ', newNode)
            # print("Tail location: ",self.tail)
        else:
            while ittr.getNext() is not None:
                ittr = ittr.getNext()
            ittr.setNext(newNode)
            newNode.setNext(None)
            self.tail = newNode
            print(f"{newNode.getData()} PUSHED in Stack")
            # print("Head location: ",self.head)
            # print('Node location ', newNode)
            # print("Tail location: ",self.tail)

        return '--------------------------------------------------'


    def pop(self):
        current = self.head
        previous = self.head
        if self.length is 0:
            return "Nothing to delete from End"
        else:
            while current.getNext() is not None:
                previous = current
                current = current.getNext()
            previous.setNext(None)
            val = current.getData()
            print(f"{val} POP from Stack")
            # print("Head location: ",self.head)
            # print("Tail location: ",self.tail)
            self.length-=1
        return '--------------------------------------------------'




    def printStack(self):
        ittr = self.head
        L = []
        while ittr is not None:
            L.append(ittr.getData())
            ittr = ittr.getNext()
        if self.length == 0:
            return "List is Empty"
        else:
            print("Length is: {}".format(self.length))
        print("Stack: {}".format(L))
        return '---------------------------------------'

    def deleteStack(self):
        self.head = None
        self.length = None
        print('--------------------------')
        return  "Stack Deleted"





stk = Stack_LinkedList()




print(stk.push(1))
print(stk.push(2))
print(stk.push(3))

print(stk.printStack())

print(stk.pop())

