# A set of functions for different sorting algorithms

# data   : 27-09-2023
# Written by: JAM 

import math

# Ot(n**2), Om(1), easy to implement
def bubbleSort(list: list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

# Ot(n**2), Om(1), easy to implement 
def selectionSort(list: list):
    for i in range(len(list)):
        index = i
        for j in range(i, len(list)):
            if list[j] < list[index]:
                index = j
        list[i], list[index] = list[index], list[i]
    return list

# Ot(n**2), Om(1), easy to implement 
def insertionSort(list: list):
    for i in range(1, len(list)):
        check = list[i]
        j = i - 1
        while j >= 0 and check < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = check
    return list

# Ot(n**2) but can be improved by changing individual bucket sorting , Om(n),
# easy to implement 
def bucketSort(list: list):
    noBuckets = round(math.sqrt(len(list)))
    maxElement = max(list)
    arr = []
    for i in range(noBuckets):
        arr. append([])
    for i in list:
        index = math.ceil((i * noBuckets) / maxElement)
        arr[index - 1].append(i)
    for i in arr:
        i = insertionSort(i)
    k = 0
    for i in range(noBuckets):
        for j in range(len(arr[i])):
            list[k] = arr[i][j]
            k += 1
    return list

# Ot(n), Om(n), helper merge function for merge sort
def merge(list: list, left: int, middle: int, right: int):
    n1 = middle - left + 1
    n2 = right - middle
    Left = [0] * (n1)
    Right = [0] * (n2)
    for i in range(0, n1):
        Left[i] = list[left + i]
    for i in range(0, n2):
        Right[i] = list[middle + 1 + i]
    index1 = 0 # index of subarray 1
    index2 = 0 # index of subarray 2
    index3 = left
    while index1 < n1 and index2 < n2:
        if Left[index1] <= Right[index2]:
            list[index3] = Left[index1]
            index1 += 1
        else:
            list[index3] = Right[index2]
            index2 += 1
        index3 += 1
    while index1 < n1:
        list[index3] = Left[index1]
        index1 += 1
        index3 += 1
    while index2 < n2:
        list[index3] < Right[index2]
        index2 += 1
        index3 += 1
    
# Ot(nlog(n)) n element for log(n) levels , Om(n), difficult to implement
def mergeSort(list: list, left: int, right: int):
    if left < right:
        middle = (left + right - 1) // 2
        mergeSort(list, left, middle)
        mergeSort(list, middle + 1, right)
        merge(list, left, middle, right)
    return list

# helper function for pivot
def swap(list: list, index1: int, index2: int):
    list[index1], list[index2] = list[index2], list[index1]

# pivot function to help quick sort implementation
def pivot(list: list, pivotIndex: int, endIndex: int):
    swapIndex = pivotIndex
    for i in range(pivotIndex + 1, endIndex + 1):
        if list[i] < list[pivotIndex]:
            swapIndex += 1
            swap(list, swapIndex, i)
    swap(list, pivotIndex, swapIndex)
    return swapIndex
    
# Ot(nlog(n)), Om(1), easier than merge sort implementation
def quickSort(list: list, left: int, right: int):
    if left < right:
        pivotIndex = pivot(list, left, right)
        quickSort(list, left, pivotIndex - 1)
        quickSort(list, pivotIndex + 1, right)
    return list

# heapify helper function for heap sort
def heapify(customList, n, i):
    smallest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and customList[l] < customList[smallest]:
        smallest = l
    
    if r < n and customList[r] < customList[smallest]:
        smallest = r
    
    if smallest != i:
        customList[i], customList[smallest] = customList[smallest], customList[i]
        heapify(customList, n, smallest)

# Ot(nlog(n)), Om(1), dififcult implementations
def heapSort(customList):
    n = len(customList)
    for i in range(int(n/2)-1, -1, -1):
        heapify(customList, n, i)
    
    for i in range(n-1,0,-1):
        customList[i], customList[0] = customList[0], customList[i]
        heapify(customList, i, 0)
    return customList.reverse()

a = [2, 1, 3, 7, 2, 9, 8, 4]
print(a)
heapSort(a)
print(a)