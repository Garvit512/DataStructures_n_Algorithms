'''
$ Spiral Traverse $

Problem Statement:



  Write a function that takes in an n x m two-dimensional array (that can be
  square-shaped when n == m) and returns a one-dimensional array of all the
  array's elements in spiral order.

  Spiral order starts at the top left corner of the two-dimensional array, goes
  to the right, and proceeds in a spiral pattern all the way until every element
  has been visited.

  Sample Input:
  array = [[1,   2,  3, 4],
           [12, 13, 14, 5],
           [11, 16, 15, 6],
           [10,  9,  8, 7]]

  Sample Output:
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
'''

# O(n) time | O(n) space


def spiralTraverse(array):
    A = array
    res = []

    SC, EC = 0, len(A[0])-1
    SR, ER = 0, len(A)-1

    while SC <= EC and SR <= ER:
        for col in range(SC, EC+1):
            res.append(A[SR][col])

        for row in range(SR+1, ER+1):
            res.append(A[row][EC])

        for col in reversed(range(SC, EC)):
            if SR == ER:
                break
            res.append(A[ER][col])

        for row in reversed(range(SR+1, ER)):
            if SC == EC:
                break
            res.append(A[row][SC])

        SC += 1
        EC -= 1
        SR += 1
        ER -= 1

    return res


'''
Quick tip:
1- Define 4 variables i.e SC(start column), EC(end column), SR(start row), ER(end row)
2- rest the code is explaining itself

'''
