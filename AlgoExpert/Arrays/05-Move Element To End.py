'''
$ Move Element To End $

Problem Statement:


  
  You're given an array of integers and an integer. Write a function that moves
  all instances of that integer in the array to the end of the array and returns
  the array.

  The function should perform this in place (i.e., it should mutate the input
  array) and doesn't need to maintain the order of the other integers.



  Sample Input:
  array  = [2, 1, 2, 2, 2, 3, 4, 2]
  toMove = 2

  Sample Output:
  [1, 3, 4, 2, 2, 2, 2, 2] // the numbers 1, 3, and 4 could be ordered differently

'''

# O(n) time | O(n) space


def moveElementToEnd(array, toMove):
    dic = {}

    if len(array) == 1 or toMove not in array:
        return array

    for i in array:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1

    temp_array = [i for i in array if toMove != i]
    toMove_len = dic[toMove]

    for i in range(toMove_len):
        temp_array.append(toMove)

    return temp_array


'''
Quick tip:
1- Create an empty dictionary to keep the elements with their counts.
2- Create another list without 'toMove' element.
3- append 'toMove' in new list till it's count. 
'''
