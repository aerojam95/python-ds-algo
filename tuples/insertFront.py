# Function which  takes two a tuple and a value, and returns a new tuple with
# the value inserted at the beginning of the original tuple

# inputs:
# inTuple: tuple
# val    : int

# Outputs:
# outTuple: tuple

import logging

logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s',
                    encoding='utf-8',
                    level=logging.INFO)

def insertFront(inTuple: tuple, val: int):

    logging.info(f"Adding element...")
    outTuple = (val,) + inTuple

    logging.info(f"Output tuple {outTuple}")
    return outTuple

print(insertFront((2,3,4),1))