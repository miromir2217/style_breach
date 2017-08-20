# def get_words(sentence):
#     return list(filter((lambda x: len(str(x)) > 0), str(sentence).split(sep=' ')))
#
#
# def get_word_count(sentence):
#     return get_words(sentence).count()


def get_word_freq_in_sentences(word, sentences):
    """
        :param word: the word which frequency we calculate
        :param sentences: a list of the sentences, representing the document / search space
        :return: the number of occurrences of the given word in the search space. Letter case is ignored
    """
    freq = 0
    for sentence in sentences:
        for w in sentence:
            if str(word).lower() == str(w).lower():
                freq += 1

    return freq


def get_most_popular_word(sentences):
    word_map = {}
    for sentence in sentences:
        for word in sentence:
            if word not in word_map:
                word_map[word] = 1

            word_map[word] = word_map[word] + 1

    max_freq = 0
    max_freq_word = ''
    for key in word_map:
        if word_map.get(key) > max_freq:
            max_freq = word_map.get(key)
            max_freq_word = key

    return max_freq_word


def get_punct_symbols():
    return [',', '.', '!', '?', '-', ':', ';']
