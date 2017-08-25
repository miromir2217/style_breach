# imports

import sys
from functools import reduce

import numpy

import feature_extractor
import read_data
from scipy.spatial import distance as scidist
from scipy.cluster import hierarchy as scihierarchy
from cluster import clustering
from cluster import custom_clustering


# functions

def distance(vector1, vector2):
    dist = 0
    for i in range(1, len(vector1)):
        dist += abs(vector1[i] - vector2[i])

    return dist
    # return dist * float(abs(vector1[0] - vector2[0]))


def print_output(positions, clusters):
    result = []
    for i in clusters:
        if i != 0:
            result.append(positions[i])

    print('{')
    if len(result) == 0:
        print('\t"borders": []')
    else:
        print('\t"borders": ' + '[%s]' % ', '.join(map(str, result)))
    print('}')


def perform_custom_clustering(vectors, distance):
    custom_cluster = custom_clustering.dynamic_clustering(vectors, distance)
    print_output(sentences_starts, list(reversed(custom_cluster)))


def perform_k_means_clustering(vectors, distance, k, repeats):
    min_error = 1000000
    best_clusters = []
    print("for k = " + str(3))
    clusters = clustering.get_clusters_k_means(vectors=vectors, k=k, distance_func=distance, num_of_repeats=repeats)
    error = clustering.get_cluster_error(vectors, clusters, k, distance)
    if error < min_error:
        min_error = error
        best_clusters = clusters

    numpy.set_printoptions(suppress=True)
    print('Clusters: ')
    print(best_clusters)

    print('Cluster error: ')
    print(min_error)


# main script

sentences_pairs = read_data.read_sentences_from_file(sys.argv[1])
sentences = list(map(lambda x: x[1], sentences_pairs))
sentences_starts = list(map(lambda x: x[0], sentences_pairs))

feature_vectors = []
position = 0
for sentence in sentences:
    punct_freq = feature_extractor.get_punctuation_freq(sentence)
    position += 1
    vector = [
        # position
        position,
        # number of stopwords
        len(feature_extractor.get_stop_words_in_sentence(sentence)),
        # number of non-stop words
        len(feature_extractor.get_non_stopwords_in_sentence(sentence)),
        # sum of score of each word
        reduce(lambda x, y: x + y, map(lambda w: feature_extractor.get_word_freq(w, sentence, sentences), sentence)),
        # freq
    ]
    feature_vectors.append(vector)

# cluster = scihierarchy.fclusterdata(X=feature_vectors, t=10000, metric=scidist.cosine)
# print(cluster)

# perform_custom_clustering(feature_vectors, scidist.cosine)
perform_k_means_clustering(vectors=feature_vectors, distance=scidist.cosine, k=3, repeats=5)