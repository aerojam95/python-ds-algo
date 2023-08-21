# This function takes an array and returns a new array that contains all but
# the first and last elements

# Arguments of functions:
# arr: array list to operate upon

# Written by JAM
# 21-08-2023

# Import libraries
import logging
import array

# Logging settings
logging.basicConfig(filename='findMiddle.log',
                    format='%(asctime)s-%(levelname)s-%(message)s',
                    encoding='utf-8',
                    level=logging.INFO)

def findMiddle(arr: array.array):

    # Find missing number
    logging.info(f"Reducing list without first and last element...")
    logging.info(f"Returned list {arr[1:-1]}")
    return arr[1:-1]