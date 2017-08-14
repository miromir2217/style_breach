# imports

import os


# functions

def read_files_from_folder(folder_name):
    """ A function to return the names of every file in the given directory """
    files = []
    for file in os.listdir(folder_name):
        if os.path.isdir(file):
            files.append(file)

    return files;


def read_sentences_from_file(filename):
    """ This function accepts a path to a file and returns a list of all the sentences found in the file
    """
    sentences = []
    _sentence = ""
    file = open(filename, 'r')
    for char in file.read():
        _sentence += char
        if char == '.':
            sentences.append(_sentence)
            _sentence = ""

    return sentences;