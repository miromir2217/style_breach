import sys
from functools import reduce

from scipy.spatial import distance as scidist
from scipy.cluster import hierarchy as scihierarchy

import read_data
from cluster import clustering
from cluster import custom_clustering
from features import feature_extractor


def distance(vector1, vector2):
    dist = 0
    for i in range(1, len(vector1)):
        dist += abs(vector1[i] - vector2[i])

    return dist * float(abs(vector1[0] - vector2[0]))


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


def show_truth(input_filename):
    print('######### Expected output from truth file #########')
    output_filename = '.'.join(str(input_filename).split('.')[:-1]) + '.truth'
    with open(output_filename, 'r') as fin:
        print(fin.read())


def perform_custom_clustering(vectors, dist_func):
    custom_cluster = custom_clustering.knapsack_clustering(vectors, dist_func)
    print_output(sentences_starts, list(reversed(custom_cluster)))


def perform_k_means_clustering(vectors, dist_func, repeats, k=-1):
    start = 1
    end = 9
    if k > 0:
        start = k
        end = k+1

    min_error = 1000000
    best_clusters = []
    for _k in range(start, end):
        clusters = clustering.get_clusters_k_means(vectors=vectors, k=_k, distance_func=distance, num_of_repeats=repeats)
        error = clustering.get_cluster_error(vectors, clusters, _k, dist_func)
        if error < min_error:
            min_error = error
            best_clusters = clusters

    # attempt to "smooth" the result by reclassifying outliers
    n = len(vectors)
    for i in range(1, n-1):
        if best_clusters[i] != best_clusters[i-1]:
            if (i+1 < n and best_clusters[i+1] == best_clusters[i-1]) or \
                    (i+2 < n and best_clusters[i+2] == best_clusters[i-1]):
                best_clusters[i] = best_clusters[i-1]

    clusters = [0]
    for i in range(1, n):
        if best_clusters[i] != best_clusters[i-1]:
            clusters.append(i)

    print_output(sentences_starts, clusters)


# Experimental. Yielded no satisfactory results
def perform_hierarchical_clustering(vectors, dist_func):
    cluster = scihierarchy.fclusterdata(X=vectors, t=5, metric=dist_func)
    # cluster = scihierarchy.linkage(y=vectors, method='ward')
    # cluster = scihierarchy.linkage(y=vectors, method='average')
    # cluster = scihierarchy.linkage(y=vectors, method='complete')
    # cluster = scihierarchy.linkage(y=vectors, method='cosine')
    print(cluster)


def sentence_to_vector(_sentence, _sentences, sentence_pos):
    result_vector = list()
    result_vector.append(sentence_pos)  # position of the sentence in the document
    result_vector.append(len(feature_extractor.get_stop_words_in_sentence(_sentence)))  # number of stopwords
    result_vector.append(len(feature_extractor.get_non_stopwords_in_sentence(_sentence)))  # number of non-stop words
    result_vector.append(
        reduce(lambda x, y: x + y, map(lambda w: feature_extractor.get_word_freq(w, _sentence, _sentences), _sentence))
    )  # sum of score of each word

    symbols_freq = feature_extractor.get_punctuation_freq(_sentence, _sentences)
    for symbol in symbols_freq:
        result_vector.append(symbols_freq[symbol])  # frequency score of each punctuation symbol

    pos_tagged_sentences = feature_extractor.get_pos_tagged_words(_sentence)
    num_of_nouns = 0
    num_of_pronounces = 0
    num_of_adjectives = 0
    num_of_verbs = 0
    for tag_pair in pos_tagged_sentences:
        if str(tag_pair[1]).startswith('JJ'):
            num_of_adjectives += 1
        elif str(tag_pair[1]).startswith('NN'):
            num_of_nouns += 1
        elif str(tag_pair[1]).startswith('RB'):
            num_of_verbs += 1
        elif str(tag_pair[1]).startswith('PR'):
            num_of_pronounces += 1
    result_vector.append(num_of_pronounces)
    result_vector.append(num_of_nouns)
    result_vector.append(num_of_verbs)
    result_vector.append(num_of_adjectives)

    return result_vector


sentences_pairs = read_data.read_sentences_from_file(sys.argv[1])
sentences = list(map(lambda x: x[1], sentences_pairs))
sentences_starts = list(map(lambda x: x[0], sentences_pairs))

feature_vectors = []
position = 0
for sentence in sentences:
    position += 1
    feature_vectors.append(sentence_to_vector(sentence, sentences, position))

perform_custom_clustering(feature_vectors, distance)
# perform_custom_clustering(feature_vectors, scidist.coside)
# perform_k_means_clustering(vectors=feature_vectors, dist_func=distance, repeats=5, k=3)
# perform_k_means_clustering(vectors=feature_vectors, dist_func=scidist.cosine, repeats=5, k=3)
# perform_hierarchical_clustering(vectors=feature_vectors, dist_func=scidist.cosine)

show_truth(sys.argv[1])
