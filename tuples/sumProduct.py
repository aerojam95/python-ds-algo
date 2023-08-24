# Function which calculates the sum and product of all elements in a tuple of 
# numbers

# inputs:
# inTuple: tuple

# Outputs:
# prod: int
# sum : int

import logging

logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s',
                    encoding='utf-8',
                    level=logging.INFO)

def sumProduct(inTuple: tuple):

    logging.info(f"Intialising sum and product...")
    sumTuple = 0
    prodTuple = 1

    sumTuple = sum(inTuple) 
    logging.info(f"Sum of {inTuple} calculated {sumTuple}")

    for i in inTuple:
        prodTuple *= i
    logging.info(f"Prod of {inTuple} calculated {prodTuple}")

    return sumTuple, prodTuple