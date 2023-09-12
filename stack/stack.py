# This set of classes is to create a stack data structures
# with all of its capabilites with methods and attributes


# Date   : 11-09-2023
# Written: JAM

# Class to define a stack using a list data structure with no size limit
class Stack(object):
    # defining attributes
    def __init__(self: object):
        self.list = []

    # printing stack
    def __str__(self: object):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        self.list.reverse()
        return '\n'.join(values)
    
    # isEmpty
    def isEmpty(self: object):
        if self.list == []:
            return True
        else:
            return False
        
    # push
    def push(self: object, value: any):
        self.list.append(value)
        return True
    
    # pop
    def pop(self: object):
        if self.isEmpty():
            return False
        else:
            return self.list.pop()
        
    # peek
    def peek(self: object):
        if self.isEmpty():
            return False
        else:
            return self.list[len(self.list) - 1]

    # delete stack
    def delete(self: object):
        self.list = None
        return self.list

# Stack data structure with a max size list 
class StackSize(object):
    # defining attributes
    def __init__(self: object, maxSize: int):
        self.maxSize =  maxSize
        self.list = []

    # printing stack
    def __str__(self: object):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        self.list.reverse()
        return '\n'.join(values)
    
    # isEmpty
    def isEmpty(self: object):
        if self.list == []:
            return True
        else:
            return False
    
    # is Full
    def isFull(self: object):
        if len(self.list)  == self.maxSize:
            return True
        else:
            return False
        
    # push
    def push(self: object, value: any):
        if self.isFull():
            return False
        else:
            self.list.append(value)
            return True
        
    # pop
    def pop(self: object):
        if self.isEmpty():
            return False
        else:
            return self.list.pop()
        
    # peek
    def peek(self: object):
        if self.isEmpty():
            return False
        else:
            return self.list[len(self.list) - 1]
        
    # delete stack
    def delete(self: object):
        self.list  = None
        return self.list
    
# stack using a SLL
# Class to define a node of a SLL
class Node(object):
    # Define node
    def __init__(self: object, value: any = None):
        self.value = value
        self.next  = None

# Singly-linked list class
class LinkedList(object):
    # Define SLL 
    def __init__(self: object):
        self.head = None

    # iterable
    def __iter__(self: object):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next

# Stack using SLL
class StackSLL(object):
    # Define stack
    def __init__(self: object):
        self.LinkedList = LinkedList()

    # printing stack
    def __str__(self: object):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)
    
    # isEmpty
    def isEmpty(self: object):
        if self.LinkedList.head is None:
            return True
        else:
            return False
    
    # Push 
    def push(self: object, value: any):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
        return True
    
    # Pop
    def  pop(self: object):
        if self.isEmpty():
            return False
        else:
            value = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return value
        
    # Peek
    def peek(self: object):
        if self.isEmpty():
            return False
        else:
            value = self.LinkedList.head.value
            return value
        
    # delete
    def delete(self: object):
        self.LinkedList.head = None