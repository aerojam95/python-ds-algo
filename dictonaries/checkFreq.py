# Function which takes two lists as inputs and checks if the two given lists
# have the same frequency of elements

# inputs:
# list1: list
# list2: list

# Outputs:
# boolean 

import logging

logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s',
                    encoding='utf-8',
                    level=logging.INFO)

def checkFreq(list1: list, list2: list):

    def buildDict(input: list):

        logging.info(f"Initialising dictionary...")
        dict1 = {}

        logging.info(f"Generating dictonary...")
        for key in input:
            if key in dict1.keys():
                dict1[key] += 1
            else:
                dict1[key] = 1

        logging.info(f"Generated frequency dictonary from list {dict1}")
        return dict1

    logging.info(f"Checking dictonaries...")
    if buildDict(list1) == buildDict(list2):
        logging.info(f"Lists have the same frequencies")
        return True
    else:
        logging.info(f"Lists do not have the same frequencies")
        return False

checkFreq([1, 2, 3, 2, 1],[3, 1, 2, 1, 3])