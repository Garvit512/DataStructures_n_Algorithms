# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# ----> In constant space <-------
def findLoop(head):
    # Write your code here.
    slowPtr = head.next
    fastPtr = head.next.next

    while slowPtr != fastPtr:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next
        print((slowPtr.value, fastPtr.value))

    slowPtr = head

    print((slowPtr.value, fastPtr.value))
    print("Starting search for loop 1st node")
    while slowPtr != fastPtr:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next
        print((slowPtr.value, fastPtr.value))

    return slowPtr
