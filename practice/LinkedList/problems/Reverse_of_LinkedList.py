"""
Created on Sat Oct 12 22:53:04 2019

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


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def insertAtBeginning(self,data):
        self.length+=1
        newNode = Node()
        newNode.setData(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            print("Node ADDED at BEGINNING with data: {}".format(newNode.getData()))
            print("Head location: ",self.head)
            print('Node location ', newNode)
            print("Tail location: ",self.tail)

        else:
            newNode.setNext(self.head)
            self.head = newNode
            print("Node ADDED at BEGINNING with data: {}".format(newNode.getData()))
            print("Head location: ",self.head)
            print('Node location ', newNode)
            print("Tail location: ", self.tail)

        return '--------------------------------------------------'


    def insertAtLast(self,data):
        self.length+=1
        ittr = self.head
        newNode = Node()
        newNode.setData(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            print("Node ADDED at LAST with data: {}".format(newNode.getData()))
            print("Head location: ",self.head)
            print('Node location ', newNode)
            print("Tail location: ",self.tail)

        else:
            while ittr.getNext() is not None:
                ittr = ittr.getNext()
            ittr.setNext(newNode)
            newNode.setNext(None)
            self.tail = newNode
            print("Node ADDED at LAST with data: {}".format(newNode.getData()))
            print("Head location: ",self.head)
            print('Node location ', newNode)
            print("Tail location: ",self.tail)

        return '--------------------------------------------------'


    def insertAtMid(self,data,position):
        limit = position-1
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
            self.length += 1
            print("Node ADDED at MID at position-{} with data: {}".format(position,newNode.getData()))
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
                counter+=1
            val = self.head.getData()
            self.head.setNext(None)
            self.head.setData(None)
            self.head = ittr
            print("Node DELETED from BEGINNING with data: {}".format(val))
            print("Head location: ",self.head)
            print("Tail location: ",self.tail)
            self.length-=1
        return '--------------------------------------------------'


    def delFromEnd(self):
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
            print("Node DELETED from LAST with data: {}".format(val))
            print("Head location: ",self.head)
            print("Tail location: ",self.tail)
            self.length-=1
        return '--------------------------------------------------'


    def delFromMid(self,position):

        limit = position-1
        counter = 0
        previous = self.head
        current = self.head
        if self.length is 0:
            return "Nothing to delete from End"
        else:
            while counter is not limit:
                previous = current
                current = current.getNext()
                counter+=1
            val = current.getData()
            current = current.getNext()
            previous.setNext(current)
            print("Node DELETED from MID with data: {}".format(val))
            print("Head location: ",self.head)
            print("Tail location: ",self.tail)

            self.length-=1
        return '--------------------------------------------------'


    def printListwithSize(self,typee):
        ittr = self.head
        L1 = []
        L2 = []
        
        if typee == 'length':
            if self.length == 0:
                return "List is Empty"
            else:
                print("Length is: {}".format(self.length))
                
        if typee == 'printList':
            while ittr is not None:
                L1.append(ittr.getData())
                ittr = ittr.getNext()
            print("LinkedList: {}".format(L1))
            
        if typee == 'reverse':
            while ittr is not None:
                L2 = [ittr.getData()] + L2
                ittr = ittr.getNext()
            print("reverse:    {}".format(L2))
            
        return '---------------------------------------'
    
    
    def reverseList(self):
        L = []
        previousNode = None
        current = self.head
        nextNode = None
        
        while nextNode is not self.tail:
            
            nextNode = current.next
            current.setNext(previousNode)
            previousNode = current
            current = nextNode
        current.setNext(previousNode)     
        previousNode = current

        while previousNode is not None:
            L.append(previousNode.getData())
            previousNode = previousNode.next
         
        print("reversedList: ",L)
        return '---------------------------------------'
        
  
    def deleteLinkedList(self):
        self.head = None
        self.length = None
        print('--------------------------')
        return  "LinkedList Deleted"


linkedList = SinglyLinkedList()

print(linkedList.insertAtLast(10))
print(linkedList.insertAtLast(20))
print(linkedList.insertAtLast(30))


print(linkedList.printListwithSize('printList'))
print(linkedList.reverseList())
print(linkedList.deleteLinkedList())

