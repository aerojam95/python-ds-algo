# A class that creates a queue that creates a queuing system for a cat or dog
# preference on dog or cat is taken on but not of the species

# Date   : 12-09-2023
# Written: JAM

# Class to define a node of a SLL
class Node(object):
    # Define node
    def __init__(self: object, species: str = None, animal: str = None):
        self.animal  = animal
        self.species = species
        self.next    = None

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
class Queue(object):
    # Define queue
    def __init__(self: object):
        self.LinkedList = LinkedList()

    # printing stack
    def __str__(self: object):
        values = [str(x.animal) for x in self.LinkedList]
        return ' - '.join(values)

    def enqueue(self: object, animal: str, species: str):
        node = Node(species, animal)
        if not self.LinkedList.head:
            self.LinkedList.head = self.LinkedList.tail= node
        else:
            self.LinkedList.tail.next = node
            self.LinkedList.tail = node
        
    def dequeueCat(self: object):
        if self.LinkedList.head is None:
            return None
        if self.LinkedList.head.next is None and self.LinkedList.head.species == "cat":
            animal = self.LinkedList.head.animal
            self.LinkedList.head = self.LinkedList.tail = None
            return animal
        if self.LinkedList.head.species == "cat":
            animal = self.LinkedList.head.animal
            self.LinkedList.head = self.LinkedList.head.next
            return animal
        else:
            prevNode = None
            currNode = self.LinkedList.head
            while currNode.species != "cat":
                prevNode = currNode
                currNode = currNode.next
        if currNode.next is None and currNode.species != "cat":
            return None
        if currNode.next is None and currNode.species == "cat":
            prevNode.next =  None
            self.LinkedList.tail = prevNode
        animal = currNode.animal
        prevNode.next = currNode.next
        currNode.next = None
        return animal
        
    def dequeueDog(self: object):
        if self.LinkedList.head is None:
            return None
        if self.LinkedList.head.next is None and self.LinkedList.head.species == "dog":
            animal = self.LinkedList.head.animal
            self.LinkedList.head = self.LinkedList.tail = None
            return animal
        if self.LinkedList.head.species == "dog":
            animal = self.LinkedList.head.animal
            self.LinkedList.head = self.LinkedList.head.next
            return animal
        else:
            prevNode = None
            currNode = self.LinkedList.head
            while currNode.species != "dog":
                prevNode = currNode
                currNode = currNode.next
        if currNode.next is None and currNode.species != "dog":
            return None
        if currNode.next is None and currNode.species == "dog":
            prevNode.next =  None
            self.LinkedList.tail = prevNode
        animal = currNode.animal
        prevNode.next = currNode.next
        currNode.next = None
        return animal
        
    def dequeueAny(self: object):
        if self.LinkedList.head is None:
            return None
        animal = self.LinkedList.head.animal
        if self.LinkedList.head.next is None:
            self.LinkedList.head = self.LinkedList.tail = None
        else:
            self.LinkedList.head = self.LinkedList.head.next
        return animal
    
queue = Queue()
queue.enqueue("cat1", "cat")
queue.enqueue("cat2", "cat")
queue.enqueue("dog1", "dog")
queue.enqueue("dog2", "dog")
print(queue)
print(queue.dequeueCat())
print(queue)
print(queue.dequeueDog())
print(queue)
print(queue.dequeueAny())
print(queue)