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
    """ This function accepts a path to a file and returns a list of all the sentences found in the file, each
        paired with the number of the first character in the sentence in the file
    """
    sentence_start = 0
    char_count = -1
    sentences = []
    old_sentence = ""
    new_sentence = ""
    opened_quote_or_bracket = False
    file = open(filename, 'r')
    for char in file.read():
        char_count += 1
        if char == '\n':
            continue

        new_sentence += char
        if char == '"' or char == '(' or char == ')':
            opened_quote_or_bracket ^= 1

        if (char == '.' and not opened_quote_or_bracket) \
                or (char == '"' and not opened_quote_or_bracket and new_sentence[-2] == '.'):
            # abbreviations like U.S.A. should not be counted as a new sentence
            if len(new_sentence) < 3 \
                    or (new_sentence[0].isalpha() and not new_sentence[0].isupper()) \
                    or (new_sentence[0] == ' ' and new_sentence[1].isalpha() and not new_sentence[1].isupper()):
                old_sentence += new_sentence
            else:
                if len(old_sentence) > 0:
                    sentences.append([sentence_start, list(filter((lambda x: len(str(x)) > 0), old_sentence.split(' ')))])
                    sentence_start = char_count + 1

                old_sentence = new_sentence

            new_sentence = ""

    if len(old_sentence) > 0:
        sentences.append([sentence_start, list(filter((lambda x: len(str(x)) > 0), old_sentence.split(' ')))])

    print('INFO: Sentence count: ' + str(len(sentences)) + '\n')
    return sentences
