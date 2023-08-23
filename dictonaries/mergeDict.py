# Function merge two dictonaries, by its values and common keys

# inputs:
# dict1: dictionary
# dict2: dictionary

# Outputs:
# combinedDict: dictonary 

import logging

logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s',
                    encoding='utf-8',
                    level=logging.INFO)

def mergeDict(dict1:dict, dict2:dict):

    logging.info(f"Initialising output dictonary...")
    combinedDict = {}
    logging.info(f"Taking dict1 into output dictionary...")
    combinedDict = dict1.copy()

    logging.info(f"Combining dictionaries...")
    for key in dict2:
        if key in combinedDict.keys():
            combinedDict[key] += dict2[key]
        else:
            combinedDict[key] = dict2[key]

    logging.info(f"Combined dictonaries: {combinedDict}")
    return combinedDict