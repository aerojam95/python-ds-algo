# This set of classes is to create a singly-linked list data structure which
# takes two SLLs and combines them into one, the two inputs lists should sorted


# Date   : 30-08-2023
# Written: JAM

# Class to define a node of a SLL
class Node(object):
    def __init__(self: object, value: int = 0, next: object = None):
        self.value = value
        self.next  = next

# Singly-linked list class
class LinkedList(object):

    # Create an empty SLL 
    def __init__(self):
        self.head   = None
        self.tail   = None
        self.length = 0

    # Print SSL
    def __str__(self: object):
        tempNode = self.head
        result = ''
        while tempNode is not None:
            result += str(tempNode.value)
            if tempNode.next is not None:
                result += ' -> '
            tempNode = tempNode.next
        return result
    
    # Append to SLL
    def append(self, value):
        newNode = Node(value)
        if self.head is None and self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail      = newNode
        self.length += 1
    
    # merge 2 ordered-input SLLs into one
    def mergeSll(self: object, list1: object, list2: object):
        newList = Node(-1)
        tempNode = newList
        while list1 and list2:
            if list1.value <= list2.value:
                tempNode.next = list1
                list1 = list1.next
            else:
                tempNode.next = list2
                list2 = list2.next
            tempNode = tempNode.next
        tempNode.next = list1 if list1 is not None else list2
        self.head = newList.next
        self.tail = tempNode.next