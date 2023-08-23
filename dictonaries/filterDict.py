# Function takes a dictionary a filter the same dictionary based on an input
# condition

# inputs:
# inDict   : dictonary
# condition: lambda function

# Outputs:
# outDict: dictionary

import logging

logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s',
                    encoding='utf-8',
                    level=logging.INFO)

def filterDict(inDict: dict, condition):
    
    logging.info(f"Initialising output dictionary...")
    outDict = {}

    logging.info(f"Filtering dictionary...")
    outDict = {key:value for key, value in inDict.items() if
               condition(key, value)}

    logging.info(f"Filtered dictionary {outDict}")
    return outDict