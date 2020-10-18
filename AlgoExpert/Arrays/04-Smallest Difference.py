'''
$ Smallest difference $

Problem Statement:


  Write a function that takes in two non-empty arrays of integers, finds the
  pair of numbers (one from each array) whose absolute difference is closest to
  zero, and returns an array containing these two numbers, with the number from
  the first array in the first position.

  You can assume that there will only be one pair of numbers with the smallest
  difference.

  Sample Imput:
  arrayOne = [-1, 5, 10, 20, 28, 3]
  arrayTwo = [26, 134, 135, 15, 17]

  Sample Output:
  [28, 26]

'''


# O(nlogn + mlogm) time
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
	A = arrayOne
	B = arrayTwo
	A = sorted(A)
	B = sorted(B)

	A_ptr = 0
	B_ptr = 0
	temp = [999999, 999999]

	while A_ptr != len(A) and B_ptr != len(B):

		if A[A_ptr] == B[B_ptr]:
			temp[0] = [A[A_ptr], B[B_ptr]]
			temp[1] = 0
			return temp[0]

		sub = abs(A[A_ptr] - B[B_ptr])
		if sub < temp[1]:
			temp[0] = [A[A_ptr], B[B_ptr]]
			temp[1] = sub

			if A[A_ptr] < B[B_ptr]:
				A_ptr +=1
			elif A[A_ptr] > B[B_ptr]:
				B_ptr += 1

		elif A[A_ptr] < B[B_ptr]:
				A_ptr +=1
		elif A[A_ptr] > B[B_ptr]:
			B_ptr += 1
	return temp[0]


'''
Quick tip:

Can solve in O(n^2) using dictionary approach by storing every pair with its difference (not optimised)

1- Sort both the arrays
2- initilize two pointers 'A_ptr' & 'B_ptr' for both arrays
3- Itterate over arrays using while loop with condition: while each pointer value is less than it's array's length
4- get absolute difference value from both pointers located at specific position
5- if new_diff < old_diff then
   update the old_diff with new_diff and update pointers with logic:
        if   value of A_ptr < B_ptr then increment A_ptr++
        elif value of A_ptr > B_ptr then increment B_ptr++

6- update pointers with logic:
        elif   value of A_ptr < B_ptr then increment A_ptr++
        elif   value of A_ptr > B_ptr then increment B_ptr++
'''
