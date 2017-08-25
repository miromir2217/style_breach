from functools import reduce
import nltk.cluster
import numpy


distances = []


def get_clusters_k_means(vectors, k, distance_func, num_of_repeats):
    feature_vectors = [numpy.array(f) for f in vectors]
    clusterer = nltk.cluster.KMeansClusterer(
        num_means=k,
        distance=lambda x, y: distance_func(x, y),
        repeats=num_of_repeats,
        avoid_empty_clusters=True)
    return clusterer.cluster(vectors=feature_vectors, assign_clusters=True)


def get_cluster_error(vectors, clusters, num_of_clusters, distance_func):
    """
    :param vectors: the feature vectors
    :param clusters: the cluster assigned to each feature vector
    :param num_of_clusters: the number of clusters contained in the vector_pair
    :param distance_func: the distance function used during clustering
    :return: a floating point number representing the average error in the cluster configuration. The error for each
             cluster is the maximum difference between any two elements
    """
    if len(distances) == 0:
        for i in range(len(vectors)):
            distances.append([])
            for j in range(len(vectors)):
                distances[i].append(-1)

    max_distances = []
    for i in range(num_of_clusters):
        max_distances.append(0)

    for i in range(len(vectors)-1):
        for j in range(i+1, len(vectors)):
            if clusters[i] == clusters[j]:
                distance = distances[i][j] if distances[i][j] != -1 else distance_func(vectors[i], vectors[j])
                distances[i][j] = distance
                distances[j][i] = distance
                if distance > max_distances[clusters[i]]:
                    max_distances[clusters[i]] = distance

    return reduce(lambda x, y: x + y, max_distances) / num_of_clusters
