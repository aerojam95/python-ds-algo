# This set of classes is to create a queue data structures
# with all of its capabilites with methods and attributes


# Date   : 11-09-2023
# Written: JAM

# Class to define a queue using a list data structure with no fixed capacity
class Queue(object):
    # defining attributes
    def __init__(self: object):
        self.list = []

    # printing queue
    def __str__(self: object):
        values = [str(x) for x in self.list]
        return ' - '.join(values)
    
    #  isEmpty
    def isEmpty(self: object):
        if self.list == []:
            return  True
        else:
            return False
        
    # Enqueue
    def enqueue(self: object, value: any):
        self.list.append(value)
        return True
    
    # dequeue
    def dequeue(self: object):
        if self.isEmpty():
            return False
        else:
            return self.list.pop(0)
        
    # peek
    def peek(self: object):
        if self.isEmpty():
            return False
        else:
            return self.list[0]
        
    # Delete
    def delete(self: object):
        self.list = None
        return self.list
    

# Class to define a queue using a list data structure with fixed capacity
class CircularQueue(object):
    # defining attributes
    def __init__(self: object, maxSize: int):
        self.list = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    # printing queue
    def __str__(self: object):
        values = [str(x) for x in self.list]
        return ' - '.join(values)
    
    # isFull
    def isFull(self: object):
        if self.top + 1 == self.start:
            return True
        elif (self.start == 0) and (self.top + 1 == self.maxSize):
            return True
        else:
            return False
        
    # isEmpty
    def isEmpty(self: object):
        if self.top == -1:
            return True
        else:
            return False
    
    # enqueue
    def enqueue(self: object, value: any):
        if self.isFull():
            return False
        else:
            if self.top + 1 == self.maxSize:
                self.top =  0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.list[self.top] = value
            return True
        
    # dequeue
    def dequeue(self: object):
        if self.isEmpty():
            return False
        else:
            element1 = self.list[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start +  1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.list[start] = None
            return element1
        
    # peek
    def peek(self: object):
        if self.isEmpty():
            return False
        else:
            return self.list[self.start]
        
    # delete
    def delete(self: object):
        self.list = self.maxSize * [None]
        self.top = -1
        self.start = -1
        return self.list
    
# queue using a SLL

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
    


queue = QueueSLL()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)
print(queue.dequeue())
print(queue)
print(queue.peek())
print(queue.delete())