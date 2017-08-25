def dynamic_clustering(vectors, distance_func):
    """
    Method for clustering based on dynamic programming

    :param vectors: the input feature vectors
    :param distance_func: the function to calculate the distance between the vectors
    :return: an array of the clusters assigned
    """
    n = len(vectors)
    clusters = []
    cluster_dists = []
    for i in range(n):
        clusters.append([])
        cluster_dists.append([])
        for j in range(n):
            clusters[i].append(-1)
            cluster_dists[i].append(100000000)

    distances = get_distances(vectors, distance_func)
    cluster_dists[0][0] = distances[0][0]
    for i in range(n):
        for j in range(i+1):
            least_distance = 0
            coming_from = -1
            for k in range(j):
                if least_distance == 0 or cluster_dists[j-1][k] < least_distance:
                    least_distance = cluster_dists[j-1][k]
                    coming_from = k

            cluster_dists[i][j] = least_distance + get_avg_cluster_score(distances, j, i)
            clusters[i][j] = coming_from

    result = []
    best_last_cluster = 100000000
    column = -1
    for i in range(n):
        if cluster_dists[n-1][i] < best_last_cluster:
            best_last_cluster = cluster_dists[n-1][i]
            column = i

    result.append(column)
    row = column - 1
    column = clusters[n-1][column]
    while column != -1:
        result.append(column)
        old_row = row
        row = column - 1
        column = clusters[old_row][column]

    return result


def get_distances(vectors, distance_func):
    empty_vec = []
    for i in range(len(vectors[0])):
        empty_vec.append(0)

    distances = []
    for i in range(len(vectors)):
        distances.append([])
        for j in range(len(vectors)):
            distances[i].append(0)

    for i in range(len(vectors)):
        for j in range(i, len(vectors)):
            distance = distance_func(vectors[i], vectors[j]) if i != j else distance_func(vectors[i], empty_vec)
            distances[i][j] = distance
            distances[j][i] = distance

    return distances


def get_avg_cluster_score(distances, left, right):
    if left == right:
        return distances[left][right]

    score = 0
    count = 0
    for i in range(left, right):
        for j in range(i+1, right+1):
            score += distances[i][j]
            count += 1

    return score / count
