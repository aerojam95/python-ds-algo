# This function finds the missing integer of an array that can contain integers
# 1 to 100

# Arguments of functions:
# arr: array that contains one missing integer from 1 to 100
# n: largest integer contained within the array

# Written by JAM
# 19-08-2023

# Import libraries
import logging
import array

# Logging settings
logging.basicConfig(filename='missingNumber.log',
                    format='%(asctime)s-%(levelname)s-%(message)s',
                    encoding='utf-8',
                    level=logging.INFO)

def missingNumber(arr, n):
     
    # Check arguments are the correct type
    # n check
    try:
        number = int(n)
        logging.info(f" {n} is an integer...")
    except ValueError:
        logging.info(f" {n} is not an integer...")
    # arr check
    if isinstance(arr, list):
        logging.info(f" {arr} is an array...")
    else:
        logging.info(f" {arr} is not an array...")

    # check limits
    # check n
    if n > 100:
        logging.error(f" {n} is larger than 100")
    else:
        logging.info(f" Parsing {n} for missing number...")
    # check arr
    if max(arr) > 100:
        logging.error(f" {arr} contains numbers larger than 100")
    else:
        logging.info(f" Parsing {arr} for missing number...")

    arr1 = array.array('i',[])
    arr1 = [i for i in range(1, n + 1)]

    # Find missing number
    missing = [i for i in arr1 if i not in arr]
    logging.info(f" The missing number is {missing[0]}")
    return missing[0]