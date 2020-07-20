'''
$ Subarray Sort $

Problem Statement:

  Write a function that takes in an array of at least two integers and that
  returns an array of the starting and ending indices of the smallest subarray
  in the input array that needs to be sorted in place in order for the entire
  input array to be sorted (in ascending order).

  If the input array is already sorted, the function should return [-1, -1]



  Sample Input:
  array  = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

  Sample Output:
  [3, 9]

'''



# O(n) time | O(1) space
def subarraySort(array):
    # Write your code here.
	n = len(array)
	minOutOfOrder = float('inf')
	maxOutOfOrder = float('-inf')

	for i in range(n):
		num = array[i]
		if isOutOfOrder(i, num, array):
			minOutOfOrder = min(minOutOfOrder, num)
			maxOutOfOrder = max(maxOutOfOrder, num)

	if 	minOutOfOrder == float('inf'):
		return [-1,-1]
	subArrayLeftIdx = 0
	while minOutOfOrder >= array[subArrayLeftIdx]:
		subArrayLeftIdx+=1
	subArrayRightIdx = len(array)-1
	while maxOutOfOrder <= array[subArrayRightIdx]:
		subArrayRightIdx-=1

	return [subArrayLeftIdx, subArrayRightIdx]



def isOutOfOrder(i, num, array):
	if i == 0:
		return num > array[i+1]
	if i == len(array)-1:
		return num < array[i-1]
	return num > array[i+1] or num < array[i-1]




'''
Quick tip:
1- check the sub-part of array which doesn't not follows ascending behaviour and
   store those elements as 'minOutOfOrder' and 'maxOutOfOrder'
2- do compare all itterating elements of sub-array with 'minOutOfOrder' & 'maxOutOfOrder' and
   replace if found new min of new max
3- Apart from sub-array, the whole rest array is sorted and
   we have our min and max of sub-array (not follows ascending behaviour)
4- Now just find the suitable position in array for our min and max of sub-array and return those indexes
'''
