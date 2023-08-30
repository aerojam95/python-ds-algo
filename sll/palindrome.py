# This set of classes is to create a singly-linked list data structure
# The linked class has a method removeVal which given the head of a singly 
# linked list, returns true if it is a palindrome or false otherwise.


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
    def append(self: object, val: int):
        newNode = ListNode(val)
        if self.head is None and self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail      = newNode
        self.length += 1

    # Check to see if SLL is a palindrome
    def isPalindrome1(self: object, head: object):
        startNode = head
        prevEndNode = ListNode(-1)
        endNode = head
        while startNode is not None:
            while endNode.next is not None:     
                prevEndNode = endNode
                endNode = endNode.next
            if startNode.val != endNode.val:
                return False
            prevEndNode.next = None
            endNode = head
            startNode = startNode.next
        del startNode
        del endNode
        del prevEndNode
        return True
    
    def isPalindrome2(self: object, head: object):

        start = end = head
        while end and end.next:
            start = start.next
            end = end.next.next

        prev = None
        next = None
        while start:
            next = start.next
            start.next = prev
            prev = start
            start = next

        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev.prev.next
        
        del start
        del end
        del prev
        del next
        return True