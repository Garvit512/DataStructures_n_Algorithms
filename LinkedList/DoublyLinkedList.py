class Node:

    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None

    def setData(self,data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self,next):
        self.next = next

    def getNext(self):
        return self.next

    def setPrev(self,prev):
        self.prev = prev

    def getPrev(self):
        return self.prev

    def hasPrev(self):
        if self.prev is None:
            return False
        else:
            return True

    def hasNext(self):
        if self.next is None:
            return False
        else:
            return True


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insertAtBeginning(self,data):
        newNode = Node()
        newNode.setData(data)

        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            self.length+=1
            print("Node ADDED at BEGINNING with data: {}".format(newNode.getData()))
            print("Head location: ",self.head)
            print('Node location ', newNode)
            print("Tail location: ",self.tail)

        else:
            newNode.setNext(self.head)
            self.head.setPrev(newNode)
            self.head = newNode
            self.length+=1
            print("Node ADDED at BEGINNING with data: {}".format(newNode.getData()))
            print("Head location: ",self.head)
            print('Node location ', newNode)
            print("Tail location: ",self.tail)
        return ''

    def insertAtEnd(self,data):
        ittr = self.head
        newNode = Node()
        newNode.setData(data)

        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            self.length+=1
            print("Node ADDED at LAST with data: {}".format(newNode.getData()))
            print("Head location: ",self.head)
            print('Node location ', newNode)
            print("Tail location: ",self.tail)

        else:
            while ittr.getNext() is not None:
                ittr = ittr.getNext()
            self.tail.setNext(newNode)
            newNode.setPrev(self.tail)
            self.tail = newNode
            self.tail.setNext(None)
            self.length += 1
            print("Node ADDED at LAST with data: {}".format(newNode.getData()))
            print("Head location: ",self.head)
            print('Node location ', newNode)
            print("Tail location: ",self.tail)

        return ''

    def insertAtMid(self,data,position):
        newNode = Node()
        newNode.setData(data)
        limit = position
        counter = 1
        previous = self.head
        current = self.head

        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            self.length+=1
            print("Node ADDED at LAST with data: {}".format(newNode.getData()))
            print("Head location: ",self.head)
            print('Node location ', newNode)
            print("Tail location: ",self.tail)
        else:
            while counter is not limit:
                previous = current
                current = current.getNext()
                counter+=1

            previous.setNext(newNode)
            newNode.setNext(current)
            self.length+=1
            print("Node ADDED at MID at position-{} with data: {}".format(position,newNode.getData()))
            print("Head location: ",self.head)
            print('Node location ', newNode)
            print("Tail location: ",self.tail)

        return ''

    def delFromStart(self):
        ittr = self.head

        if self.head is None:
            print("Nothing to Delete")
        else:
            val = self.head.getData()
            ittr = ittr.getNext()
            self.head.setNext(None)
            ittr.setPrev(None)
            self.head = ittr
            print("Node DELETED from BEGINNING with data: {}".format(val))
            print("Head location: ",self.head)
            print("Tail location: ",self.tail)
            self.length-=1

        return ''

    def delFromEnd(self):
        previous = self.head
        current = self.head

        if self.head is None:
            print("Nothing to Delete")
        else:
            while current.getNext() is not None:
                previous = current
                current = current.getNext()
            val = self.tail.getData()
            previous.setNext(None)
            self.tail = previous
            print("Node DELETED from LAST with data: {}".format(val))
            print("Head location: ",self.head)
            print("Tail location: ",self.tail)
            self.length-=1

        return ''

    def delFromMid(self,position):
        previous = self.head
        current = self.head
        limit = position
        counter = 1

        if self.head is None:
            print("Nothing to Delete")
        else:
            while counter != limit:
                previous = current
                current = current.getNext()
                counter+=1
            val = current.getData()
            current = current.getNext()
            previous.setNext(current)
            current.setPrev(previous)
            # print("pevious: ",previous)
            # print('current: ',current)
            print("Node DELETED from MID with data: {}".format(val))
            print("Head location: ",self.head)
            print("Tail location: ",self.tail)
            self.length-=1
        return ''

    def printListwithSize(self):
        ittr = self.head
        L = []
        while ittr is not None:
            L.append(ittr.getData())
            ittr = ittr.getNext()
        if self.length == 0:
            print("List is Empty")
        else:
            print('Length: ',self.length)
        print('LinkedList: ',L)
        return '------------------------------------'

    def deleteLinkedList(self):
        self.head = None
        self.length = None
        print('--------------------------')
        return  "LinkedList Deleted"


linkedList = DoublyLinkedList()

# print(linkedList.insertAtBeginning(2))
# print(linkedList.printListwithSize())

# print(linkedList.insertAtBeginning(3))
# print(linkedList.printListwithSize())

print(linkedList.insertAtEnd(11))
print(linkedList.printListwithSize())

print(linkedList.insertAtEnd(12))
print(linkedList.printListwithSize())

print(linkedList.insertAtEnd(13))
print(linkedList.printListwithSize())

print(linkedList.delFromMid(2))
print(linkedList.printListwithSize())

print(linkedList.deleteLinkedList())
print(linkedList.printListwithSize())

