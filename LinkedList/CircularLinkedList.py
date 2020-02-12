"""
Created on Tue Feb 11 21:35:21 2020

@author: garvit
"""

class Node:

    # initilizing a node on circular linked list
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


class CircularLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.L = []

    def insertAtBeginning(self, data):
        self.length += 1
        newNode = Node()
        newNode.setData(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.tail.setNext(self.head)
            print("Node ADDED at BEGINNING with data: {}".format(newNode.getData()))
            print("Head location: ", self.head)
            print('Node location ', newNode)
            print("Tail location: ", self.tail)
            print("Tail Next location: ", self.tail.getNext())
        else:
            newNode.setNext(self.head)
            self.head = newNode
            self.tail.setNext(self.head)
            print("Node ADDED at BEGINNING with data: {}".format(newNode.getData()))
            print("Head location: ", self.head)
            print('Node location ', newNode)
            print("Tail location: ", self.tail)
            print("Tail Next location: ", self.tail.getNext())

        return '--------------------------------------------------'

    def insertAtLast(self, data):
        self.length += 1
        ittr = self.head
        newNode = Node()
        newNode.setData(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.setNext(self.head)
            print("Node ADDED at LAST with data: {}".format(newNode.getData()))
            print("Head location: ", self.head)
            print('Node location ', newNode)
            print("Tail location: ", self.tail)
            print("Tail Next location: ", self.tail.getNext())

        else:

            self.tail.setNext(newNode)
            self.tail = newNode
            self.tail.setNext(self.head)
            print("Node ADDED at LAST with data: {}".format(newNode.getData()))
            print("Head location: ", self.head)
            print('Node location ', newNode)
            print("Tail location: ", self.tail)
            print("Tail Next location: ", self.tail.getNext())

        return '--------------------------------------------------'

    def insertAtMid(self, data, position):
        limit = position - 1
        counter = 0
        previous = self.head
        current = self.head
        newNode = Node()
        newNode.setData(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.length += 1
            print("Node ADDED at MID with data: {}".format(newNode.getData()))
            print("Head location: ", self.head)
            print('Node location ', newNode)
            print("Tail location: ", self.tail)
        else:
            while counter is not limit:
                previous = current
                current = current.getNext()
                counter += 1
            previous.setNext(newNode)
            newNode.setNext(current)
            self.length += 1
            print("Node ADDED at MID at position-{} with data: {}".format(position, newNode.getData()))
            print("Head location: ", self.head)
            print('Node location ', newNode)
            print("Tail location: ", self.tail)
        return '--------------------------------------------------'

    def delFromStart(self):
        ittr = self.head
        counter = 0
        if self.length is 0:
            return "Nothing to delete from Start"
        else:
            while counter is not 1:
                ittr = ittr.getNext()
                counter += 1
            val = self.head.getData()
            self.head.setNext(None)
            self.head.setData(None)
            self.head = ittr
            self.L.remove(self.L[0])
            print("Node DELETED from BEGINNING with data: {}".format(val))
            print("Head location: ", self.head)
            print("Tail location: ", self.tail)
            self.length -= 1
        return '--------------------------------------------------'

    def delFromEnd(self):
        ittr = self.head
        if self.length is 0:
            return "Nothing to delete from End"
        else:
            self.tail.setNext(None)
            while ittr.getNext() is not None:
                ittr = ittr.getNext()
            ittr.setNext(self.head)
            self.tail = ittr
            val = self.tail.getData()
            self.L.pop()
            # self.tail.setNext(self.head)
            print("Node DELETED from LAST with data: {}".format(val))
            print("Head location: ", self.head)
            print("Tail location: ", self.tail)
            print("Tail Next location: ", self.tail.getNext())
            self.length -= 1
        return '--------------------------------------------------'

    def delFromMid(self, position):

        limit = position - 1
        counter = 0
        previous = self.head
        current = self.head
        if self.length is 0:
            return "Nothing to delete from End"
        else:
            while counter is not limit:
                previous = current
                current = current.getNext()
                counter += 1
            val = current.getData()
            current = current.getNext()
            previous.setNext(current)
            print("Node DELETED from MID with data: {}".format(val))
            print("Head location: ", self.head)
            print("Tail location: ", self.tail)

            self.length -= 1
        return '--------------------------------------------------'

    def printListwithSize(self):
        self.tail.setNext(None)
        ittr = self.head
        while ittr is not None:
            self.L.append(ittr.getData())
            ittr = ittr.getNext()
        self.tail.setNext(self.head)
        if self.length == 0:
            return "List is Empty"
        else:
            print("Length is: {}".format(self.length))
        print(f"LinkedList: {self.L}")
        return '---------------------------------------'

    def deleteLinkedList(self):
        self.head = None
        self.length = None
        print('--------------------------')
        return "LinkedList Deleted"


linkedList = CircularLinkedList()


# print(linkedList.delFromEnd())
# print(linkedList.delFromEnd())
# # print(linkedList.deleteLinkedList())
# print(linkedList.insertAtLast(5))
# print(linkedList.insertAtLast(10))


# print(linkedList.insertAtBeginning(10))
# print(linkedList.insertAtBeginning(22))

# print(linkedList.insertAtLast(8))
# print(linkedList.insertAtLast(9))
# print(linkedList.insertAtLast(10))
# print(linkedList.insertAtLast(11))

# print(linkedList.printListwithSize())





