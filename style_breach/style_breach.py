# imports

import sys
import read_data


# functions


# main script

for sentence in read_data.read_sentences_from_file(sys.argv[1]):
    print(sentence)