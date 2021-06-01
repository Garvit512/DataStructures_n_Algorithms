# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
	# code with print statements is in Solution 2
	a_ptr = linkedList
	b_ptr = linkedList.next
	aux_ptr = None
	ittr = linkedList

	while ittr.next is not None:
		if a_ptr.value == b_ptr.value:
			aux_ptr = b_ptr.next
			a_ptr.next = aux_ptr
			b_ptr.next = None
			b_ptr = aux_ptr
			if aux_ptr == None:
				break
			else:
				pass
		else:
			a_ptr = b_ptr
			b_ptr = b_ptr.next
			ittr = ittr.next

    return linkedList
