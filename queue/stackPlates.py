# Stack class that creates stacks of given maxSize. When a stack is Full it 
# creates a new stack

# Date   : 12-09-2023
# Written: JAM

class SetOfStacks(object):
    # Define attributes
    def __init__(self: object, stackSize: int):
        self.stacks    = []
        self.stackSize = stackSize

    # printing stack
    def __str__(self: object):
        return self.stacks
    
    # push
    def push(self: object, value: any):
        if len(self.stacks) > 0 and (len(self.stacks[-1]) < self.stackSize):
            self.stacks[-1].append(value)
        else:
            self.stacks.append([value])

    # pop
    def pop(self: object):
        while (len(self.stacks) > 0) and (len(self.stacks[-1]) == 0):
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()

    # popAt
    def popAt(self: object, stackNumber: int):
        if len(self.stacks) > 0:
            return self.stacks[stackNumber].pop()
        else:
            return None
        
stack = SetOfStacks(3)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.pop())
print(stack.popAt(1))