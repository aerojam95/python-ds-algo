# This set of classes is to create a  general linked list data structure
# with all of its capabilites with methods and attributes


# Date   : 05-09-2023
# Written: JAM

# Import libraries
import random as random

# Class to define a cdll node
class Node(object):
    # define node
    def __init__(self: object, value: any = None):
        self.value = value
        self.next  = None
        self.prev = None

    # Print node values
    def __str__(self: object):
        return str(self.value)
    
class LinkedList(object):
    # define ll
    def __init__(self: object):
        self.head = None
        self.tail = None

    # Print elements of dll
    def __iter__(self: object):
        node = self.head
        while node:
            yield node
            node = node.next

    # Print node values in ll
    def __str__(self: object):
        values = [str(x.value) for x in self]
        return " -> ".join(values)
    
    # Length of ll
    def __len__(self: object):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result
    
    # Add node to ll
    def add(self: object, value: int):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        return self.tail
    
    # Generate new ll
    def generate(self: object, n: int, min_value: int, max_value: int):
        self.head = self.tail = None
        for _ in range(n):
            self.add(random.randint(min_value, max_value))
        return self