# This function finds the max product of between of two elements possible from
# an array argument

# Arguments of functions:
# arr: array that contains one missing integer from 1 to 100
# n: largest integer contained within the array

# Written by JAM
# 19-08-2023

# Import libraries
import logging
import array

# Logging settings
logging.basicConfig(filename='calculateMaxProduct.log',
                    format='%(asctime)s-%(levelname)s-%(message)s',
                    encoding='utf-8',
                    level=logging.INFO)

def calculateMaxProduct(arr: array.array):

    # Find largest elements
    logging.info(f"Finding largest elements from {arr}")
    arr.sort(reverse=True)
    logging.info(f"Max product is {arr[0] * arr[1]}")
    return arr[0] * arr[1]
        
print(calculateMaxProduct([1,7,3,4,9,5]))