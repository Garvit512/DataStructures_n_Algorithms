'''
$ Longest Peak $

Problem Statement:


  Write a function that takes in an array of integers and returns the length of
  the longest peak in the array.

  A peak is defined as adjacent integers in the array that are strictly 
  increasing until they reach a tip (the highest value in the peak), at which
  point they become strictly decreasing. At least three integers are required to
  form a peak.

  For example, the integers 1, 4, 10, 2  form a peak, but the integers 4, 0, 10 don't 
  and neither do the integers 1, 2, 2, 0 . Similarly, the integers 1, 2, 3  don't
  form a peak because there aren't any strictly decreasing integers after the 3

  Sample Input:
  array  = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

  Sample Output:
  6 // 0, 10, 6, 5, -1, -3

'''

# O(n) time | O(1) space


def longestPeak(array):

    peak = 0
    i = 1
    while i < len(array)-1:
        isPeak = array[i-1] < array[i] and array[i] > array[i+1]
        if not isPeak:
            i += 1
            continue

        leftIdx = i - 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx+1]:
            leftIdx -= 1

        rightIdx = i + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx-1]:
            rightIdx += 1

        currentPeak = rightIdx-leftIdx-1
        peak = max(currentPeak, peak)
        i = rightIdx
    return peak


'''
Quick tip:
1- The first goal is to find the peak i.e the left and right value of an element 
   should be smaller
2- now instead of finding all the peaks first and then compare each one of them, 
   we find the peak and expend it in left(using leftIdx) and right(using rightIdx) 
   till the peak goes i.e till we are getting minimum value each time 
   (which satisfies peak condition)
3- in right we've assign rightIdx to i coz we are starting the new index where the 
   1st peak ends i.e where the rightIdx stops/ends.
'''
