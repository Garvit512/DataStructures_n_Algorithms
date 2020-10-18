'''
$ Three Number Sum $

Problem Statement:


  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. The function should find all triplets in
  the array that sum up to the target sum and return a two-dimensional array of
  all these triplets. The numbers in each triplet should be ordered in ascending
  order, and the triplets themselves should be ordered in ascending order with
  respect to the numbers they hold.


  If no three numbers sum up to the target sum, the function should return an
  empty array.

  Sample Imput:
  array  = [12, 3, 1, 2, -6, 5, -8, 6]
  targetSum = 0

  Sample Output:
  [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

'''

# O(n^2) time | O(n) space
def threeNumberSum(array, targetSum):
	A = array
	A = sorted(A)
	n = len(A)
	dic = {}
	res = []

	for i in range(n):
		head_ptr = i+1
		tail_ptr = n-1

		while head_ptr < tail_ptr:

			add = A[i] + A[head_ptr] + A[tail_ptr]

			if add == targetSum:
				out = [A[i], A[head_ptr], A[tail_ptr]]
				out.sort()
				res.append(out)
				head_ptr += 1
				tail_ptr -= 1
			elif add < targetSum:
					head_ptr += 1
			elif add > targetSum:
					tail_ptr -= 1


	res.sort()
	return res


'''
Quick tip:
1- Sort the array
2- Itterate over array using single for loop and a while loop with two pointers i.e 'head_ptr' & 'tail_ptr'
3- perform sum of for loop element + head element + tail element
4- If sum == targetSum: store the numbers and contract the while loop by head_ptr++ and tail_ptr--
5- else if sum < targetSum then move head_ptr forward i.e head_ptr++
6- else if sum > targetSum then move tail_ptr backward i.e tail_ptr--
'''
