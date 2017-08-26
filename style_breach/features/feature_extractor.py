import math

import nltk
from stop_words import get_stop_words

from features import feature_helper


###############
# POS TAGGING #
###############
def get_pos_tagged_words(sentence):
    return nltk.pos_tag(sentence) if sentence != [] else []


##############
# STOP WORDS #
##############
def get_stop_words_in_sentence(sentence):
    stopwords = get_stop_words('en')
    stopwords_in_sentence = []

    for word in sentence:
        if word in stopwords:
            stopwords_in_sentence.append(word)

    return stopwords_in_sentence


def get_non_stopwords_in_sentence(sentence):
    stopwords = get_stop_words_in_sentence(sentence);
    words = []
    for word in sentence:
        if word not in stopwords:
            words.append(word)

    return words


####################
# WORD FREQUENCIES #
####################
def get_word_freq(word, sentence, sentences):
    most_popular_word = feature_helper.get_word_freq_in_sentences(feature_helper.get_most_popular_word(sentences), sentences)
    word_freq_all = feature_helper.get_word_freq_in_sentences(word, sentences)
    word_freq = feature_helper.get_word_freq_in_sentences(word, [sentence])

    return math.log2(float(most_popular_word / (word_freq_all - word_freq + 1)))


def get_punctuation_freq(sentence, sentences):
    symbol_freq = {}
    for symbol in feature_helper.get_punct_symbols():
        freq_in_sentence = feature_helper.get_symbol_freq_in_senteces(symbol, [sentence])
        freq_in_doc = feature_helper.get_symbol_freq_in_senteces(symbol, sentences)
        symbol_freq[symbol] = freq_in_sentence / (1 if freq_in_doc == 0 else freq_in_doc)

    return symbol_freq
