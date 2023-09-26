# A class to define an AVL tree DS with LL

# data   : 26-09-2023
# Written by: JAM

from queuesll import QueueSLL

class AVLNode(object):
    # Define tree node object
    def __init__(self: object, data: any = None):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

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

# search for value in AVL log(n) time and space complexity
def searchAVL(rootNode: object, value: any):
    if rootNode is None:
        return False
    if rootNode.data == value:
        print("Element in AVL")
        return True
    elif value < rootNode.data:
        if rootNode.leftChild.data == value:
            print("Element in AVL")
            return True
        else:
            searchAVL(rootNode.leftChild, value)
    else:
        if rootNode.rightChild.data == value:
            print("Element in AVL")
            return True
        else:
            searchAVL(rootNode.rightChild, value)

# rotate AVL right
def rotateRight(unbalancedNode: object):
    newRootNode = unbalancedNode.leftChild
    unbalancedNode.leftChild = unbalancedNode.leftChild.rightChild
    newRootNode.rightChild = unbalancedNode
    unbalancedNode.height = 1 + max(getHeight(unbalancedNode.leftChild), getHeight(unbalancedNode.rightChild))
    newRootNode.height = 1 + max(getHeight(newRootNode.leftChild), getHeight(newRootNode.rightChild))
    return newRootNode

# rotate AVL left
def rotateLeft(unbalancedNode: object):
    newRootNode = unbalancedNode.rightChild
    unbalancedNode.rightChild = unbalancedNode.rightChild.leftChild
    newRootNode.leftChild = unbalancedNode
    unbalancedNode.height = 1 + max(getHeight(unbalancedNode.leftChild), getHeight(unbalancedNode.rightChild))
    newRootNode.height = 1 + max(getHeight(newRootNode.leftChild), getHeight(newRootNode.rightChild))
    return newRootNode

# get height
def getHeight(rootNode: object):
    if rootNode is None:
        return 0
    return rootNode.height

# Check balance of tree
def getBalance(rootNode: object):
    if rootNode is None:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

# insert node to AVL
def insertNode(rootNode: object, value: any):
    if rootNode is None:
        return AVLNode(value)
    if value <= rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, value)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, value)
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and value <= rootNode.leftChild.data:
        return rotateRight(rootNode)
    if balance > 1 and value > rootNode.leftChild.data:
        rootNode.leftChild = rotateLeft(rootNode.leftChild)
        return rotateRight(rootNode)
    if balance < -1 and value <= rootNode.rightChild.data:
        rootNode.rightChild = rotateRight(rootNode.rightChild)
        return rotateLeft(rootNode)
    if balance < -1 and value > rootNode.rightChild.data:
        return rotateLeft(rootNode)
    return rootNode

# Minimum value node
def minNode(rootNode: object):
    currNode = rootNode
    while (currNode.leftChild is not None):
        currNode = currNode.leftChild
    return currNode

# delete node from AVL
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
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:
        return rotateRight(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild = rotateLeft(rootNode.leftChild)
        return rotateRight(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return rotateLeft(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) > 0:
        rootNode.rightChild = rotateRight(rootNode.rightChild)
        return rotateLeft(rootNode)
    return rootNode

# delete AVL
def deleteAVL(rootNode: object):
    if rootNode is None:
        return True
    else:
        rootNode.data = None
        rootNode.leftChild = None
        rootNode.rightChild = None
        return True
    

AVL = AVLNode(5)
AVL = insertNode(AVL, 10)
AVL = insertNode(AVL, 15)
AVL = insertNode(AVL, 20)
AVL = insertNode(AVL, 2)
AVL = insertNode(AVL, 25)
AVL = insertNode(AVL, 30)
AVL = deleteNode(AVL, 15)
levelOrderTraversal(AVL)
print(deleteAVL(AVL))