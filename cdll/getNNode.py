# This function gets nth node from a linked list defined by linkedlist.py

# Date   : 05-09-2023
# Written: JAM

from ll import LinkedList

def getNNode(ll: object, element: int):
    if ll.head is None:
        return None
    p1 = ll.head
    p2 = ll.head
    for _ in range(element):
        if p2 is None:
            return None
        p2 = p2.next
    while p2:
        p1 = p1.next
        p2 = p2.next
    return p1

ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
print(getNNode(ll, 3))