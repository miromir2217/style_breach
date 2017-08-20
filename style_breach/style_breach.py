# imports

import sys
from functools import reduce

import read_data
import feature_extractor


# functions


# main script

sentences = read_data.read_sentences_from_file(sys.argv[1])
for sentence in sentences:
    print('--------------------------')
    print('Sentence: ' + ''.join(reduce((lambda x, y: x + ' ' + y), sentence)) + '\n')
    stopwords = feature_extractor.get_stop_words_in_sentence(sentence)
    print('stopwords: ' +
          ''.join(reduce((lambda x, y: x + ', ' + y), stopwords))
          if stopwords != []
          else '')
    pos_tagged_words = feature_extractor.get_pos_tagged_words(sentence)
    print('pos-tagged: ' +
          ''.join(
              reduce(
                  (lambda x, y: x + ', ' + y),
                  list(map((lambda x: '(' + x[0] + ', ' + x[1] + ')'), pos_tagged_words))))
          if pos_tagged_words != [] else '')
    for word in sentence:
        print(word + ' freq score: ' + str(feature_extractor.get_word_freq(word, sentence, sentences)))
    punct_freq = feature_extractor.get_punctuation_freq(sentence)
    print(punct_freq)
    print('--------------------------')
