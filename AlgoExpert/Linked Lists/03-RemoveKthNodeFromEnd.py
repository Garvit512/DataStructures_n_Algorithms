# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    aux_ptr = head
    previous = head
    current = head
    counter = 0

    while aux_ptr.next is not None:
        aux_ptr = aux_ptr.next
    # print(ittr.value)
    idx = (aux_ptr.value-k)+1
    print("idx:", idx)

    def getList(head):
        L = []
        ittr = head
        while ittr is not None:
            L.append(ittr.value)
            ittr = ittr.next
        return L

    if k == aux_ptr.value+1:
        print("head.value:", head.value)
        print("head.next.value", head.next.value)
        print(getList(head))

        current = current.next
        head = current
        print("head.value:", head.value)
        print("head.next.value", head.next.value)
        print(getList(head))
        print("head:", head, '\n')
        print("previous:", previous)
        previous.value = current.value
        previous.next = current.next

    else:
        while counter != idx:
            print("inside while loop")
            previous = current
            current = current.next
            counter += 1
        # print(previous.value, current.value)
        previous.next = current.next
        current.next = None
        print("head.value:", head.value)
        print(getList(head))
    pass
