# A class to define a binary tree DS with LL

# Date   : 25-09-2023
# Written by: JAM

from queuesll import QueueSLL

class TreeNode(object):
    # Define tree node object
    def __init__(self: object, data: any = None):
        self.data = data
        self.leftChild = None
        self.rightChild = None

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

# Search by level order traversal
def searchBT(rootNode: object, nodeValue: any):
    if rootNode is None:
        return False
    else:
        queue = QueueSLL()
        queue.enqueue(rootNode)
        while not(queue.isEmpty()):
            root = queue.dequeue()
            if root.data == nodeValue:
                return True
            if (root.leftChild is not None):
                queue.enqueue(root.leftChild)
            if (root.rightChild is not None):
                queue.enqueue(root.rightChild)
        return False
    
# Insert fist empty spot by level order traversal    
def insertBT(rootNode: object, node: object):
    if rootNode is None:
        rootNode = node
        return True
    else:
        queue = QueueSLL()
        queue.enqueue(rootNode)
        while not(queue.isEmpty()):
            root = queue.dequeue()
            if root.leftChild is None:
                root.leftChild = node
                return True
            else:
                queue.enqueue(root.leftChild)
            if root.rightChild is None:
                root.rightChild = node
                return True
            else:
                queue.enqueue(root.rightChild)

# Get deepest node of BT
def getDeepestNode(rootNode: object):
    if rootNode is None:
        return rootNode
    else:
        queue = QueueSLL()
        queue.enqueue(rootNode)
        while not(queue.isEmpty()):
            root = queue.dequeue()
            if root.leftChild is not None:
                queue.enqueue(root.leftChild)
            if root.rightChild is not None:
                queue.enqueue(root.rightChild)
        deepestNode = root
        return deepestNode
    
def deleteDepestNode(rootNode: object, deleteNode: object):
    if rootNode is None:
        return False
    else:
        queue = QueueSLL()
        queue.enqueue(rootNode)
        while not(queue.isEmpty()):
            root = queue.dequeue()
            if root is deleteNode:
                root = None
                return True
            if root.leftChild is deleteNode:
                root.leftChild = None
                return True
            else:
                queue.enqueue(root.leftChild)
            if root.rightChild is deleteNode:
                root.rightChild = None
                return True
            else:
                queue.enqueue(root.rightChild)

# delete a specific node from BT and replace it with deepest node
def deleteNodeBT(rootNode: object, node: object):
    if rootNode is None:
        return False
    else:
        queue = QueueSLL()
        queue.enqueue(rootNode)
        while not(queue.isEmpty()):
            root = queue.dequeue()
            if root.data == node:
                delNode = getDeepestNode(rootNode)
                root.data = delNode.data
                deleteDepestNode(rootNode, delNode)
                return True
            if (root.leftChild is not None):
                queue.enqueue(root.leftChild)
            if (root.rightChild is not None):
                queue.enqueue(root.rightChild)
        return False
    
# delete BT
def deleteBT(rootNode: object):
    if rootNode is None:
        return True
    else:
        rootNode.data = None
        rootNode.leftChild = None
        rootNode.rightChild = None
        return True