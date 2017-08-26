# style_breach

How to run the program:
    style_breach.py <file> <-dp|-kmeans|-experimental> <-dist|-cosine> [-show-truth]

where:
    <filename> - the input document to be analysed
    <-dp|-kmeans|-experimental> - the algorithm that would be used
        -dp: a custom clustering algorithm with similar idea to the dynamic programming solution of the knapsack problem
        -kmeans: k-means algorithm implementation from NLTK. It runs multiple times (k=[1; 8]) and chooses the best result
        -experimental: an agglomerative clustering algorithm from Scipy. Experimental run, as this not produce adequate results
    <-dist|-cosine> - the distance function that would be used during clustering
        -dist: a custom distance function, taking the difference between each dymention of the vector and then multiplying
               it by the difference of the positions of the sentences in the text. This is done to uplift the
               significance of the order of the sentences
        -cosine: a cosine similarity function from Scipy
    [-show-truth] - optional parameter that, if used, would print the expected results as well. Expects a file with the same
                    name as the input file, but with ".truth" extension found in the same folder as the input file