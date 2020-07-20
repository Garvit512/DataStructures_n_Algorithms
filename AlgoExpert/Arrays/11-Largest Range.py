'''
$ Largest Range $

Problem Statement:


  Write a function that takes in an array of integers and returns an array of
  length 2 representing the largest range of integers contained in that array.

  The first number in the output array should be the first number in the range,
  while the second number should be the last number in the range.

  A range of numbers is defined as a set of numbers that come right after each
  other in the set of real integers. For instance, the output array [2, 6]
  represents the range {2, 3, 4, 5, 6} , which
  is a range of length 5. Note that numbers don't need to be sorted or adjacent
  in the input array in order to form a range.

  You can assume that there will only be one largest range.


  Sample Input:
  array   = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]

  Sample Output:
  [0, 7]

'''


# O(nlogn) time | O(n) space
def largestRange(array):
    # Write your code here.
	dic = {}
	minn = float('inf')
	maxx = float('-inf')
	n = len(array)
	head = 0
	ittr = 0
	tail = 1
	counter = 0
	keeper = []

	if len(array) != 1:
		for i in range(n):
			if array[i] in dic.keys():
				dic[array[i]] +=1
			else:
				dic[array[i]] = 1
		
		# print(dic)
		dic = sorted(dic.keys())
		print(dic)
		array = dic
		new_len = len(array)

		while tail < new_len:
			# print("ittr-tail: ",(array[ittr], array[tail]))
			diff = abs(array[tail] - array[ittr]) == 1
			if diff:
				ittr+=1
				tail+=1
				counter+=1
				keeper.append((counter, f"{array[head]}@{array[ittr]}"))
			else:
				counter = 0
				ittr = tail
				head = ittr
				tail+=1

		# print(keeper)
		keeper = sorted(keeper, key=lambda x:x[0])
		print(keeper)
		keeper = keeper[-1][1].split('@')
		keeper = [int(i) for i in keeper]
		print("keeper: ",keeper)
		return keeper
	else:
		return [array[0], array[0]]








'''
Quick tip [for O(nlogn) time]:
1- Feed the array in dictionary with keys in sorted order.
2- check the current and next value with difference == 1 increment the counter 
 and store the values (head ptr & ittr ptr)in a dictionary or list
3- if two consecutive elements difference is not 1, reset the pointer values 
and set counter to 0
4- sort the dictionary or list containing largest range and return the start & end ptrs
'''
