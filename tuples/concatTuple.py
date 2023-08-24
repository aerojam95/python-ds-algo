# Function which calculates the sum and product of all elements in a tuple of 
# numberstakes a tuple of strings and concatenates them, separating each string
#  with a space

# inputs:
# inTuple: tuple

# Outputs:
# outStr: str

import logging

logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s',
                    encoding='utf-8',
                    level=logging.INFO)

def concatTuple(inTuple: tuple):

    logging.info(f"Initialising string...")
    outStr = ""

    logging.info(f"Evaluating string...")
    outStr = ' '.join(inTuple)

    logging.info(f"Output string {outStr}")
    return outStr