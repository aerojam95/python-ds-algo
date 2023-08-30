# This set of classes is to create a singly-linked list data structure which
# takes a SLL given the head of it, deletes all duplicates such that each
# element appears only once. Returning the SLL sorted as well. 


# Date   : 30-08-2023
# Written: JAM

# Class to define a node of a SLL
class ListNode(object):
    def __init__(self: object, val: int = 0, next: object = None):
        self.val = val
        self.next = next

class Solution(object):
    # Create an empty SLL 
    def __init__(self: object):
        self.head   = None
        self.tail   = None
        self.length = 0

    # Print SSL
    def __str__(self: object):
        tempNode = self.head
        result = ''
        while tempNode is not None:
            result += str(tempNode.val)
            if tempNode.next is not None:
                result += ' -> '
            tempNode = tempNode.next
        return result
    
    # Append to SLL
    def append(self, val):
        newNode = ListNode(val)
        if self.head is None and self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail      = newNode
        self.length += 1

    # Delete duplicate elements of SLL
    def deleteDuplicates(self, head):
        if head is None:
            return None
        currentNode = head
        while currentNode is not None and currentNode.next is not None:
            if currentNode.val == currentNode.next.val:
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next
        del currentNode
        return head