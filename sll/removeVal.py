# This set of classes is to create a singly-linked list data structure
# The linked class has a method removeVal which given the head of a linked list
# and an integer val, removes all the nodes of the linked list that has 
# Node.val == val, and returns the new head.


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
    
    # remove elements from SLL if they have a given value
    def removeElements(self: object, head: object, val: int):
        dummyNode = ListNode(-1)
        dummyNode.next = head
        prevNode = dummyNode
        currNode = head
        while currNode:
            if currNode.val == val:
                prevNode.next = currNode.next
            else:
                prevNode = currNode
            currNode = currNode.next
        del currNode 
        del prevNode
        return dummyNode.next