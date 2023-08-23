# Function counts the frequency of words in an input list

# inputs:
# words: list

# Outputs:
# freq: dictonary 

import logging

logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s',
                    encoding='utf-8',
                    level=logging.INFO)

def countWordFreq(words: list):

    logging.info(f"Initialising dictionary...")
    freq = {}

    logging.info(f"Counting word frequencies...")
    for word in words:
        if word in freq.keys():
            freq[word] +=1
        else:
            freq[word] = 1

    logging.info(f"Word frequencies {freq}")
    return freq