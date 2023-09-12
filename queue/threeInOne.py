# Stack class that creates three stacks from one Python list

# Date   : 12-09-2023
# Written: JAM

class MultiStack(object):
    # define multistack
    def __init__(self: object, stackSize: int):
        self.numberStacks = 3
        self.list         = [0] * (stackSize * self.numberStacks)
        self.sizes        = [0] * self.numberStacks
        self.stackSize    = stackSize

    # printing stack
    def __str__(self: object):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        self.list.reverse()
        return ' - '.join(values)

    # isFull
    def isFull(self: object, stackNum: int):
        if self.sizes[stackNum] == self.stackSize:
            return True
        else:
            return False
        
    # is Empty
    def isEmpty(self: object, stackNum: int):
        if self.sizes[stackNum] == 0:
            return True
        else:
            return False
        
    # Top element of stack
    def indexTop(self: object, stackNum: int):
        offset = stackNum * self.stackSize
        return offset + self.sizes[stackNum] - 1
    
    # push
    def push(self: object, value: any, stackNum: int):
        if self.isFull(stackNum):
            return False
        else:
            self.sizes[stackNum] += 1
            self.list[self.indexTop(stackNum)]  = value

    # pop
    def pop(self: object, stackNum: int):
        if self.isEmpty(stackNum):
            return False
        else:
            value  = self.list[self.indexTop(stackNum)]
            self.list[self.indexTop(stackNum)] = 0
            self.sizes[stackNum] -= 1
            return value
        
    # peek
    def peek(self: object, stackNum: int):
        if self.isEmpty(stackNum):
            return False
        else:
            value  = self.list[self.indexTop(stackNum)]
            return value
        
stack = MultiStack(6)
print(stack.isEmpty(1))
print(stack.isFull(0))
stack.push(1, 0)
stack.push(2, 0)
stack.push(3, 2)
print(stack.pop(0))
print(stack.peek(1))