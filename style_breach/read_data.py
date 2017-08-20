# imports

import os


# functions

def read_files_from_folder(folder_name):
    """ A function to return the names of every file in the given directory """
    files = []
    for file in os.listdir(folder_name):
        if os.path.isdir(file):
            files.append(file)

    return files


def read_sentences_from_file(filename):
    """ This function accepts a path to a file and returns a list of all the sentences found in the file
    """
    sentences = []
    old_sentence = ""
    new_sentence = ""
    file = open(filename, 'r')
    for char in file.read():
        if char == '\n':
            continue

        new_sentence += char

        if (char == '"' or char == '\'') and len(new_sentence) == 1:
            old_sentence += char
            new_sentence = ""

        if char == '.':
            # abbreviations like U.S.A. should not be counted as a new sentence
            if len(new_sentence) < 3 or new_sentence[0].islower() or (new_sentence[0] == ' ' and new_sentence[1].islower()):
                old_sentence += new_sentence
            else:
                if len(old_sentence) > 0:
                    sentences.append(list(filter((lambda x: len(str(x)) > 0), old_sentence.split(' '))))

                old_sentence = new_sentence

            new_sentence = ""

    if len(old_sentence) > 0:
        sentences.append(list(filter((lambda x: len(str(x)) > 0), old_sentence.split(' '))))

    print('INFO: Sentence count: ' + str(len(sentences)) + '\n')
    return sentences
