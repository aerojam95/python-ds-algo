# This function finds the intersection of two linked lists, defined by ll.py,
# intersection being defined by reference not value, return of intersection 
# node

# Date   : 08-09-2023
# Written: JAM

from ll import LinkedList, Node

def findIntersect(lla: object, llb: object):

    if lla.tail is not llb.tail:
        return None

    short = lla if len(lla) < len(llb) else llb
    long  = llb if len(lla) < len(llb) else lla
    diff = len(long) - len(short)

    tempNodeA = long.head
    tempNodeB =  short.head

    for _ in range(diff):
        tempNodeA = tempNodeA.next
    
    while tempNodeA is not tempNodeB:
        tempNodeA =  tempNodeA.next
        tempNodeB = tempNodeB.next

    return tempNodeA

def appendNodeToTwoLL(lla: object, llb: object, value: any):
    node = Node(value)
    lla.tail.next= llb.tail.next = node
    lla.tail = llb.tail  = node

lla = LinkedList()
lla.generate(4, 1, 9)

llb = LinkedList()
llb.generate(3, 1, 9)

appendNodeToTwoLL(lla, llb, 7)
appendNodeToTwoLL(lla, llb, 2)
appendNodeToTwoLL(lla, llb, 1)

print(lla)
print(llb)

print(findIntersect(lla, llb))