class Node(object):
    def __init__(self: object, value: any):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self: object):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self: object):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self: object, value: any):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1