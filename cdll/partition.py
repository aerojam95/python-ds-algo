# This function gets partition a linked list defined by ll.py around an
# argument x, values less than x are prepended, values great thn or equal to x
# are appended

# Date   : 05-09-2023
# Written: JAM

from ll import LinkedList

def partition(ll: object, pivot: int):

    currNode = ll.head
    ll.tail  = ll.head

    while currNode:
        nextNode = currNode.next
        currNode.next = None
        if currNode.value < pivot:
            currNode.next = ll.head
            ll.head = currNode
        else:
            ll.tail.next = currNode
            ll.tail = currNode
        currNode = nextNode

    if ll.tail.next is not None:
        ll.tail.next = None
    
ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
partition(ll, 20)
print(ll)