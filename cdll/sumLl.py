# This function the sum of two linked lists, defined by ll.py,
# each list is a representation of a number and the function returns a third
# list as the output of the sums

# Date   : 08-09-2023
# Written: JAM

from ll import LinkedList

def sumLl(lla: object, llb: object):

    if lla.head is None and llb is None:
        return None
    
    if lla.head is None:
        return llb
    
    if llb.head is None:
        return lla
    
    llc = LinkedList()
    tempNodeA = lla.head
    tempNodeB = llb.head
    carry = 0

    while tempNodeA and tempNodeB:
        if tempNodeA.value + tempNodeB.value + carry >= 10:
            llc.add((tempNodeA.value + tempNodeB.value + carry) % 10)
            carry = 1
        else:
            llc.add(tempNodeA.value + tempNodeB.value + carry)
            carry = 0
        tempNodeA = tempNodeA.next
        tempNodeB = tempNodeB.next

    if tempNodeA is None:
        while tempNodeB:
            if tempNodeB.value + carry >= 10:
                    llc.add((tempNodeB.value + carry) % 10)
                    carry = 1
            else:
                llc.add(tempNodeB.value + carry)
                carry = 0
            tempNodeB = tempNodeB.next

    if tempNodeB is None:
        while tempNodeA:
            if tempNodeA.value + carry >= 10:
                    llc.add((tempNodeA.value + carry) % 10)
                    carry = 1
            else:
                llc.add(tempNodeA.value + carry)
                carry = 0
            tempNodeA = tempNodeA.next

    if carry != 0:
        llc.add(1)

    return llc

lla = LinkedList()
lla.add(7)
lla.add(1)
lla.add(6)
lla.add(2)

llb = LinkedList()
llb.add(5)
llb.add(9)
llb.add(3)

print(sumLl(lla, llb))