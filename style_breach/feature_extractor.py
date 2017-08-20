import nltk
import feature_helper
import math

from stop_words import get_stop_words


def get_pos_tagged_words(sentence):
    return nltk.pos_tag(sentence) if sentence != [] else []


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


def get_word_freq(word, sentence, sentences):
    most_popular_word = feature_helper.get_word_freq_in_sentences(feature_helper.get_most_popular_word(sentences), sentences)
    word_freq_all = feature_helper.get_word_freq_in_sentences(word, sentences)
    word_freq = feature_helper.get_word_freq_in_sentences(word, [sentence])

    return math.log2(float(most_popular_word / (word_freq_all - word_freq + 1)))


def get_punctuation_freq(sentence):
    punct_freq = {}
    for symbol in feature_helper.get_punct_symbols():
        punct_freq[symbol] = 0

    for word in sentence:
        for char in word:
            if char in punct_freq:
                punct_freq[char] += 1

    return punct_freq
