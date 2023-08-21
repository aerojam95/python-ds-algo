# This function takes an array and returns if the array has duplicates or not

# Arguments of functions:
# arr: array to operate upon

# Written by JAM
# 21-08-2023

# Import libraries
import logging
import array

# Logging settings
logging.basicConfig(filename='containCopy.log',
                    format='%(asctime)s-%(levelname)s-%(message)s',
                    encoding='utf-8',
                    level=logging.INFO)

def containCopy(arr: array.array):

    # Logging
    logging.info(f"Fiding duplicate elements...")

    # Initialise vairbales
    temp = 0
    elements = arr[:]
    
    for i in range(len(arr)):
        temp = arr[i]
        elements.remove(arr[i])
        if temp in elements:
            return True
    
    return False

print(containCopy([1, 2, 3, 4, 5, 6, 7, 8, 9, 1]))