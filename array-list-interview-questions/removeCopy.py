# This function takes an array and returns two largest elements

# Arguments of functions:
# arr: array to operate upon

# Written by JAM
# 21-08-2023

# Import libraries
import logging
import array

# Logging settings
logging.basicConfig(filename='removeCopy.log',
                    format='%(asctime)s-%(levelname)s-%(message)s',
                    encoding='utf-8',
                    level=logging.INFO)

def removeCopy(arr: array.array):

    # Logging
    logging.info(f"Removing duplicate elements...")

    # Initialise vairbales
    temp = 0
    elements = []
    
    for i in range(len(arr)):
        temp = arr[i]
        if temp not in elements:
            elements.append(temp)
    return elements