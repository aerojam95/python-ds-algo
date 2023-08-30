# This set of classes is to create a singly-linked list data structure with
# all of its capabilites with methods and attributes


# Date   : 29-08-2023
# Written: JAM

# Class to define a node of a SLL
class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None

# Singly-linked list class
class LinkedList:
    
    # Create an empty SLL 
    def __init__(self):
        self.head   = None
        self.tail   = None
        self.length = 0

    # Print SSL
    def __str__(self):
        tempNode = self.head
        result = ''
        while tempNode is not None:
            result += str(tempNode.value)
            if tempNode.next is not None:
                result += ' -> '
            tempNode = tempNode.next
        return result

    # Prepend to SLL
    def prepend(self, value):
        newNode = Node(value)
        if self.head is None & self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head    = newNode
        self.length  += 1

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

    # insert into SLL
    def insert(self, index, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
    
    # Traverse SLL
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
    
    # Check if element is in SLL
    def check(self, target):
        current = self.head
        while current is not None:
            if current.value == target:
                return True
            current = current.next
        return False
    
    # Find index of an element in SLL
    def search(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1
    
    # Get Sll element
    def get(self, index):
        if index == -1:
            return self.tail
        elif index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    # Set value in SLL
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    # Delete first element of SLL
    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    # Delete last element of SLL
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp
        self.length -= 1
        return popped_node
    
    # Delete an element of SLL
    def remove(self, index):
        if index < -1 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == -1 or index == self.length-1:
            return self.pop()
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node
    
    # Reverse SLL
    def reverse(self):
        prevNode = None
        currentNode = self.head
        nextNode = None
        while currentNode is not None:
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
        self.head, self.tail = self.tail, self.head

    # find middle node of SLL
    def middle(self):
        middleNode = self.head
        traverseNode = self.head
        while traverseNode is not None and traverseNode.next is not None:
            middleNode = middleNode.next
            traverseNode = traverseNode.next.next
        return middleNode.value

    # Remove duplicates in SLL
    def removeDup(self):
        if self.head is None:
            return None
        values = []
        prevNode = None
        currentNode = self.head
        while currentNode is not None:
            if currentNode.value in values:
                prevNode.next = currentNode.next
                self.length -= 1
                if currentNode.next is None:
                    self.tail = prevNode
            else:
                values.append(currentNode.value)
                prevNode = currentNode
                if currentNode.next is None:
                    self.tail = currentNode
            currentNode = currentNode.next
        del values
        del prevNode
        del currentNode