# Function which takes two tuples and returns a tuple containing the common
# elements of the input tuples

# inputs:
# inTuple1: tuple
# inTUple2: tuple

# Outputs:
# outTuple: tuple

import logging

logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s',
                    encoding='utf-8',
                    level=logging.INFO)

def sameElem(inTuple1: tuple, inTuple2: tuple):

    logging.info(f"Finding common elements...")
    outTuple = tuple([i for i in inTuple1 if i in inTuple2])

    logging.info(f"Common elements {outTuple}")
    return outTuple