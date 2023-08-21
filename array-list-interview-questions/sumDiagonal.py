# This function takes a 2D array and returns a the sum of its diagonal elements

# Arguments of functions:
# arr: 2D array to operate upon

# Written by JAM
# 21-08-2023

# Import libraries
import logging
import array

# Logging settings
logging.basicConfig(filename='sumDiagonal.log',
                    format='%(asctime)s-%(levelname)s-%(message)s',
                    encoding='utf-8',
                    level=logging.INFO)

def sumDiagonal(arr: array.array):

    # Find missing number
    logging.info(f"Finding diagonal sum...")

    # initialise variables
    sum = 0

    # Calculate diagonal sum
    logging.info(f"Calculating diagonal sum...")
    for i in range(len(arr)):
        sum += arr[i][i]

    #
    logging.info(f"Diagonal sum {sum}")
    return sum
