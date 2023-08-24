# Function which takes a tuple of tuples and returns a tuple containing the
# diagonal elements of the input

# inputs:
# inTuple: tuple of tuples

# Outputs:
# outTuple: tuple

import logging

logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s',
                    encoding='utf-8',
                    level=logging.INFO)

def diagonal(inTuple: tuple):

    logging.info(f"Searching for diagonal elements...")
    outTuple = tuple([i for i,_,_ in inTuple])

    logging.info(f"Diagonal elments {outTuple}")
    return outTuple