# This script finds all the integer pairs of an array that sum to a separate 
# integer argument

# Arguments of functions:
# nums  : list of integers from which to find pairs
# target: integer to which the pairs sum

# Written by JAM
# 21-08-2023

# Import libraries
import logging

# Logging settings
logging.basicConfig(filename='sumPairs.log',
                    format='%(asctime)s-%(levelname)s-%(message)s',
                    encoding='utf-8',
                    level=logging.INFO)

def sumPairs(nums: list, target: int):
    # Temp variables
    temp = 0
    pairs = []
    pairLocations = []
    # Find pair
    for i in range(len(nums)):
        for j in range(len(nums)):
            temp = nums[i] + nums[j]
            if (temp == target) & (j != i) & ([j,i] not in pairLocations):
                pairs.append(f"{nums[i]}+{nums[j]}")
                pairLocations.append([i,j])
    logging.info(f"the sumPairs are {pairs}")
    return pairs



# script definition
def main(nums: list, target: int):
    # Starting script
    logging.info(f"sumPairs starting...")
    # Find sumPairs
    logging.info(f"Running sumPairs search...")
    sumPair = sumPairs(nums, target)
    print(sumPair)

# script exectuion
if __name__ == "__main__":

    # Set arguments
    # Set arguments
    nums   = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
    target = 7
    main(nums, target)