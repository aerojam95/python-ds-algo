# This function takes an array and returns two largest elements

# Arguments of functions:
# arr: array to operate upon

# Written by JAM
# 21-08-2023

# Import libraries
import logging
import array

# Logging settings
logging.basicConfig(filename='findTopTwo.log',
                    format='%(asctime)s-%(levelname)s-%(message)s',
                    encoding='utf-8',
                    level=logging.INFO)

def findTopTwo(arr: array.array):

    # Find missing number
    logging.info(f"Finding two largest elements...")
    arr.sort(reverse=True)
    logging.info(f"The largest elements are {arr[0:2]}")
    return arr[0:2]