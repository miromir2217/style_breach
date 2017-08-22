# imports

import sys
import nltk.cluster
from functools import reduce
import numpy

import read_data
import feature_extractor


# functions
def distance(vector1, vector2):
    dist = 0
    for i in range(1, len(vector1)):
        dist += abs(vector1[i] - vector2[i])

    return dist

# main script

sentences = read_data.read_sentences_from_file(sys.argv[1])
# for sentence in sentences:
#     print('--------------------------')
#     print('Sentence: ' + ''.join(reduce((lambda x, y: x + ' ' + y), sentence)) + '\n')
#     stopwords = feature_extractor.get_stop_words_in_sentence(sentence)
#     print('stopwords: ' +
#           ''.join(reduce((lambda x, y: x + ', ' + y), stopwords))
#           if stopwords != []
#           else '')
#     pos_tagged_words = feature_extractor.get_pos_tagged_words(sentence)
#     print('pos-tagged: ' +
#           ''.join(
#               reduce(
#                   (lambda x, y: x + ', ' + y),
#                   list(map((lambda x: '(' + x[0] + ', ' + x[1] + ')'), pos_tagged_words))))
#           if pos_tagged_words != [] else '')
#     for word in sentence:
#         print(word + ' freq score: ' + str(feature_extractor.get_word_freq(word, sentence, sentences)))
#     punct_freq = feature_extractor.get_punctuation_freq(sentence)
#     print(punct_freq)
#     print('--------------------------')

feature_vectors = []
for sentence in sentences:
    punct_freq = feature_extractor.get_punctuation_freq(sentence)
    vector = [
        # number of stopwords
        len(feature_extractor.get_stop_words_in_sentence(sentence)),
        # number of non-stop words
        len(feature_extractor.get_non_stopwords_in_sentence(sentence)),
        # sum of score of each word
        reduce(lambda x, y: x + y, map(lambda w: feature_extractor.get_word_freq(w, sentence, sentences), sentence)),
        # freq
    ]
    feature_vectors.append(vector)

feature_vectors = [numpy.array(f) for f in feature_vectors]
clusterer = nltk.cluster.KMeansClusterer(num_means=3, distance=(lambda x, y: distance(x, y)))
clusters = clusterer.cluster(vectors=feature_vectors, assign_clusters=True)

numpy.set_printoptions(suppress=True)
print('Clustered: ')
print(feature_vectors)

print('Clusters: ')
print(clusters)

print('Means: ')
print(clusterer.means())
