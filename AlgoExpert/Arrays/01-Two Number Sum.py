'''
$ Two Number Sum $

Problem Statement:

  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. If any two numbers in the input array sum
  up to the target sum, the function should return them in an array, in any
  order. If no two numbers sum up to the target sum, the function should return
  an empty array.

  Note that the target sum has to be obtained by summing two different integers
  in the array; you can't add a single integer to itself in order to obtain the
  target sum.

  You can assume that there will be at most one pair of numbers summing up to
  the target sum.


  Sample Input:
  array = [3, 5, -4, 8, 11, 1, -1, 6]
  targetSum = 10

  Sample Output:
  [-1, 11]

'''

 # O(n) time
def twoNumberSum(array, targetSum):
    A = array
	n = len(A)
	dic = {}
	res = []
	for i in range(n):
		y = targetSum - A[i]
		if y in dic.keys():
			res.append(A[i])
			res.append(y)
		else:
			dic.update({A[i]:True})

	return res


'''
Quick tip:
1- Handle the Problem as solving equation {x + y = z}
2- solve {y = z - x} as we know, x is the list elements and z our targetSum
3- if y is present in dictionary, i.e we've find out targetSum as x+y = targetSum or z
4- else update the dictionary
'''
