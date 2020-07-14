'''
$ Validate Subsequence $

Problem Statement:

  Given two non-empty arrays of integers, write a function that determines
  whether the second array is a subsequence of the first one.

  A subsequence of an array is a set of numbers that aren't necessarily adjacent
  in the array but that are in the same order as they appear in the array. For
  instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4]
  , and so do the numbers [2, 4] . Note that a single number in an array and the
  array itself are both valid subsequences of the array.

  Sample Input:
  array  = [5, 1, 22, 25, 6, -1, 8, 10]
  sequence  = [1, 6, -1, 10]

  Sample Output:
  true

'''

# O(n) time | O(1) space - where n is the length of the array
def isValidSubsequence(array, sequence):
	A = array
	seq = sequence

	A_ptr = 0
	seq_ptr = 0

	while A_ptr<len(A) and seq_ptr<len(seq):
		if A[A_ptr] == seq[seq_ptr]:
			seq_ptr+=1
		A_ptr+= 1

	return seq_ptr == len(seq)


'''
Quick tip:
1- Use two pointer 'A_ptr' & 'seq_ptr' for both arrays
2- Compare the pointer of both arrays pointing at perticular element
3- if both element matches, increase both pointer position by 1, else increase outer/ main array pointer i.e A_ptr by 1
4- itterate while A_ptr<len(A) and seq_ptr<len(seq)
'''
