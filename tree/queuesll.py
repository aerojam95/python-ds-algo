# This set of classes is to create a queue data structures
# with all of its capabilites with methods and attributes


# Date   : 11-09-2023
# Written: JAM

# Class to define a node of a SLL
class Node(object):
    # Define node
    def __init__(self: object, value: any = None):
        self.value = value
        self.next  = None

    # print node
    def __str__(self: object):
        return str(self.value)

# Singly-linked list class
class LinkedList(object):
    # Define SLL 
    def __init__(self: object):
        self.head = None
        self.tail = None

    # iterable
    def __iter__(self: object):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next

# Queue using SLL
class QueueSLL(object):
    # Define queue
    def __init__(self: object):
        self.linkedList = LinkedList()

    # printing stack
    def __str__(self: object):
        values = [str(x.value) for x in self.linkedList]
        return ' - '.join(values)
    
    # isEmpty
    def isEmpty(self: object):
        if self.linkedList.head == None:
            return True
        else:
            return False

    # Enqueue
    def enqueue(self: object, value: any):
        node = Node(value)
        if self.isEmpty():
            self.linkedList.head = self.linkedList.tail = node
        else:
            self.linkedList.tail.next = node
            self.linkedList.tail = node

    # Dequeue
    def dequeue(self: object):
        if self.isEmpty():
            return False
        else:
            value  = self.linkedList.head.value
            if self.linkedList.head == self.linkedList.tail:
                self.delete()
            else:
                self.linkedList.head = self.linkedList.head.next
            return value
    # Peek
    def peek(self: object):
        if self.isEmpty():
            return False
        else:
            return self.linkedList.head.value

    # Delete
    def delete(self: object):
        self.linkedList.head = self.linkedList.tail = None