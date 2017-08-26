# style_breach

**How to run the program:**  
  
&nbsp;&nbsp;&nbsp;&nbsp;_style_breach.py <file> <-dp|-kmeans|-experimental> <-dist|-cosine> [-show-truth]_  
  
where:  
&nbsp;&nbsp;&nbsp;&nbsp;&lt;_*filename*_&gt; - the input document to be analysed  
&nbsp;&nbsp;&nbsp;&nbsp;&lt;_*-dp|-kmeans|-experimental*_&gt; - the algorithm that would be used  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_*-dp*_: a custom clustering algorithm with similar idea to the dynamic programming solution of the knapsack problem  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_*-kmeans*_: k-means algorithm implementation from NLTK. It runs multiple times (k=[1; 8]) and chooses the best result  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_*-experimental*_: an agglomerative clustering algorithm from Scipy. Experimental run, as this not produce adequate results  
&nbsp;&nbsp;&nbsp;&nbsp;&lt;_*-dist|-cosine*_&gt; - the distance function that would be used during clustering  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_*-dist*_: a custom distance function, taking the difference between each dymention of the vector and then multiplying it by the difference of the positions of the sentences in the text. This is done to uplift the significance of the order of the sentences  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_*-cosine*_: a cosine similarity function from Scipy  
&nbsp;&nbsp;&nbsp;&nbsp;_*[-show-truth]*_ - optional parameter that, if used, would print the expected results as well. Expects a file with the same name as the input file, but with ".truth" extension found in the same folder as the input file  
