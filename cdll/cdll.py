# This set of classes is to create a circular doubly-linked list data structure
# with all of its capabilites with methods and attributes


# Date   : 04-09-2023
# Written: JAM

# Class to define a cdll node
class Node(object):
    def __init__(self: object, value: any):
        self.value = value
        self.next  = None
        self.prev = None

# Circular doubly-linked list class
class CircularDoublyLinkedList(object):

    # Initialise cdll
    def __init__(self: object):
        self.head = None
        self.tail = None

    # Print elements of dll
    def __iter__(self: object):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    # create cdll
    def createCdll(self: object, value: any):
        node = Node(value)
        self.head = node
        self.tail = node
        node.prev = node
        node.next = node
        return "cdll created"
    
    # prepend cdll
    def prependCdll(self:  object, value: any):
        if self.head is None:
            return "No dll to append"
        node = Node(value)
        node.next = self.head
        self.head.prev = node
        node.prev = self.tail
        self.tail.next = node
        self.head = node
        return "cdll prepended"
    
    # append cdll
    def appendCdll(self:  object, value: any):
        if self.head is None:
            return "No dll to append"
        node = Node(value)
        node.prev = self.tail
        self.tail.next = node
        node.next = self.head
        self.head.prev = node
        self.tail = node
        return "cdll appended"
    
    # insert into to cdll
    def insertCdll(self: object, value: any, element: int):
        if self.head is None:
            return f"No dll to insert {value}"
        if element == 0:
            self.prependCdll(value)
        elif element == -1:
            self.appendCdll(value)
        else:
            tempNode = self.head
            index = 0
            while index < element - 1:
                tempNode = tempNode.next
                index += 1
                if tempNode == self.tail.next:
                    return f"{element} is out of list range"
            node = Node(value)
            node.prev = tempNode
            node.next = tempNode.next
            tempNode.next.prev = node
            tempNode.next = node
            return "cdll inserted"
        
    # traverse cdll
    def traverseCdll(self: object):
        if self.head is None:
            return f"No dll to traverse"
        tempNode = self.head
        while tempNode:
            print(tempNode.value)
            tempNode = tempNode.next
            if tempNode == self.tail.next:
                break
        return "cdll traversed"
    
    # Reverse traverse cdll
    def reverseTraverseCdll(self: object):
        if self.head is None:
            return f"No dll to reverse traverse"
        tempNode = self.tail
        while tempNode:
            print(tempNode.value)
            tempNode = tempNode.prev
            if tempNode == self.head.prev:
                break
        return "cdll reverse traversed"

    # Search cdll
    def searchCdll(self: object, value: any):
        if self.head is None:
            return f"No dll to search for {value}"
        tempNode = self.head
        while tempNode:
            if  tempNode.value == value:
                return True
            tempNode = tempNode.next
            if tempNode == self.tail.next:
                break
        return False
    
    # First pop cdll
    def firstPopCdll(self: object):
        if self.head is None:
            return f"No dll to be first popped"
        if self.head == self.tail:
            self.head.next = self.head.prev = None
            self.head = self.tail = None 
        else:
            self.tail.next = self.head.next
            self.head.next.prev = self.tail
            self.head = self.head.next
        return f"cdll first popped"
    
    # Pop cdll
    def popCdll(self: object):
        if self.head is None:
            return f"No dll to be popped"
        if self.head == self.tail:
            self.head.next = self.head.prev = None
            self.head = self.tail = None 
        else:
            self.head.prev = self.tail.prev
            self.tail.prev.next = self.head
            self.tail = self.tail.prev
        return f"cdll popped"
    
    # remove from cdll
    def removeCdll(self: object, element: int):
        if self.head is None:
            return f"No cdll to delete element {element}"
        if element == 0:
            self.firstPopCdll()
        elif  element == -1:
            self.popCdll()
        else:
            tempNode = self.head
            index = 0
            while index < element - 1:
                tempNode = tempNode.next
                index += 1
                if tempNode == self.tail.next:
                    return f"{element} is out of list range"
            tempNode.next = tempNode.next.next
            tempNode.next.prev = tempNode
        return f"element {element} removed from cdll"
    
    # delete cdll
    def deleteCdll(self: object):
        if self.head is None:
            return f"No cdll to delete"
        tempNode = self.head
        self.tail.next = None
        while tempNode:
            tempNode.prev = None
            tempNode = tempNode.next
        self.head = self.tail = None
        return f"cdll deleted"