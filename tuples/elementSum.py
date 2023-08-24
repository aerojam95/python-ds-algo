# Function which  takes two tuples and returns a tuple containing the 
# element-wise sum of the input tuples

# inputs:
# inTuple1: tuple
# inTUple2: tuple

# Outputs:
# outTuple: tuple

import logging

logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s',
                    encoding='utf-8',
                    level=logging.INFO)

def elementSum(inTuple1: tuple, inTuple2: tuple):

    logging.info(f"Checking tuples are the same size...")
    if len(inTuple1) != len(inTuple2):
        raise ValueError(f"{inTuple1} and {inTuple2} are not the same size")

    logging.info(f"Calculating output tuple...")
    outTuple= tuple([i + j for i, j in zip(inTuple1, inTuple2)])
    logging.info(f"Output tuple {outTuple}")
    return outTuple

print(elementSum((1,2,3),(4,5,6)))