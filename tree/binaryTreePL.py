# A class to define a binary tree DS with Python lists

# Date   : 25-09-2023
# Written by: JAM

class BinaryTreePL(object):
    def __init__(self: object, size: int):
      self.list = size * [None]
      self.lastIndexUsed = 0
      self.maxSize = size

    def insertNode(self: object, value: any):
       if self.lastIndexUsed + 1 == self.maxSize:
          # tree is full as there is a fixed size set in the objects definition
          return False
       self.list[self.lastIndexUsed + 1] = value
       self.lastIndexUsed += 1
       return True
    
    def serachNode(self: object, value: any):
       for i in range(self.maxSize):
          if self.list[i] == value:
             return True
       return False
    
    # root -> left  -> right
    def preOrderTraversal(self: object, index: int):
       if index > self.lastIndexUsed:
          return
       print(self.list[index])
       self.preOrderTraversal(index * 2)
       self.preOrderTraversal(index * 2 + 1)

    # left -> root -> right
    def inOrderTraversal(self: object, index: int):
       if index > self.lastIndexUsed:
          return
       self.inOrderTraversal(index * 2)
       print(self.list[index])
       self.inOrderTraversal(index * 2 + 1)

    # left -> right -> root
    def postOrderTraversal(self: object, index: int):
        if index > self.lastIndexUsed:
            return
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2 + 1)
        print(self.list[index])

    # left -> right level by level
    def levelOrderTraversal(self: object, index: int):
       for i in range(index, self.lastIndexUsed + 1):
          print(self.list[i])

    # delete a node from BT and replace with furthest right leaf
    def deleteNode(self: object, value: any):
       if self.lastIndexUsed == 0:
          return False
       for i in range(1, self.lastIndexUsed + 1):
          if self.list[i] == value:
             self.list[i] = self.list[self.lastIndexUsed]
             self.list[self.lastIndexUsed] = None
             self.lastIndexUsed -= 1

    # delete BT
    def deleteBT(self: object):
       if self.lastIndexUsed == 0:
          return True
       self.list = None
       return True
       
       

newBT = BinaryTreePL(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")
newBT.preOrderTraversal(1)
newBT.inOrderTraversal(1)
newBT.postOrderTraversal(1)
newBT.levelOrderTraversal(1)
newBT.deleteNode("Hot")
newBT.levelOrderTraversal(1)
newBT.deleteBT()