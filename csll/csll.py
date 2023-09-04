# This set of classes is to create a circular singly-linked list data structure
# with all of its capabilites with methods and attributes


# Date   : 31-08-2023
# Written: JAM

# Class to define  sll node
class Node(object):
    def __init__(self: object, value: any):
        self.value = value
        self.next  = None


# Circular singly-linked list class
class CircularSinglyLinkedList(object):
    
    # intialise csll 
    def __init__(self: object):
        self.head   = None
        self.tail   = None

    # iterate print over csll
    def __iter__(self: object):
        node = self.head
        while node:
            yield node
            node = node.next
            if node.next == self.tail.next:
                break

    # create csll
    def create(self: object, value: any):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node

    # prepend csll
    def prepend(self: object, value: any):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.tail.next = newNode

    # insert to csll
    def insert(self: object, value: any, index: int):
        if self.head is None:
            return f"The head reference is {None}"
        else:
            newNode = Node(value)
            if index == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif index == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                counter = 0
                while counter < index - 1:
                    tempNode = tempNode.next
                    counter += 1
                newNode.next = tempNode.next
                tempNode.next = newNode
            return f"Insertion of {value} at {index}"
    
    # append csll
    def append(self: object, value: any):
        newNode = Node(value)
        newNode.next = self.tail.next
        self.tail.next = newNode
        self.tail = newNode

    # traverse csll
    def traverse(self: object):
        if self.head is None:
            return f"There are no elements in CSLL"
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break
        return f"CSLL traversed"
    
    # search csll
    def search(self: object, value: any):
        if self.head is None:
            return f"There are no elements in CSLL with value {value}"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    return True
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return False
                
    # popFirst csll
    def popFirst(self: object):
        if self.head is None:
            return f"There are no elements in CSLL"
        else:
            if self.head == self.tail:
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
            return True
        
    # remove from csll
    def remove(self: object, index: int):
        if self.head is None:
            return f"There are no elements in CSLL"
        else:
            if index == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif index == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head.next
                    while tempNode != self.tail.next:
                        if tempNode.next == self.tail:
                            break
                        tempNode = tempNode.next
                    tempNode.next = self.tail.next
                    self.tail = tempNode
            else:
                tempNode = self.head
                counter = 0
                while counter < index - 1:
                    tempNode = tempNode.next
                    counter += 1
                tempNode.next = tempNode.next.next
            return True
        
    # pop csll
    def pop(self: object):
        if self.head is None:
            return f"There are no elements in CSLL"
        else:
            if self.head == self.tail:
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                tempNode = self.head.next
                while tempNode != self.tail.next:
                    if tempNode.next == self.tail:
                        break
                    tempNode = tempNode.next
                tempNode.next = self.tail.next
                self.tail = tempNode
            return True
        
    # delete csll
    def delete(self: object):
        if self.head is None:
            return f"There are no elements in CSLL"
        else:
            self.head = None
            self.tail.next = None
            self.tail = None
            return True