"""
Created on Sat Oct 19 23:56:57 2019

@author: garvit
"""

class Queue:

    def __init__(self, limit = 5):
        self.que = []
        self.tail = None
        self.head = None
        self.limit = limit
        self.size = 0


    def isEmpty(self):
        if self.size == 0:
            print('Queue is empty')
        else:
            print(f"Queue size: {self.size}")



    def enqueue(self, data):
        if self.size >= self.limit:
            print('Queue Overflow')
        else:
            self.que.append(data)

        if self.head is None:
            self.head = self.tail = 0
        else:
            self.tail = self.size

        self.size+=1

        print(f"Enqueue {data} at location {self.tail}")
        print(f"head location: {self.head}")
        print(f"tail location: {self.tail}")

        return "---------------------------"

    def dequeue(self):
        if self.size == 0:
            print('Queue underflow')
        else:
            poped = self.que.pop(0)
            self.size-=1
            print(f"Dequeue {poped} from location {self.head}")
            self.head = self.head+1
            print(f"head location: {self.head}")
            print(f"tail location: {self.tail}")

        return "---------------------------"


    def printQueue(self):
        print('Queue:', self.que)

        return "---------------------------"




queue = Queue()

queue.isEmpty()

print(queue.enqueue(10))
print(queue.enqueue(15))
print(queue.enqueue(21))
print(queue.enqueue(2))
print(queue.enqueue(6))

print(queue.printQueue())

queue.dequeue()