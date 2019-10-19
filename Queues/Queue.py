"""
Created on Sat Oct 19 23:56:57 2019

@author: garvit
"""


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.insert(0, data)
        print("enqueue in QUEUE: ", data)

    def dequeue(self):
        print("dequeue from QUEUE: ", self.items.pop())

    def size(self):
        print("size of QUEUE: ", len(self.items))

    def printQueue(self):
        print("Queue: ", self.items)


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.printQueue()
queue.dequeue()
queue.printQueue()
queue.size()