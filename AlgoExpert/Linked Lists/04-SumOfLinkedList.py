# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Aux function


def getList(head_of_linkedlist):
	L = []
	ittr = head_of_linkedlist
	while ittr is not None:
		L.append(ittr.value)
		ittr = ittr.next
	return L

# Aux class


class LinkedlistCreator:
	def __init__(self):
		self.head = None
		self.tail = None

	def creator(self, data):
		node = LinkedList(int(data))
		if self.head == None:
			self.head = node
			self.tail = node
			node.next = None
		else:
			ittr = self.head
			while ittr.next is not None:
				ittr = ittr.next
			ittr.next = node
			node.next = None
			self.tail = node

		return self.head


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
	firstLinkedList_list = getList(linkedListOne)
	firstLinkedList_list.reverse()
	firstLinkedList_digits = int(''.join([str(s) for s in firstLinkedList_list]))
	print(firstLinkedList_digits)

	secondLinkedList_list = getList(linkedListTwo)
	secondLinkedList_list.reverse()
	secondLinkedList_digits = int(
	    ''.join([str(s) for s in secondLinkedList_list]))
	print(secondLinkedList_digits)

	new_digits = firstLinkedList_digits + secondLinkedList_digits
	print(new_digits)

	new_digits = [digit for digit in str(new_digits)]
	new_digits.reverse()
	print(new_digits)

	obj = LinkedlistCreator()
	for i in new_digits:
		res = obj.creator(i)
    return res
