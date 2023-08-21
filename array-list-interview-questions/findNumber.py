# This function finds the element in an array which is equal to an integer
# argument

# Arguments of functions:
# arr: array that contains integers
# n  :  integer contained within the array

# Written by JAM
# 19-08-2023

# Import libraries
import logging
import array

# Logging settings
logging.basicConfig(filename='findNumber.log',
                    format='%(asctime)s-%(levelname)s-%(message)s',
                    encoding='utf-8',
                    level=logging.INFO)

def checkNumber(arr: array.array, n: int):

    # Find missing number
    logging.info(f"Finding where {n} is located in an argument array {arr}")
    for i, x in enumerate(arr):
        if x == n:
            logging.info(f"{n} is located at element {i} of {arr}")
            return i
