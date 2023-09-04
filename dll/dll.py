# This set of classes is to create a doubly-linked list data structure
# with all of its capabilites with methods and attributes


# Date   : 04-09-2023
# Written: JAM

# Class to define a dll node
class Node(object):
    def __init__(self: object, value: any):
        self.value = value
        self.next  = None
        self.prev = None

# Doubly-linked list class
class DoublyLinkedList(object):

    # Initialise dll
    def __init__(self:object):
        self.head = None
        self.head = None

    # Print elements of dll
    def __iter__(self:object):
        node = self.head
        while node:
            yield node
            node = node.next

    # Create dll
    def createDll(self: object, value: any):
        node = Node(value)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "dll created"
    
    #  Prepend dll
    def prependDll(self: object, value: any):
        if self.head is None:
            return "No dll to prepend"
        node = Node(value)
        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node
        return "dll prepended"
    
    # Append dll
    def appendDll(self: object, value: any):
        if self.head is None:
            return "No dll to append"
        node = Node(value)
        node.next = None
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        return "dll appended"
    
    # Insert into dll
    def insertDll(self: object, value: any, element: int):
        if self.head is None:
            return "No dll to insert"
        if element == 0:
            self.prependDll(value)
        elif element == -1:
            self.appendDll(value)
        else:
            node = Node(value)
            tempNode = self.head
            index = 0
            while index < element - 1:
                tempNode == tempNode.next
                index += 1
                if (tempNode.next == None) and  (tempNode == self.tail):
                    return "insert is out of dll dimension"
            node.next = tempNode.next
            node.prev = tempNode
            node.next.prev = node
            tempNode.next = node
            return "inserted to dll"
    
    # Traverse dll
    def traverseDll(self: object):
        if self.head is None:
            return "No dll to traverse"
        tempNode = self.head
        while tempNode:
            print(tempNode.value)
            tempNode = tempNode.next
        return "dll traversed"

    # Reverse traverse dll
    def reverseTraverseDll(self: object):
        if self.head is None:
            return "No dll to reverse traverse"
        tempNode = self.tail
        while tempNode:
            print(tempNode.value)
            tempNode = tempNode.prev
        return "dll reverse traversed"

    # Search dll
    def searchDll(self: object, value: any):
        if self.head is None:
            return "No dll to search"
        tempNode = self.head
        while tempNode:
            if tempNode.value == value:
                return tempNode.value
            tempNode = tempNode.next
        return f"{value} is not in dll"
    
    # Pop_first dll
    def firstPopDll(self: object):
        if self.head is None:
            return "No dll to remove first element"
        popNode = self.head
        if self.head.next is not None:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = self.tail = None
        return popNode.value


    # pop dll
    def popDll(self: object):
        if self.head is None:
            return "No dll to remove last element"
        popNode = self.tail
        if  self.head.next is not None:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.head = self.tail = None
        return popNode.value

    # Remove element from dll
    def removeDll(self: object, element: int):
        if self.head is None:
            return f"No dll to remove element {element}"
        if element == 0:
            self.firstPopDll()
        elif element == -1:
            self.popDll()
        else:
            curNode = self.head
            index = 0
            while index < element - 1:
                curNode = curNode.next
                index += 1
            delNode = curNode.next
            curNode.next = curNode.next.next
            curNode.next.prev = curNode
            return delNode
        
    # Delete dll
    def deleteDll(self : object):
        if self.head is None:
            return f"No dll to delete"
        tempNode = self.head
        while tempNode:
            tempNode.prev = None
            tempNode = tempNode.next
        self.head = self.tail = None
        return "dll deleted"
        

dll = DoublyLinkedList()
dll.createDll(5)
print([node.value for node in dll])
dll.insertDll(0,0)
print([node.value for node in dll])
dll.insertDll(2,-1)
print([node.value for node in dll])
dll.appendDll(3)
dll.prependDll(2)
print([node.value for node in dll])
dll.traverseDll()
dll.reverseTraverseDll()
print(dll.searchDll(5))
dll.firstPopDll()
print([node.value for node in dll])
dll.popDll()
print([node.value for node in dll])
dll.removeDll(1)
print([node.value for node in dll])
dll.deleteDll()
print([node.value for node in dll])
