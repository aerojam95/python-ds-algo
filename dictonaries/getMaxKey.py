# Function finds the key with the largest value

# inputs:
# maxDict: dictonary

# Outputs:
# maxKey: string

import logging

logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s',
                    encoding='utf-8',
                    level=logging.INFO)

def getMaxKey(maxDict: dict):
    logging.info(f"Key with largerst value {max(maxDict, key=maxDict.get)}")
    return max(maxDict, key=maxDict.get)