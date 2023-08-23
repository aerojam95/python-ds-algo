# Function reverses the keys for values of an input dictonary

# inputs:
# inDict: dictonary

# Outputs:
# outDict: dictionary

import logging

logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s',
                    encoding='utf-8',
                    level=logging.INFO)

def reverseDict(inDict: dict):

    logging.info(f"Initialising output dictionary...")
    outDict = {}

    outDict = {value:key for key, value in inDict.items()}
    logging.info(f"reversed dictionary {outDict}")
    return outDict