# This function removes duplicate from a linked list defined by linkedlist.py

# Date   : 05-09-2023
# Written: JAM

from linkedlist import LinkedList

def remove_duplicates(ll: object):
    if ll.head is None:
        return f"ll is empty"
    if  ll.head.next is None:
        return  f"ll has only 1 element"
    prevNode = None
    currNode = ll.head
    while currNode:
        tempNode = currNode
        while tempNode.next:
            if tempNode.next.value == currNode.value:
                tempNode.next = tempNode.next.next
            else:
                tempNode = tempNode.next
        prevNode = currNode
        currNode = currNode.next
    ll.tail = prevNode
    return ll.head



ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(4)
ll.append(4)
ll.append(6)
ll.append(5)
ll.append(6)
print(ll)
remove_duplicates(ll)
print(ll)
print(ll.tail.value)
print(ll.head.value)