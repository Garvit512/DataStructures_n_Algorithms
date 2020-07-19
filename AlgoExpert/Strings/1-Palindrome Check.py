'''
$ Palindrome Check $

Problem Statement:


  Write a function that takes in a non-empty string and that returns a boolean
  representing whether the string is a palindrome.

  A palindrome is defined as a string that's written the same forward and
  backward. Note that single-character strings are palindromes.



  Sample Input:
  string = "abcdcba"

  Sample Output:
  True

'''

# O(n) time | O(1) space
def isPalindrome(string):
	head = 0
	tail = len(string)-1
	while head < tail:
		if string[head] != string[tail]:
			return False
		head+=1
		tail-=1
	return True


'''
Quick tip:
1- Initilize head and tail pointers
2- Compare both value of each pointers
3- return False if value mismatch else True
'''
