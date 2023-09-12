# A class that creates a queue stacks with two stacks of given maxSize. 
# When a stack 1 is Full it reverses the stack by enqueuing to stack 2, an 
# element is popped and then stack 2 is dequeued to stack 1

# Date   : 12-09-2023
# Written: JAM

class Stack(object):
    # Define attributes
    def __init__(self: object):
        self.list = []

    # length of stack
    def __len__(self: object):
        return len(self.list)
    
    # push
    def push(self: object, value: any):
        self.list.append(value)

    # pop
    def pop(self: object):
        if len(self.list) == 0:
            return None
        else:
            return self.list.pop()

class Queue(object):
    # Define attributes
    def __init__(self: object):
        self.inStack = Stack()
        self.outStack = Stack()

    # enqueue
    def enqueue(self: object, value: any):
        self.inStack.push(value)

    # dequeue
    def dequeue(self: object):
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        result  = self.outStack.pop()
        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        return result
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.dequeue())
queue.enqueue(5)
print(queue.dequeue())