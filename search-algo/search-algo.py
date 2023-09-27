# A set of functions for different searching algorithms

# data   : 27-09-2023
# Written by: JAM

# Ot(n), Om(1), easy to implement
def linearSearch(array: list, value: any):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1

# Only for sorted arrays
# Ot(log(n)), Om(1), easy to implement
def binarySearch(array: list, value: any):
    left = 0
    right = len(array) - 1
    middle = (right + left) // 2
    while not(array[middle] == value) and left <= right:
        print(array[middle])
        if value < array[middle]:
            right = middle - 1
        if value > array[middle]:
            left = middle + 1
        middle = (left + right) // 2
    if array[middle] == value:
        return middle
    else:
        return -1

print(binarySearch([10, 20, 60, 70, 75, 83, 92], 75))