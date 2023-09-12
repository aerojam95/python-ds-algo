# Stack class that has a method to find minimum element of the stack
#  push, pop, min: O(1)

# Date   : 12-09-2023
# Written: JAM

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
        self.min  = None

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
        return ' - '.join(values)
    
    # isEmpty
    def isEmpty(self: object):
        if self.LinkedList.head is None:
            return True
        else:
            return False
    
    # Push 
    def push(self: object, value: any):
        node = Node(value)
        if self.isEmpty():
            self.LinkedList.head = self.LinkedList.min = node
            return True
        if self.LinkedList.min.value > value:
            minNode = node
            minNode.next = self.LinkedList.min
            self.LinkedList.min = minNode
        node.next = self.LinkedList.head
        self.LinkedList.head = node
        return True

    
    # Pop
    def  pop(self: object):
        if self.isEmpty():
            return None
        popNode = self.LinkedList.head.value
        if self.LinkedList.min ==  self.LinkedList.head:
            self.LinkedList.min = self.LinkedList.min.next
        self.LinkedList.head = self.LinkedList.head.next
        return popNode
        
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

    # min
    def stackMin(self: object):
        if not self.LinkedList.min:
            return None
        return  self.LinkedList.min.value
    
stack =  StackSLL()
print(stack.LinkedList.head)
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print(stack.stackMin())
print(stack.pop())
print(stack.stackMin())
print(stack)
print(stack.pop())
print(stack.stackMin())
print(stack)
print(stack.delete())