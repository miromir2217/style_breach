# style_breach

**How to run the program:**  
  
&nbsp;&nbsp;&nbsp;&nbsp;style_breach.py <file> <-dp|-kmeans|-experimental> <-dist|-cosine> [-show-truth]  
  
where:  
&nbsp;&nbsp;&nbsp;&nbsp;&lt;filename&gt; - the input document to be analysed  
&nbsp;&nbsp;&nbsp;&nbsp;&lt;-dp|-kmeans|-experimental&gt; - the algorithm that would be used  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-dp: a custom clustering algorithm with similar idea to the dynamic programming solution of the knapsack problem  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-kmeans: k-means algorithm implementation from NLTK. It runs multiple times (k=[1; 8]) and chooses the best result  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-experimental: an agglomerative clustering algorithm from Scipy. Experimental run, as this not produce adequate results  
&nbsp;&nbsp;&nbsp;&nbsp;&lt;-dist|-cosine&gt; - the distance function that would be used during clustering  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-dist: a custom distance function, taking the difference between each dymention of the vector and then multiplying  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;it by the difference of the positions of the sentences in the text. This is done to uplift the  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;significance of the order of the sentences  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-cosine: a cosine similarity function from Scipy  
&nbsp;&nbsp;&nbsp;&nbsp;[-show-truth] - optional parameter that, if used, would print the expected results as well. Expects a file with the same  
                    name as the input file, but with ".truth" extension found in the same folder as the input file  
