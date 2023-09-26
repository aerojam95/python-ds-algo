# A class to define a binary search tree DS with LL

# data   : 26-09-2023
# Written by: JAM

from queuesll import QueueSLL

class BSTNode(object):
    # Define tree node object
    def __init__(self: object, data: any = None):
        self.data = data
        self.leftChild = None
        self.rightChild = None

# insert node to BST log(n) time and space complexity
def insertNode(rootNode: object, value: any):
    if rootNode.data == None:
        rootNode.data = value
    elif value <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(value)
        else:
            insertNode(rootNode.leftChild, value)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(value)
        else:
            insertNode(rootNode.rightChild, value)
    return True

# root -> left  -> right
def preOrderTraversal(rootNode: object):
    if rootNode is None:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

# left -> root -> right
def inOrderTraversal(rootNode: object):
    if rootNode is None:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

# left -> right -> root
def postOrderTraversal(rootNode: object):
    if rootNode is None:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

# left -> right level by level
def levelOrderTraversal(rootNode: object):
    if rootNode is None:
        return
    else:
        queue = QueueSLL()
        queue.enqueue(rootNode)
        while not(queue.isEmpty()):
            root = queue.dequeue()
            print(root.data)
            if (root.leftChild is not None):
                queue.enqueue(root.leftChild)
            if (root.rightChild is not None):
                queue.enqueue(root.rightChild)

# search for value in BST log(n) time and space complexity
def searchBST(rootNode: object, value: any):
    if rootNode is None:
        return False
    if rootNode.data == value:
        print("Element in BST")
        return True
    elif value < rootNode.data:
        if rootNode.leftChild.data == value:
            print("Element in BST")
            return True
        else:
            searchBST(rootNode.leftChild, value)
    else:
        if rootNode.rightChild.data == value:
            print("Element in BST")
            return True
        else:
            searchBST(rootNode.rightChild, value)

# Minimum value node
def minNode(rootNode: object):
    currNode = rootNode
    while (currNode.leftChild is not None):
        currNode = currNode.leftChild
    return currNode

# Delete node from binary search tree
def deleteNode(rootNode: object, value: any):
    if rootNode is None:
        return rootNode
    if value < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, value)
    elif value > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, value)
    else:
        if rootNode.leftChild is None:
            tempNode = rootNode.rightChild
            rootNode = None
            return tempNode
        if rootNode.rightChild is None:
            tempNode = rootNode.leftChild
            rootNode = None
            return tempNode
        tempNode = minNode(rootNode.rightChild)
        rootNode.data = tempNode.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, tempNode.data)
    return rootNode

# delete BST
def deleteBT(rootNode: object):
    if rootNode is None:
        return True
    else:
        rootNode.data = None
        rootNode.leftChild = None
        rootNode.rightChild = None
        return True