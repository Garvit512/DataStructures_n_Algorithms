'''
$ Monotonic Array $

(array which is continous increasing or decreasing)

Problem Statement:
  

  
  Write a function that takes in an array of integers and returns a boolean
  representing whether the array is monotonic.

  An array is said to be monotonic if its elements, from left to right, are
  entirely non-increasing or entirely non-decreasing.

  Non-increasing elements aren't necessarily exclusively decreasing; they simply
  don't increase. Similarly, non-decreasing elements aren't necessarily
  exclusively increasing; they simply don't decrease.

  Note that empty arrays and arrays of one element are monotonic.

  Sample Input:
  array  = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

  Sample Output:
  true
'''

# O(n) time | O(1) space


def isMonotonic(array):
    return (all([array[i] >= array[i+1] for i in range(len(array)-1)]) or
            all([array[i] <= array[i+1] for i in range(len(array)-1)]))


'''
Quick tip:
1- use all() function which returns True if all the elements of the array are True
   of returns False  if all the elements of an array are False
'''
