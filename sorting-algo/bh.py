# A class to define an Binary heap with python lists

# data   : 26-09-2023
# Written by: JAM

class Heap(object):
    def __init__(self: object, size: int):
      self.list = (size + 1) * [None]
      self.heapSize = 0
      self.maxSize = size + 1

def peekofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.list[1]

def sizeofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize+1):
            print(rootNode.list[i])

def heapifyTreeInsert(rootNode: object, index: int, heapType: str):
    parentIndex = int(index / 2)
    if index <= 1:
        return
    if heapType == "min":
        if rootNode.list[index] < rootNode.list[parentIndex]:
            rootNode.list[index], rootNode.list[parentIndex] = rootNode.list[parentIndex], rootNode.list[index]
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType == "max":
        if rootNode.list[index] > rootNode.list[parentIndex]:
            rootNode.list[index], rootNode.list[parentIndex] = rootNode.list[parentIndex], rootNode.list[index]
        heapifyTreeInsert(rootNode, parentIndex, heapType)

def insertNode(rootNode: object, value: any, heapType: str):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return False
    rootNode.list[rootNode.heapSize + 1] = value
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return True

def heapifyTreeExtract(rootNode: object, index: int, heapType: str):
    left = index * 2
    right = index * 2 + 1
    swap = 0
    if rootNode.heapSize < left:
        return
    elif rootNode.heapSize == left:
        if heapType == "min":
            if rootNode.list[index] > rootNode.list[left]:
                rootNode.list[index], rootNode.list[left] = rootNode.list[left], rootNode.list[index]
            return
        elif heapType == "max":
            if rootNode.list[index] < rootNode.list[left]:
                rootNode.list[index], rootNode.list[left] = rootNode.list[left], rootNode.list[index]
            return
    else:
        if heapType == "min":
            if rootNode.list[left] < rootNode.list[right]:
                swap = left
            else:
                swap = right
            if rootNode.list[index] > rootNode.list[swap]:
                rootNode.list[index], rootNode.list[swap] = rootNode.list[swap], rootNode.list[index]
        elif heapType == "max":
            if rootNode.list[left] > rootNode.list[right]:
                swap = left
            else:
                swap = right
            if rootNode.list[index] < rootNode.list[swap]:
                rootNode.list[index], rootNode.list[swap] = rootNode.list[swap], rootNode.list[index]
    heapifyTreeExtract(rootNode, swap, heapType)

def extractNode(rootNode: object, heapType: str):
    if rootNode.heapSize == 0:
        return
    else:
        extractedNode = rootNode.list[1]
        rootNode.list[1] = rootNode.list[rootNode.heapSize]
        rootNode.list[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractedNode
    
def deleteBH(rootNode: object):
    rootNode.list = None
    return True

BH = Heap(5)
insertNode(BH, 4, "max")
insertNode(BH, 5, "max")
insertNode(BH, 2, "max")
insertNode(BH, 1, "max")
print(extractNode(BH, "max"))
levelOrderTraversal(BH)
print(deleteBH(BH))
