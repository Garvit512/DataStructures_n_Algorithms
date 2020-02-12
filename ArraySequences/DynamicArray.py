"""
Created on Wed Oct  9 23:13:19 2019

@author: garvit
"""

# Dynamic Arrays with python

import sys
import ctypes
import timeit


class DynamicArray():

    def __init__(self):
        self.n = 0  # count array elements
        self.capacity = 1  # array capacity i.e 1
        self.A = self.make_array(self.capacity)  # to create

    def _len(self):
        return "Array size is {}".format(self.n)

    def getitem(self, i):
        # return element at index i
        if i > self.n and i <= 0:
            return IndexError('i is out of bounds')

        print()
        print("Item at index {} is {}".format(i, self.A[i]))

    def additem(self, item):

        if self.n >= self.capacity:
            self._resize(2 * self.capacity)
            print("Array size increased dynamically")

        self.A[self.n] = item
        self.n += 1
        print("{} added in array".format(item))

    def _resize(self, new_cap):

        B = self.make_array(new_cap)

        for i in range(len(self.A)):
            B[i] = self.A[i]

        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):

        return (new_cap * ctypes.py_object)()


arr = DynamicArray()

arr._len
arr.additem(3)
arr.additem(5)

arr.getitem(1)
